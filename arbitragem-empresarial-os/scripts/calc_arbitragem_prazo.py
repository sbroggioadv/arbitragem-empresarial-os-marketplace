#!/usr/bin/env python3
"""calc_arbitragem_prazo.py - data-limite de prazo arbitral pela regra do regulamento.

Conta aberta, metodo e CAMPOS: context/calculo-prazo-arbitral.md.

USO:
    python3 calc_arbitragem_prazo.py --entrada caso.json
    echo '{...}' | python3 calc_arbitragem_prazo.py
    python3 calc_arbitragem_prazo.py --versao

Saida: JSON no stdout. Exit 0 = calculado; 2 = entrada invalida (JSON de erro);
3 = formula aberta (marco sem documento, calendario nao informado ou que nao
cobre o periodo, prazo fora do regulamento, regime sem regra). Nunca estima.

So biblioteca padrao, Python 3.9+, sem rede. A regra de contagem de cada camara e
o catalogo de prazos ficam em data/contagem-prazos-arbitrais.json, com fonte
(arquivo de context/ e linha Ln). Nao ha calendario embutido: feriados no local
da sede, dias sem expediente da camara e recesso sao sempre entrada; sabado e
domingo sao tratados como dias sem expediente (premissa declarada na saida).

Nao e o engine B da familia (contagem processual do CPC): a contagem arbitral
segue o regulamento escolhido pelas partes.
"""

import argparse
import datetime as dt
import json
import sys
from pathlib import Path

VERSAO = "0.1.0"
EXIT_OK, EXIT_ENTRADA, EXIT_FORMULA = 0, 2, 3

PASTA = Path(__file__).resolve().parent
DADOS = PASTA / "data" / "contagem-prazos-arbitrais.json"

REGIMES = ("cam-ccbc-2025", "camarb-2019", "cam-b3-2026", "sem-regulamento")
UNIDADES = ("continuos", "uteis")
UM_DIA = dt.timedelta(days=1)
DATA_MIN, DATA_MAX = dt.date(2000, 1, 1), dt.date(2100, 12, 31)
MAX_DIAS = 365
DIAS_SEMANA = ("segunda", "terca", "quarta", "quinta", "sexta", "sabado", "domingo")


def _ids_catalogo():
    try:
        with open(DADOS, encoding="utf-8") as f:
            return tuple(p["id"] for p in json.load(f)["prazos"])
    except (OSError, ValueError, KeyError):
        return ()


PRAZO_IDS = _ids_catalogo()

# Contrato da entrada. A skill e o context/calculo-prazo-arbitral.md declaram o mesmo
# conjunto no bloco ```campos```; tests/test_contrato.py compara os dois lados.
CAMPOS = {
    "regime": {"tipo": "enum", "obrigatorio": "sim", "valores": "|".join(REGIMES)},
    "prazo_id": {"tipo": "enum", "obrigatorio": "condicional", "valores": "sem prazo_dias; id do catalogo"},
    "prazo_dias": {"tipo": "inteiro", "obrigatorio": "condicional",
                   "valores": "sem prazo_id; prazo do Termo, de ordem ou da convencao"},
    "prazo_fonte": {"tipo": "texto", "obrigatorio": "condicional", "valores": "com prazo_dias; documento e trecho"},
    "unidade": {"tipo": "enum", "obrigatorio": "nao", "valores": "|".join(UNIDADES)},
    "marco": {"tipo": "data", "obrigatorio": "sim", "valores": "AAAA-MM-DD; o evento que o regulamento manda contar"},
    "marco_documentado": {"tipo": "bool", "obrigatorio": "sim",
                          "valores": "true so com documento que constitui ou comprova o evento"},
    "dias_nao_uteis": {"tipo": "lista", "obrigatorio": "sim",
                       "valores": "datas sem expediente no periodo (feriados da sede, dias sem expediente da camara); [] = nenhum"},
    "recesso": {"tipo": "lista", "obrigatorio": "sim",
                "valores": "periodos de recesso da camara no periodo, {inicio, fim}; [] = nenhum"},
    "calendario_conferido_ate": {"tipo": "data", "obrigatorio": "sim",
                                 "valores": "ultima data coberta pelo calendario informado"},
    "acordo_afasta_recesso": {"tipo": "bool", "obrigatorio": "nao", "valores": "cam-ccbc-2025; padrao false"},
}

