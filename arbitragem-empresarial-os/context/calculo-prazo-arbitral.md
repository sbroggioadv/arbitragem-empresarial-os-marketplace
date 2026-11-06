# Cálculo de prazo arbitral — script e conta aberta

> Data-limite de prazo no procedimento arbitral sai por um de dois caminhos, e só por eles: o script `scripts/calc_arbitragem_prazo.py` (exit 0) ou a **conta aberta** abaixo, passo a passo, com o aviso de que **o número não foi conferido por script**. A conta aberta não é plano B: é a que o advogado confere à mão.

## O que vale

- **Fonte do prazo:** lei, convenção, regulamento + versão, Termo ou ordem, com o `Ln` ou o documento. A Lei 9.307 fixa prazos (ex.: esclarecimentos, `context/lei-9307-1996.md` L562 «Art. 30. No prazo de 5 (cinco)») mas não diz como contar.
- **Regra de contagem:** a do regulamento escolhido pelas partes; nunca a do CPC por padrão.

| Regulamento | Dia 1 | Curso | Vencimento sem expediente | Recesso | Fonte |
|---|---|---|---|---|---|
| CAM-CCBC 2025 | 1º dia útil seguinte ao recebimento (data do comprovante de envio ou entrega) | contínuo | prorroga ao 1º dia útil, pelo local da sede | suspende, salvo acordo | `context/packs/cam-ccbc-2025/regulamento.md` L187 «3.4 Os prazos serão contínuos»; L188 «3.4.1 Considera-se prorrogado»; L190 «3.5.1 Salvo acordo em contrário» |
| CAMARB 2019 | dia útil subsequente à entrega da correspondência | contínuo, sem suspensão | prorroga se cair em feriado no local ou dia sem expediente | não suspende; só adia o início e prorroga o fim | `context/packs/camarb-2019/regulamento.md` L45 «2.5   Os prazos regimentais» |
| CAM B3 2026 | 1º dia útil seguinte à comunicação (envio, postagem ou recebimento) | contínuo | prorroga; dia útil = expediente na CAM | suspende | `context/packs/cam-b3-2026/regulamento.md` L65 «5.1 Os prazos serão contados»; L69 «5.2.1 Consideram-se dias úteis»; L71 «5.2.2 Todos os prazos ficarão suspensos» |

- **Calendário é entrada, nunca presunção.** Feriado no local da sede, dia sem expediente da câmara e recesso vêm do calendário oficial da câmara ou de documento. Lista vazia só quando o advogado conferiu que não há nenhum no período. Sábado e domingo são tratados como dias sem expediente (premissa declarada na saída).
- **Marco só com documento** que constitui ou comprova o evento (comunicação com data de envio ou entrega, comprovante, ata, ordem, Termo). Relato não basta: sem documento, ⚪ e fórmula, sem data.
- **Prazos fora do regulamento** saem como fórmula, sem data: instituição da arbitragem depois da medida judicial (`context/lei-9307-1996.md` L433 «Parágrafo único. Cessa a eficácia»), sentença em seis meses (L487 «Art. 23. A sentença arbitral será proferida») e ação de nulidade em 90 dias (L636 «§ 1o A demanda»). A regra de contagem deles não está no `context/` desta versão.

## Como rodar

O script fica na raiz do plugin. A partir da pasta base da skill: `<pasta-base>/../../scripts/calc_arbitragem_prazo.py`. Se não existir, buscar pelo nome único:

```bash
N='calc_arbitragem_prazo.py'
S=$(find "$HOME" -name "$N" -path '*/scripts/*' 2>/dev/null)
[ -z "$S" ] && S=$(find / -name "$N" -path '*/scripts/*' 2>/dev/null)
for f in $S; do python3 "$f" --versao; done
```

