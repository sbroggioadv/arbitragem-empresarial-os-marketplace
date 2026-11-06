#!/usr/bin/env python3
"""calc_arbitragem_custas.py - custas arbitrais pela tabela capturada.

Conta aberta, metodo e CAMPOS: context/calculo-custas-arbitrais.md.

USO:
    python3 calc_arbitragem_custas.py --entrada caso.json
    echo '{...}' | python3 calc_arbitragem_custas.py
    python3 calc_arbitragem_custas.py --versao

Saida: JSON no stdout. Exit 0 = calculado; 2 = entrada invalida (JSON de erro);
3 = formula aberta (tabela ausente ou fora do intervalo, valor entre faixas,
ou duas leituras que mudam o resultado). Nunca estima.

So biblioteca padrao, Python 3.9+, sem rede. As tabelas ficam em data/, ao lado
deste arquivo: custas-cam-ccbc-2025.json e custas-camarb-2019-emergencia.json,
cada uma com fonte (arquivo de context/ e linha Ln) e data de captura.
CAM B3 2026 e a tabela geral da CAMARB nao foram incorporadas: PENDENTE DE FONTE.
"""

import argparse
import json
import sys
from decimal import ROUND_HALF_UP, Decimal, InvalidOperation
from pathlib import Path

VERSAO = "0.1.0"
EXIT_OK, EXIT_ENTRADA, EXIT_FORMULA = 0, 2, 3

PASTA = Path(__file__).resolve().parent
DADOS_CCBC = PASTA / "data" / "custas-cam-ccbc-2025.json"
DADOS_CAMARB = PASTA / "data" / "custas-camarb-2019-emergencia.json"

CAMARAS = ("cam-ccbc-2025", "camarb-2019", "cam-b3-2026", "outra")
ARBITROS = ("unico", "tres", "indefinido")
PROCEDIMENTOS = ("comum", "expedito", "indefinido")
POLOS = ("requerente", "requerida", "indefinido")
INCIDENTES = ("esclarecimentos", "impugnacao", "emergencia")

# Contrato da entrada. A skill e o context/calculo-custas-arbitrais.md declaram o mesmo
# conjunto no bloco ```campos```; tests/test_contrato.py compara os dois lados.
CAMPOS = {
    "camara": {"tipo": "enum", "obrigatorio": "sim", "valores": "|".join(CAMARAS)},
    "valor_causa": {"tipo": "decimal", "obrigatorio": "condicional",
                    "valores": "cam-ccbc-2025 sem pedidos; soma dos pedidos das partes (L206)"},
    "pedidos": {"tipo": "lista", "obrigatorio": "condicional",
                "valores": "alternativa a valor_causa; um decimal por pedido; a soma e o valor da causa"},
    "arbitros": {"tipo": "enum", "obrigatorio": "nao", "valores": "|".join(ARBITROS)},
    "procedimento": {"tipo": "enum", "obrigatorio": "nao", "valores": "|".join(PROCEDIMENTOS)},
    "polo": {"tipo": "enum", "obrigatorio": "nao", "valores": "|".join(POLOS)},
    "incidentes": {"tipo": "lista", "obrigatorio": "nao", "valores": "|".join(INCIDENTES)},
    "arbitros_impugnados": {"tipo": "inteiro", "obrigatorio": "nao", "valores": "com impugnacao; padrao 1"},
}

CENTAVO = Decimal("0.01")
CEM = Decimal(100)
TOLERANCIA = Decimal("0.01")
LIMITE_MAGNITUDE = Decimal("1e15")
AVISO_FIXO = ("Conferir na camara antes de orcar ou recolher: a tabela e a captura de 2026-10-02; "
              "o numero nao substitui a conferencia do advogado.")


class EntradaInvalida(Exception):
    pass


# ---------------------------------------------------------------- entrada