PREMISSA_FDS = ("sabado e domingo tratados como dias sem expediente; conferir no calendario oficial da camara")
AVISO_FIXO = ("Conferir a data no calendario oficial da camara e nos documentos do caso antes de confiar nela; "
              "o numero nao substitui a conferencia do advogado.")


class EntradaInvalida(Exception):
    pass


class ForaDoCalendario(Exception):
    pass


def _data(campo, valor):
    if not isinstance(valor, str):
        raise EntradaInvalida(f"{campo}: esperado texto AAAA-MM-DD")
    try:
        d = dt.date.fromisoformat(valor)
    except ValueError:
        raise EntradaInvalida(f"{campo}: data invalida '{valor}' (use AAAA-MM-DD)")
    if not DATA_MIN <= d <= DATA_MAX:
        raise EntradaInvalida(f"{campo}: data fora do intervalo suportado (2000-01-01 a 2100-12-31)")
    return d


def _bool(campo, valor):
    if not isinstance(valor, bool):
        raise EntradaInvalida(f"{campo}: esperado true ou false")
    return valor


def ler_entrada(e, dados):
    if not isinstance(e, dict):
        raise EntradaInvalida("entrada: esperado objeto JSON")
    extras = set(e) - set(CAMPOS)
    if extras:
        raise EntradaInvalida(f"campos desconhecidos: {sorted(extras)}")
    if e.get("regime") not in REGIMES:
        raise EntradaInvalida(f"regime: obrigatorio, um de {list(REGIMES)}")
    out = {"regime": e["regime"]}
    if ("prazo_id" in e) == ("prazo_dias" in e):
        raise EntradaInvalida("informe prazo_id (catalogo) OU prazo_dias (com prazo_fonte)")
    catalogo = {p["id"]: p for p in dados["prazos"]}
    if "prazo_id" in e:
        if e["prazo_id"] not in catalogo:
            raise EntradaInvalida(f"prazo_id: '{e['prazo_id']}' fora do catalogo {sorted(catalogo)}")
        if "prazo_fonte" in e or "unidade" in e:
            raise EntradaInvalida("prazo_fonte e unidade so com prazo_dias; o catalogo ja traz os dois")
        out["prazo"] = dict(catalogo[e["prazo_id"]])
    else:
        n = e["prazo_dias"]
        if isinstance(n, bool) or not isinstance(n, int) or not 1 <= n <= MAX_DIAS:
            raise EntradaInvalida(f"prazo_dias: inteiro de 1 a {MAX_DIAS}")
        fonte = e.get("prazo_fonte")
        if not isinstance(fonte, str) or not fonte.strip():
            raise EntradaInvalida("prazo_fonte: obrigatorio com prazo_dias (documento e trecho que fixam o prazo)")
        un = e.get("unidade", "continuos")
        if un not in UNIDADES:
            raise EntradaInvalida(f"unidade: um de {list(UNIDADES)}")
        out["prazo"] = {"id": None, "regimes": [out["regime"]], "dias": n, "unidade": un,
                        "fonte": fonte.strip(), "ln": None, "evento": "o indicado no documento",
                        "observacao": "prazo informado pelo usuario (Termo, ordem ou convencao)"}
    if "marco" not in e:
        raise EntradaInvalida("marco: obrigatorio")
    out["marco"] = _data("marco", e["marco"])
    if "marco_documentado" not in e:
        raise EntradaInvalida("marco_documentado: obrigatorio")
    out["marco_documentado"] = _bool("marco_documentado", e["marco_documentado"])
    out["acordo_afasta_recesso"] = _bool("acordo_afasta_recesso", e.get("acordo_afasta_recesso", False))
    # Calendario: ausencia (None) e diferente de lista vazia ([]). Ausente = formula aberta.
    out["dias_nao_uteis"] = None
    if "dias_nao_uteis" in e:
        if not isinstance(e["dias_nao_uteis"], list):
            raise EntradaInvalida("dias_nao_uteis: lista de datas")
        out["dias_nao_uteis"] = sorted({_data(f"dias_nao_uteis[{i}]", x) for i, x in enumerate(e["dias_nao_uteis"])})
    out["recesso"] = None
    if "recesso" in e:
        if not isinstance(e["recesso"], list):
            raise EntradaInvalida("recesso: lista de {inicio, fim}")
        rec = []
        for i, r in enumerate(e["recesso"]):
            if not isinstance(r, dict) or set(r) != {"inicio", "fim"}:
                raise EntradaInvalida(f"recesso[{i}]: esperado {{inicio, fim}}")
            a, b = _data(f"recesso[{i}].inicio", r["inicio"]), _data(f"recesso[{i}].fim", r["fim"])
            if b < a:
                raise EntradaInvalida(f"recesso[{i}]: fim antes do inicio")
            rec.append((a, b))
        out["recesso"] = rec
    out["calendario_conferido_ate"] = (_data("calendario_conferido_ate", e["calendario_conferido_ate"])
                                       if "calendario_conferido_ate" in e else None)
    return out