Usar o que responder `"versao": "0.1.0"`. Entrada em JSON por `--entrada` ou stdin. Exit 0 = data calculada (mostrar `resultado`, `regras` e `memoria`); 2 = entrada inválida (corrigir o dado); 3 = fórmula aberta (mostrar `formula_aberta` e o que falta, sem data). Sem Python, sem o arquivo ou outro código: conta aberta abaixo.

Script: `calc_arbitragem_prazo.py`
```flags
--entrada   arquivo   opcional   JSON; sem ele, le o stdin
--versao    flag      opcional   imprime a versao
```
```campos
regime   enum   obrigatorio   cam-ccbc-2025|camarb-2019|cam-b3-2026|sem-regulamento
prazo_id   enum   condicional   sem prazo_dias; id do catalogo em scripts/data/contagem-prazos-arbitrais.json
prazo_dias   inteiro   condicional   sem prazo_id; prazo do Termo, de ordem ou da convencao
prazo_fonte   texto   condicional   com prazo_dias; documento e trecho
unidade   enum   opcional   continuos|uteis
marco   data   obrigatorio   AAAA-MM-DD; evento que o regulamento manda contar
marco_documentado   bool   obrigatorio   true so com documento do evento
dias_nao_uteis   lista   obrigatorio   datas sem expediente no periodo; [] = nenhum
recesso   lista   obrigatorio   {inicio, fim} do recesso da camara; [] = nenhum
calendario_conferido_ate   data   obrigatorio   ultima data coberta pelo calendario informado
acordo_afasta_recesso   bool   opcional   cam-ccbc-2025; padrao false
```

Catálogo (`prazo_id`): `ccbc-resposta`, `ccbc-coarbitros`, `ccbc-termo`, `ccbc-alegacoes-iniciais`, `ccbc-respostas-alegacoes`, `ccbc-sentenca`, `ccbc-esclarecimentos`, `ccbc-manifestacao-esclarecimentos`, `ccbc-supletivo`, `camarb-resposta`, `camarb-supletivo`, `b3-resposta`, `b3-supletivo`, `b3-impugnacao-arbitro-emergencia`, `lei-art30-esclarecimentos`, `lei-art22a-instituicao`, `lei-art23-sentenca`, `lei-art33-anulatoria`. Prazo do Termo ou de ordem: `prazo_dias` + `prazo_fonte`.

## Conta aberta (sem script)

**Aviso fixo: conta feita à mão, não conferida por script.**

1. Marco: data e documento (o evento que o regulamento manda contar).
2. Dias sem expediente e recesso no período, com a fonte (calendário oficial da câmara, feriados da sede).
3. Dia 1: o primeiro dia útil depois do marco (fora do recesso, quando o recesso suspende).
4. Contar dia a dia; no recesso que suspende, o dia não conta.
5. Último dia sem expediente: prorrogar ao primeiro dia útil.

| Data | Dia | Situação (dia N, suspenso, sem expediente, prorrogação) | Fonte |
|---|---|---|---|

**Caso de referência resolvido à mão (fictício).** CAM-CCBC 2025, resposta em 15 dias (`context/packs/cam-ccbc-2025/regulamento.md` L243 «8.1 A secretaria do CAM-CCBC notificará»); notificação recebida em 22/09/2026 (terça), com comprovante; calendário conferido até 31/12/2026 sem feriado nem recesso no período. Dia 1 = 23/09 (quarta); dia 15 = 07/10/2026 (quarta), dia útil: **vencimento em 07/10/2026**. Com recesso de 20/12/2026 a 06/01/2027 e notificação em 10/12/2026: dias 1 a 9 de 11/12 a 19/12, suspenso de 20/12 a 06/01, dias 10 a 15 de 07/01 a 12/01: **vencimento em 12/01/2027**. Na CAMARB 2019, prazo de 10 dias com o mesmo marco e o mesmo recesso: o dia 10 cai em 20/12 (domingo e recesso), sem suspensão: **prorroga a 07/01/2027**.