def _dec(campo, valor):
    if isinstance(valor, bool) or not isinstance(valor, (str, int)):
        raise EntradaInvalida(f"{campo}: esperado numero decimal em texto, com ponto (ex.: \"3000000.00\")")
    try:
        v = Decimal(str(valor).strip())
    except (InvalidOperation, ValueError):
        raise EntradaInvalida(f"{campo}: numero invalido")
    if not v.is_finite() or v.copy_abs() >= LIMITE_MAGNITUDE:
        raise EntradaInvalida(f"{campo}: numero fora do intervalo suportado")
    if v <= 0:
        raise EntradaInvalida(f"{campo}: tem de ser positivo")
    if v != v.quantize(CENTAVO):
        raise EntradaInvalida(f"{campo}: no maximo duas casas decimais")
    return v


def _opcao(campo, valor, opcoes, padrao):
    if valor is None:
        return padrao
    if valor not in opcoes:
        raise EntradaInvalida(f"{campo}: valor '{valor}' fora de {list(opcoes)}")
    return valor


def ler_entrada(e):
    if not isinstance(e, dict):
        raise EntradaInvalida("entrada: esperado objeto JSON")
    extras = set(e) - set(CAMPOS)
    if extras:
        raise EntradaInvalida(f"campos desconhecidos: {sorted(extras)}")
    if "camara" not in e:
        raise EntradaInvalida("camara: obrigatorio")
    out = {"camara": _opcao("camara", e["camara"], CAMARAS, None)}
    if "valor_causa" in e and "pedidos" in e:
        raise EntradaInvalida("informe valor_causa OU pedidos, nao os dois")
    out["pedidos"] = None
    out["valor_causa"] = None
    if "pedidos" in e:
        if not isinstance(e["pedidos"], list) or not e["pedidos"]:
            raise EntradaInvalida("pedidos: lista nao vazia de decimais")
        out["pedidos"] = [_dec(f"pedidos[{i}]", p) for i, p in enumerate(e["pedidos"])]
        out["valor_causa"] = sum(out["pedidos"], Decimal(0))
    elif "valor_causa" in e:
        out["valor_causa"] = _dec("valor_causa", e["valor_causa"])
    out["arbitros"] = _opcao("arbitros", e.get("arbitros"), ARBITROS, "indefinido")
    out["procedimento"] = _opcao("procedimento", e.get("procedimento"), PROCEDIMENTOS, "indefinido")
    out["polo"] = _opcao("polo", e.get("polo"), POLOS, "indefinido")
    inc = e.get("incidentes", [])
    if not isinstance(inc, list):
        raise EntradaInvalida("incidentes: lista")
    out["incidentes"] = [_opcao(f"incidentes[{i}]", x, INCIDENTES, None) for i, x in enumerate(inc)]
    n = e.get("arbitros_impugnados", 1)
    if isinstance(n, bool) or not isinstance(n, int) or not 1 <= n <= 3:
        raise EntradaInvalida("arbitros_impugnados: inteiro de 1 a 3")
    if "arbitros_impugnados" in e and "impugnacao" not in out["incidentes"]:
        raise EntradaInvalida("arbitros_impugnados: so com o incidente 'impugnacao'")
    out["arbitros_impugnados"] = n
    return out


def eco(e):
    """parametros_usados: eco da entrada normalizada, decimais como texto."""
    r = {}
    for k, v in e.items():
        if isinstance(v, Decimal):
            r[k] = str(v)
        elif isinstance(v, list):
            r[k] = [str(x) if isinstance(x, Decimal) else x for x in v]
        else:
            r[k] = v
    return r


# ---------------------------------------------------------------- tabelas

def carregar(caminho):
    with open(caminho, encoding="utf-8") as f:
        return json.load(f)


def _brl(v):
    s = f"{v.quantize(CENTAVO, ROUND_HALF_UP):,.2f}"
    return "R$ " + s.replace(",", "X").replace(".", ",").replace("X", ".")


def _faixa_contem(f, v):
    de = Decimal(f["de"]) if f["de"] else None
    ate = Decimal(f["ate"]) if f["ate"] else None
    return (de is None or v >= de) and (ate is None or v <= ate)


def selecionar_faixa(faixas, v):
    """Caminho 1: primeira faixa, de cima para baixo, cujo limite superior alcanca v."""
    for f in faixas:
        ate = Decimal(f["ate"]) if f["ate"] else None
        if ate is None or v <= ate:
            return f if _faixa_contem(f, v) else None
    return None