def eco(e):
    r = {}
    for k, v in e.items():
        if isinstance(v, dt.date):
            r[k] = v.isoformat()
        elif k == "dias_nao_uteis" and v is not None:
            r[k] = [d.isoformat() for d in v]
        elif k == "recesso" and v is not None:
            r[k] = [{"inicio": a.isoformat(), "fim": b.isoformat()} for a, b in v]
        else:
            r[k] = v
    return r


def _fonte(arquivo, ln):
    return f"{arquivo} {ln}" if ln else arquivo


def formula(regime, prazo, motivo, falta):
    if regime is None:
        contagem = "sem regra de contagem no plugin para este caso"
    else:
        contagem = (f"dia 1 = {regime['inicio']} ({_fonte(regime['fonte'], regime['inicio_ln'])}); "
                    f"{'contagem continua' if prazo['unidade'] == 'continuos' else 'so dias uteis'}; "
                    f"{'recesso suspende' if regime['recesso_suspende'] else 'recesso nao suspende'} "
                    f"({_fonte(regime['fonte'], regime['recesso_ln'])}); {regime['prorrogacao']} "
                    f"({_fonte(regime['fonte'], regime['prorrogacao_ln'])})")
    qtd = f"{prazo['dias']} dias" if prazo.get("dias") else f"{prazo.get('meses')} meses"
    return {
        "motivo": motivo,
        "formula": (f"vencimento = marco ({prazo['evento']}) + {qtd}, "
                    f"pela regra: {contagem}"),
        "passos_para_o_advogado": [
            "1. confirmar o marco com o documento que o constitui ou comprova",
            "2. listar os dias sem expediente e o recesso da camara no periodo (calendario oficial e feriados da sede)",
            "3. achar o dia 1 e contar dia a dia pela regra acima",
            "4. se o ultimo dia nao tiver expediente, prorrogar ao primeiro dia util seguinte",
        ],
        "falta": falta,
    }


class Calendario:
    def __init__(self, nao_uteis, recesso, suspende, recesso_sem_expediente=True):
        self.nao_uteis = set(nao_uteis)
        self.recesso = recesso
        self.suspende = suspende
        self.recesso_sem_expediente = recesso_sem_expediente

    def em_recesso(self, d):
        return any(a <= d <= b for a, b in self.recesso)

    def sem_expediente(self, d):
        """Dia nao util: fim de semana (premissa), data informada ou recesso da camara."""
        if d.weekday() >= 5:
            return "sabado/domingo (premissa)"
        if d in self.nao_uteis:
            return "dia sem expediente informado"
        if self.recesso_sem_expediente and self.em_recesso(d):
            return "recesso da camara informado"
        return None


def contar(regime, prazo, e):
    afastado = e["regime"] == "cam-ccbc-2025" and e["acordo_afasta_recesso"]
    suspende = regime["recesso_suspende"] and not afastado
    # CAM-CCBC 3.4.1: com sede definida, so prorroga dia nao util no local da sede. Com o recesso
    # afastado por acordo, o dia de recesso so conta como sem expediente se vier em dias_nao_uteis.
    cal = Calendario(e["dias_nao_uteis"], e["recesso"], suspende, recesso_sem_expediente=not afastado)
    memoria = []
    limite = e["calendario_conferido_ate"]
    d = e["marco"] + UM_DIA
    # Dia 1: primeiro dia util depois do marco (fora do recesso).
    while True:
        if d > limite:
            raise ForaDoCalendario(d)
        motivo = cal.sem_expediente(d)
        if motivo is None:
            break
        memoria.append({"data": d.isoformat(), "dia": DIAS_SEMANA[d.weekday()], "situacao": f"inicio adiado: {motivo}"})
        d += UM_DIA
    inicio, n = d, 0
    uteis = prazo["unidade"] == "uteis"
    while True:
        if d > limite:
            raise ForaDoCalendario(d)
        if suspende and cal.em_recesso(d):
            memoria.append({"data": d.isoformat(), "dia": DIAS_SEMANA[d.weekday()], "situacao": "suspenso: recesso"})
        elif uteis and cal.sem_expediente(d):
            memoria.append({"data": d.isoformat(), "dia": DIAS_SEMANA[d.weekday()],
                            "situacao": f"nao conta (prazo em dias uteis): {cal.sem_expediente(d)}"})
        else:
            n += 1
            memoria.append({"data": d.isoformat(), "dia": DIAS_SEMANA[d.weekday()], "situacao": f"dia {n}"})
            if n == prazo["dias"]:
                break
        d += UM_DIA
    nominal = d
    venc = d
    while cal.sem_expediente(venc):
        if venc > limite:
            raise ForaDoCalendario(venc)
        motivo = cal.sem_expediente(venc)
        if venc != nominal:
            memoria.append({"data": venc.isoformat(), "dia": DIAS_SEMANA[venc.weekday()],
                            "situacao": f"prorrogacao: {motivo}"})
        else:
            memoria[-1]["situacao"] += f" - sem expediente ({motivo}): prorroga"
        venc += UM_DIA
    if venc != nominal:
        memoria.append({"data": venc.isoformat(), "dia": DIAS_SEMANA[venc.weekday()],
                        "situacao": "vencimento prorrogado (primeiro dia util)"})
    return inicio, nominal, venc, memoria, suspende


def calcular(e, dados):
    prazo = e["prazo"]
    regime = dados["regimes"].get(e["regime"])
    avisos = [AVISO_FIXO, PREMISSA_FDS]
    if prazo.get("observacao"):
        avisos.append(prazo["observacao"])
    if e["regime"] == "cam-ccbc-2025" and e["acordo_afasta_recesso"]:
        avisos.append("recesso afastado por acordo: dia de recesso so prorroga o vencimento se for dia sem expediente "
                      "no local da sede (ou, sem sede definida, no CAM-CCBC) e vier em dias_nao_uteis "
                      f"({regime['fonte']} L188, L190)")
    fonte_prazo = _fonte(prazo["fonte"], prazo["ln"])
    base = {"regime": e["regime"],
            "prazo": {"id": prazo["id"], "dias": prazo.get("dias"), "meses": prazo.get("meses"),
                      "unidade": prazo["unidade"], "evento": prazo["evento"], "fonte": fonte_prazo},
            "regras": [], "resultado": None, "memoria": [], "avisos": avisos, "formula_aberta": None}
    if regime is not None:
        base["regras"] = [
            {"regra": f"marco: {regime['marco']}", "fonte": _fonte(regime["fonte"], regime["marco_ln"])},
            {"regra": f"dia 1: {regime['inicio']}", "fonte": _fonte(regime["fonte"], regime["inicio_ln"])},
            {"regra": "prazo continuo" if regime["continuo"] else "prazo nao continuo",
             "fonte": _fonte(regime["fonte"], regime["continuo_ln"])},
            {"regra": f"prorrogacao: {regime['prorrogacao']}", "fonte": _fonte(regime["fonte"], regime["prorrogacao_ln"])},
            {"regra": f"recesso: {'suspende' if regime['recesso_suspende'] else 'nao suspende'} - {regime['recesso_ressalva']}",
             "fonte": _fonte(regime["fonte"], regime["recesso_ln"])},
        ]
    if e["regime"] == "sem-regulamento":
        base["formula_aberta"] = formula(None, prazo, (
            "sem regulamento de camara nao ha regra de contagem no plugin: a Lei 9.307 fixa prazos mas nao a forma "
            "de contar, e o CPC nao entra por padrao"), ["regra de contagem na convencao, no Termo ou em ordem"])
        return EXIT_FORMULA, base
    if prazo["unidade"] == "fora-do-regulamento":
        base["formula_aberta"] = formula(regime, prazo, (
            f"prazo de {fonte_prazo} corre fora do procedimento regido pelo regulamento: {prazo['observacao']}"),
            ["regra de contagem com fonte no context (nao incorporada nesta versao) [VERIFICAR]"])
        return EXIT_FORMULA, base
    if e["regime"] not in prazo["regimes"]:
        raise EntradaInvalida(f"prazo_id '{prazo['id']}' nao pertence ao regime '{e['regime']}'")
    falta = []
    if not e["marco_documentado"]:
        falta.append("documento que constitui ou comprova o marco (relato, e-mail ou mensagem do cliente nao bastam)")
    if e["dias_nao_uteis"] is None:
        falta.append("dias sem expediente no periodo (feriados no local da sede e dias sem expediente da camara), "
                     "ou [] se nao houver")
    if e["recesso"] is None:
        falta.append("recesso da camara no periodo, pelo calendario oficial, ou [] se nao houver")
    if e["calendario_conferido_ate"] is None:
        falta.append("calendario_conferido_ate: ate que data o calendario informado foi conferido")
    if falta:
        base["formula_aberta"] = formula(regime, prazo, "faltam dados: o script nao presume calendario nem marco", falta)
        return EXIT_FORMULA, base
    try:
        inicio, nominal, venc, memoria, suspende = contar(regime, prazo, e)
    except ForaDoCalendario as exc:
        base["formula_aberta"] = formula(regime, prazo, (
            f"a contagem passa de {e['calendario_conferido_ate'].isoformat()}, ultima data do calendario informado"),
            [f"calendario conferido alem de {exc.args[0].isoformat()} (dias sem expediente e recesso)"])
        return EXIT_FORMULA, base
    if venc > e["calendario_conferido_ate"]:
        base["formula_aberta"] = formula(regime, prazo, (
            f"o vencimento cai depois de {e['calendario_conferido_ate'].isoformat()}, ultima data do calendario informado"),
            [f"calendario conferido ate pelo menos {venc.isoformat()}"])
        return EXIT_FORMULA, base
    base["memoria"] = memoria
    base["resultado"] = {
        "inicio_contagem": inicio.isoformat(),
        "vencimento_nominal": nominal.isoformat(),
        "vencimento": venc.isoformat(),
        "dia_da_semana": DIAS_SEMANA[venc.weekday()],
        "prorrogado": venc != nominal,
        "recesso_suspendeu": suspende and any(m["situacao"].startswith("suspenso") for m in memoria),
        "regra": (f"{prazo['dias']} dias {'continuos' if prazo['unidade'] == 'continuos' else 'uteis'} "
                  f"a partir do dia 1 ({inicio.isoformat()}), pela regra de {e['regime']}"),
        "fonte": f"prazo: {fonte_prazo}; contagem: {_fonte(regime['fonte'], regime['inicio_ln'])}, "
                 f"{_fonte(regime['fonte'], regime['prorrogacao_ln'])}, {_fonte(regime['fonte'], regime['recesso_ln'])}; "
                 f"captura {dados['data_captura']}",
    }
    return EXIT_OK, base