def reselecionar_faixa(faixas, v):
    """Caminho 2: todas as faixas que contem v; tem de haver exatamente uma."""
    achadas = [f for f in faixas if _faixa_contem(f, v)]
    return achadas[0] if len(achadas) == 1 else None


def conta_linha(f, v):
    """Conta 1: fixo + pct% x (v - base). Conta 2: fixo + (v x pct - base x pct) / 100."""
    fixo = Decimal(f["fixo"])
    if not f["pct"]:
        return fixo, fixo, f"{_brl(fixo)} (parcela fixa da faixa, sem percentual)"
    pct, base = Decimal(f["pct"]), Decimal(f["base"])
    excedente = v - base
    c1 = fixo + pct * excedente / CEM
    c2 = fixo + (v * pct - base * pct) / CEM
    txt = (f"{_brl(fixo)} + {f['pct']}% x ({_brl(v)} - {_brl(base)}) = {_brl(fixo)} + "
           f"{f['pct']}% x {_brl(excedente)} = {c1}")
    return c1, c2, txt


def rubrica_tabela(dados, chave, v, rotulo):
    tab = dados["tabelas"][chave]
    faixas = tab["faixas"]
    f1 = selecionar_faixa(faixas, v)
    f2 = reselecionar_faixa(faixas, v)
    if f1 is None or f2 is None or f1["ln"] != f2["ln"]:
        return None, {
            "rubrica": rotulo,
            "motivo": (f"o valor {_brl(v)} nao cabe em uma unica faixa de {tab['nome']} "
                       f"({dados['fonte']} {tab['ln_cabecalho']}): valor entre faixas ou fora do intervalo"),
            "formula": "parcela fixa da faixa + percentual da faixa x (valor da causa - 'do valor superior a' da faixa)",
            "falta": "confirmar com a camara a faixa aplicavel",
        }
    c1, c2, txt = conta_linha(f1, v)
    if (c1 - c2).copy_abs() > TOLERANCIA:
        return None, {"rubrica": rotulo, "motivo": "as duas contas divergem alem de centavos",
                      "formula": txt, "falta": "conferencia manual"}
    valor = c1.quantize(CENTAVO, ROUND_HALF_UP)
    return {
        "rubrica": rotulo,
        "valor": str(valor),
        "valor_brl": _brl(valor),
        "regra": f"{tab['nome']}: {txt}; arredondamento ao centavo (ROUND_HALF_UP)",
        "fonte": f"{dados['fonte']} {f1['ln']} (cabecalho {tab['ln_cabecalho']}); captura {dados['data_captura']}",
        "faixa": {"de": f1["de"], "ate": f1["ate"], "ln": f1["ln"]},
        "segunda_conta": {
            "faixa_reselecionada": f2["ln"],
            "conta_1": str(c1), "conta_2": str(c2),
            "diferenca": str((c1 - c2).copy_abs()),
        },
    }, None


def valor_fixo(rotulo, valor, fonte, regra):
    v = Decimal(valor)
    return {"rubrica": rotulo, "valor": str(v), "valor_brl": _brl(v), "regra": regra, "fonte": fonte}


# ---------------------------------------------------------------- cenarios

def cenario_ccbc(dados, e, procedimento):
    """Custas principais e incidentes do CAM-CCBC 2025 para um procedimento (comum|expedito)."""
    v = e["valor_causa"]
    F = dados["fonte"]
    exp = procedimento == "expedito"
    itens, abertas = [], []
    sufixo = "_exp" if exp else "_comum"

    itens.append(valor_fixo(
        "taxa de registro (requerente, antes do requerimento)", dados["taxa_registro"]["valor"],
        f"{F} {dados['taxa_registro']['ln']}, {dados['taxa_registro']['responsavel_ln']}, "
        f"{dados['taxa_registro']['momento_ln']}; captura {dados['data_captura']}",
        "valor fixo do item 20; nao compensavel nem reembolsavel"))

    adm, ab = rubrica_tabela(dados, "adm" + sufixo, v, "taxa de administracao")
    if adm:
        itens.append(adm)
    else:
        abertas.append(ab)

    arbitros = ["unico", "tres"] if e["arbitros"] == "indefinido" else [e["arbitros"]]
    honorarios = {}
    for a in arbitros:
        chave = ("unico" if a == "unico" else "trino") + sufixo
        rotulo = "honorarios do arbitro unico" if a == "unico" else "honorarios do tribunal de tres arbitros"
        h, ab = rubrica_tabela(dados, chave, v, rotulo)
        if h:
            if a == "tres":
                div = dados["divisao_trino"]
                total = Decimal(h["valor"])
                h["divisao"] = {
                    "presidente": str((total * Decimal(div["presidente"])).quantize(CENTAVO, ROUND_HALF_UP)),
                    "cada_coarbitro": str((total * Decimal(div["coarbitro"])).quantize(CENTAVO, ROUND_HALF_UP)),
                    "fonte": f"{F} {div['ln']}",
                }
            honorarios[a] = h
        else:
            abertas.append(ab)

    totais = {}
    for a, h in honorarios.items():
        if adm:
            soma = Decimal(adm["valor"]) + Decimal(h["valor"])
            fr = Decimal(dados["rateio_polos"]["fracao"])
            rat = dados["rateio_polos"]
            lns = (f"{rat['adm_exp_ln']}, {rat['honorarios_exp_ln']}" if exp
                   else f"{rat['adm_comum_ln']}, {rat['honorarios_comum_ln']}")
            totais[a] = {
                "taxa_adm_mais_honorarios": str(soma),
                "parcela_de_cada_polo": str((soma * fr).quantize(CENTAVO, ROUND_HALF_UP)),
                "regra": "taxa de administracao + honorarios; rateio de 50% para cada polo",
                "fonte": f"{F} {lns}",
            }
            if exp and a == "unico":
                teto = Decimal(dados["teto_expedito_unico"]["valor"])
                excesso = soma - teto
                totais[a]["teto_item_64"] = {
                    "teto": str(teto), "dentro_do_teto": soma <= teto,
                    "excesso": str(excesso) if excesso > 0 else "0.00",
                    "observacao": ("a soma das parcelas arredondadas passa o teto; o item 64 limita a taxa de "
                                   "administracao + honorarios do arbitro unico ao teto [VERIFICAR com a camara]"
                                   if excesso > 0 else "soma dentro do teto do item 64"),
                    "fonte": f"{F} {dados['teto_expedito_unico']['ln']}",
                }

    inc = []
    for x in e["incidentes"]:
        if x == "esclarecimentos":
            if exp:
                d = dados["esclarecimentos_expedito"]
                inc.append(valor_fixo("honorarios adicionais para esclarecimentos (expedito)", d["valor"],
                                      f"{F} {d['ln']}", "valor fixo do item 67"))
            else:
                r, ab = rubrica_tabela(dados, "esclarecimentos_comum", v,
                                       "honorarios adicionais para esclarecimentos")
                (inc.append(r) if r else abertas.append(ab))
        elif x == "impugnacao":
            d = dados["impugnacao_por_arbitro"]["expedito" if exp else "comum"]
            n = e["arbitros_impugnados"]
            tot = Decimal(d["valor"]) * n
            inc.append({"rubrica": f"custas do incidente de impugnacao ({n} arbitro(s))",
                        "valor": str(tot), "valor_brl": _brl(tot),
                        "regra": f"{_brl(Decimal(d['valor']))} por arbitro impugnado x {n}",
                        "fonte": f"{F} {d['ln']}"})
        elif x == "emergencia":
            d = dados["emergencia"]
            soma = sum((Decimal(p["valor"]) for p in d["partes"]), Decimal(0))
            item = valor_fixo("deposito do arbitro de emergencia", d["total"], f"{F} {d['ln']}",
                              " + ".join(f"{_brl(Decimal(p['valor']))} ({p['rubrica']}, {p['ln']})"
                                         for p in d["partes"]) + f" = {_brl(soma)}")
            item["confere_com_o_total"] = soma == Decimal(d["total"])
            inc.append(item)
    return {"procedimento": procedimento, "itens": itens, "honorarios": honorarios,
            "totais": totais, "incidentes": inc}, abertas