def build_parser():
    p = argparse.ArgumentParser(
        prog="calc_arbitragem_prazo.py",
        description="Data-limite de prazo arbitral pela regra do regulamento (CAM-CCBC 2025, CAMARB 2019, "
                    "CAM B3 2026). Entrada JSON por --entrada ou stdin.")
    p.add_argument("--entrada", help="arquivo JSON de entrada (sem ele, le o stdin)")
    p.add_argument("--versao", action="store_true", help="imprime a versao e sai")
    return p


def main(argv=None):
    args = build_parser().parse_args(argv)
    if args.versao:
        print(json.dumps({"script": "calc_arbitragem_prazo.py", "versao": VERSAO}))
        return EXIT_OK
    try:
        with open(DADOS, encoding="utf-8") as f:
            dados = json.load(f)
        bruto = (open(args.entrada, encoding="utf-8").read() if args.entrada else sys.stdin.read())
        try:
            e = json.loads(bruto)
        except json.JSONDecodeError as exc:
            raise EntradaInvalida(f"JSON invalido: {exc.msg} (linha {exc.lineno})")
        e = ler_entrada(e, dados)
        codigo, corpo = calcular(e, dados)
    except EntradaInvalida as exc:
        print(json.dumps({"erro": str(exc), "versao": VERSAO}, ensure_ascii=False))
        return EXIT_ENTRADA
    except Exception as exc:  # nunca traceback com exit 1
        print(json.dumps({"erro": f"falha inesperada: {type(exc).__name__}: {exc}", "versao": VERSAO},
                         ensure_ascii=False))
        return EXIT_ENTRADA
    saida = {"script": "calc_arbitragem_prazo.py", "versao": VERSAO, "parametros_usados": eco(e)}
    saida.update(corpo)
    print(json.dumps(saida, ensure_ascii=False, indent=1))
    return codigo


if __name__ == "__main__":
    sys.exit(main())