def calcular_ccbc(dados, e):
    avisos, leituras = [AVISO_FIXO], []
    for r in dados["ressalvas"]:
        avisos.append(r["texto"] + (f" ({dados['fonte']} {', '.join(r['ln'])})" if r["ln"] else ""))
    avisos.append(f"vigencia: {dados['vigencia_declarada']}")
    if e["valor_causa"] is None:
        return EXIT_FORMULA, {
            "cenarios": [],
            "formula_aberta": {
                "motivo": "sem o valor da causa (soma dos pedidos das partes) nao ha conta",
                "formula": "valor da causa = soma dos pedidos (L206); depois, a faixa de cada tabela",
                "falta": ["valor_causa ou pedidos"],
            },
            "avisos": avisos,
        }
    v = e["valor_causa"]
    lim = dados["limite_expedito"]
    limite = Decimal(lim["valor"])
    proc = e["procedimento"]
    if proc == "expedito" and v > limite:
        return EXIT_FORMULA, {
            "cenarios": [],
            "formula_aberta": {
                "motivo": (f"as tabelas do expedito so alcancam valor em disputa inferior a {_brl(limite)} "
                           f"({dados['fonte']} {lim['custas_ln']}); o valor informado e {_brl(v)}"),
                "formula": "procedimento comum: Tabelas 1 a 3",
                "falta": ["confirmar o procedimento com a camara"],
            },
            "avisos": avisos,
        }
    if v == limite and proc in ("expedito", "indefinido"):
        # Duas leituras que mudam o resultado: custas item 54 'inferior a' x regulamento 36.1 'nao exceda'.
        cen = []
        for p in ("comum", "expedito"):
            c, ab = cenario_ccbc(dados, e, p)
            c["leitura"] = ("custas item 54: 'inferior a' R$ 3.000.000,00 exclui o valor exato"
                            if p == "comum" else
                            "regulamento 36.1: 'nao exceda' o valor fixado inclui o valor exato")
            cen.append(c)
        return EXIT_FORMULA, {
            "cenarios": cen,
            "formula_aberta": {
                "motivo": (f"valor exatamente {_brl(limite)}: o regramento de custas exige valor 'inferior a' "
                           f"({dados['fonte']} {lim['custas_ln']}) e o regulamento usa 'nao exceda' "
                           f"({lim['regulamento']} {lim['regulamento_ln']}); as duas leituras mudam o rito e a tabela"),
                "formula": "as duas contas acima, sem escolher",
                "falta": ["confirmar com a Secretaria do CAM-CCBC o rito e a tabela aplicaveis [VERIFICAR]"],
            },
            "avisos": avisos,
        }
    procs = [proc] if proc != "indefinido" else (["comum", "expedito"] if v < limite else ["comum"])
    cen, abertas = [], []
    for p in procs:
        c, ab = cenario_ccbc(dados, e, p)
        if proc == "indefinido" and p == "expedito":
            c["leitura"] = ("cenario alternativo: o expedito exige, cumulativamente, valor inferior ao limite e "
                            f"procedimento regido pelos arts. 36 e 37 ({dados['fonte']} {lim['custas_ln']})")
        cen.append(c)
        abertas += ab
    out = {"cenarios": cen, "formula_aberta": None, "avisos": avisos}
    if abertas:
        out["formula_aberta"] = {"motivo": "rubricas sem conta", "itens": abertas,
                                 "falta": [a["falta"] for a in abertas]}
        return EXIT_FORMULA, out
    return EXIT_OK, out


def calcular_camarb(dados, e):
    avisos = [AVISO_FIXO, f"vigencia: {dados['vigencia_declarada']}"]
    for r in dados["ressalvas"]:
        avisos.append(r["texto"] + f" ({dados['fonte']} {', '.join(r['ln'])})")
    F = dados["fonte"]
    itens, falta = [], []
    if "emergencia" in e["incidentes"]:
        d = dados["deposito"]
        soma = sum((Decimal(p["valor"]) for p in d["partes"]), Decimal(0))
        it = valor_fixo("deposito do arbitro de emergencia (RA 06/20)", d["total"], f"{F} {d['ln']}",
                        " + ".join(f"{_brl(Decimal(p['valor']))} ({p['rubrica']}, {p['ln']})"
                                   for p in d["partes"]) + f" = {_brl(soma)}")
        it["confere_com_o_total"] = soma == Decimal(d["total"])
        it["aplicacao"] = f"so convencao firmada apos 12/08/2019, salvo disposicao em contrario ({F} {dados['aplicacao_ln']})"
        itens.append(it)
    if "impugnacao" in e["incidentes"]:
        d = dados["impugnacao_taxa"]
        itens.append(valor_fixo("taxa da impugnacao ao arbitro de emergencia (RA 06/20)", d["valor"],
                                f"{F} {d['ln']}", "valor fixo do item 9.3 da RA 06/20"))
    principais = e["valor_causa"] is not None or e["arbitros"] != "indefinido" or e["procedimento"] != "indefinido" \
        or not e["incidentes"] or "esclarecimentos" in e["incidentes"]
    if principais:
        falta.append("tabela geral de custas da CAMARB (taxa de administracao, honorarios, esclarecimentos): "
                     "capturada, mas nao incorporada nem analisada nesta versao - PENDENTE DE FONTE")
    out = {"cenarios": [{"procedimento": "camarb-2019", "itens": itens}], "formula_aberta": None, "avisos": avisos}
    if falta:
        out["formula_aberta"] = {"motivo": "sem tabela incorporada", "formula": None, "falta": falta}
        return EXIT_FORMULA, out
    return EXIT_OK, out


def calcular(e):
    if e["camara"] == "cam-ccbc-2025":
        return calcular_ccbc(carregar(DADOS_CCBC), e)
    if e["camara"] == "camarb-2019":
        return calcular_camarb(carregar(DADOS_CAMARB), e)
    motivo = ("CAM B3 2026: pagina de custas sem versao declarada; tabela nao incorporada"
              if e["camara"] == "cam-b3-2026" else "camara sem tabela no plugin")
    return EXIT_FORMULA, {"cenarios": [], "avisos": [AVISO_FIXO],
                          "formula_aberta": {"motivo": motivo + " - PENDENTE DE FONTE", "formula": None,
                                             "falta": ["tabela oficial da camara, com versao e data"]}}


# ---------------------------------------------------------------- cli

def build_parser():
    p = argparse.ArgumentParser(
        prog="calc_arbitragem_custas.py",
        description="Custas arbitrais pela tabela capturada (CAM-CCBC 2025; RA 06/20 da CAMARB). "
                    "Entrada JSON por --entrada ou stdin.")
    p.add_argument("--entrada", help="arquivo JSON de entrada (sem ele, le o stdin)")
    p.add_argument("--versao", action="store_true", help="imprime a versao e sai")
    return p


def main(argv=None):
    args = build_parser().parse_args(argv)
    if args.versao:
        print(json.dumps({"script": "calc_arbitragem_custas.py", "versao": VERSAO}))
        return EXIT_OK
    try:
        bruto = (open(args.entrada, encoding="utf-8").read() if args.entrada else sys.stdin.read())
        try:
            e = json.loads(bruto)
        except json.JSONDecodeError as exc:
            raise EntradaInvalida(f"JSON invalido: {exc.msg} (linha {exc.lineno})")
        e = ler_entrada(e)
        codigo, corpo = calcular(e)
    except EntradaInvalida as exc:
        print(json.dumps({"erro": str(exc), "versao": VERSAO}, ensure_ascii=False))
        return EXIT_ENTRADA
    except Exception as exc:  # nunca traceback com exit 1
        print(json.dumps({"erro": f"falha inesperada: {type(exc).__name__}: {exc}", "versao": VERSAO},
                         ensure_ascii=False))
        return EXIT_ENTRADA
    saida = {"script": "calc_arbitragem_custas.py", "versao": VERSAO, "parametros_usados": eco(e)}
    saida.update(corpo)
    print(json.dumps(saida, ensure_ascii=False, indent=1))
    return codigo


if __name__ == "__main__":
    sys.exit(main())
