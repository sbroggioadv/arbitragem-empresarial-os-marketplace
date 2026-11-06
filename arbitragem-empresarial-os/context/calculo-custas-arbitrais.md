# Cálculo de custas arbitrais — script e conta aberta

> Valor de custas sai por um de dois caminhos, e só por eles: o script `scripts/calc_arbitragem_custas.py` (exit 0) ou a **conta aberta** abaixo, com a linha da tabela transcrita, a fórmula, as duas contas e o aviso de que **o número não foi conferido por script**.

## O que vale

- **Só a tabela capturada.** CAM-CCBC 2025: `context/packs/cam-ccbc-2025/custas.md` (Tabelas 1 a 7, valores fixos). CAMARB 2019: só os valores fixos do árbitro de emergência da RA 06/20 (`context/packs/camarb-2019/arbitro-emergencia-ra-06-20.md` L127 «9.1.  A parte requerente deverá depositar»); a tabela geral da CAMARB e a da CAM B3 ficam `PENDENTE DE FONTE`.
- **Valor da causa** = soma dos pedidos das partes (`context/packs/cam-ccbc-2025/custas.md` L206 «14. O valor da causa»).
- **Fórmula da linha:** parcela fixa da faixa + percentual da faixa × (valor da causa − valor indicado em "do valor superior a" da faixa); na primeira faixa, só a parcela fixa.
- **Valor exatamente R$ 3.000.000,00:** o regramento exige valor «inferior a» para o expedito (L348 «54. As custas dos procedimentos expeditos») e o regulamento usa «não exceda» (`context/packs/cam-ccbc-2025/regulamento.md` L534 «36.1 O Procedimento Expedito»). O script devolve as duas contas, sem escolher (exit 3), e manda confirmar com a Secretaria do CAM-CCBC.
- **Fora da conta:** fundo de despesas, honorários periciais, tributos e atualização por IPCA (L564 «(c) A atualização será realizada»).

## Como rodar

O script fica na raiz do plugin. A partir da pasta base da skill: `<pasta-base>/../../scripts/calc_arbitragem_custas.py`. Se não existir, buscar pelo nome único:

```bash
N='calc_arbitragem_custas.py'
S=$(find "$HOME" -name "$N" -path '*/scripts/*' 2>/dev/null)
[ -z "$S" ] && S=$(find / -name "$N" -path '*/scripts/*' 2>/dev/null)
for f in $S; do python3 "$f" --versao; done
```

Usar o que responder `"versao": "0.1.0"`. Exit 0 = calculado (mostrar cada rubrica com `regra`, `fonte` e `segunda_conta`); 2 = entrada inválida; 3 = fórmula aberta (mostrar o que foi calculado, a `formula_aberta` e o que falta). Sem Python, sem o arquivo ou outro código: conta aberta abaixo.

Script: `calc_arbitragem_custas.py`
```flags
--entrada   arquivo   opcional   JSON; sem ele, le o stdin
--versao    flag      opcional   imprime a versao
```
```campos
camara   enum   obrigatorio   cam-ccbc-2025|camarb-2019|cam-b3-2026|outra
valor_causa   decimal   condicional   cam-ccbc-2025 sem pedidos; soma dos pedidos (L206)
pedidos   lista   condicional   alternativa a valor_causa; um decimal por pedido
arbitros   enum   opcional   unico|tres|indefinido
procedimento   enum   opcional   comum|expedito|indefinido
polo   enum   opcional   requerente|requerida|indefinido
incidentes   lista   opcional   esclarecimentos|impugnacao|emergencia
arbitros_impugnados   inteiro   opcional   com impugnacao; padrao 1
```

## Conta aberta (sem script)

**Aviso fixo: conta feita à mão, não conferida por script.**

1. Valor da causa: a soma, mostrada.
2. Procedimento e tabela: comum (Tabelas 1 a 3) ou expedito (Tabelas 5 a 7), com o limite do item 54.
3. Para cada rubrica: a linha transcrita com o `Ln`, a fórmula e a conta 1.
4. Conta 2 por caminho independente: selecionar de novo a faixa comparando o valor com os limites da linha de cima e da de baixo; refazer a aritmética separada (excedente, produto, soma). Diferença além de centavos ⇒ número bloqueado.
5. Rateio de cada polo (50%) e prazo de recolhimento, com o `Ln`.

| Rubrica | Linha (Ln) | Fórmula | Conta 1 | Conta 2 | Valor |
|---|---|---|---|---|---|

**Caso de referência resolvido à mão (fictício, valores de exemplo (ex.)).** CAM-CCBC 2025, procedimento comum, valor da causa R$ 4.500.000,00. Faixa de 4.000.001 a 10.000.000 nas três tabelas (4.500.000 ≥ 4.000.001 e ≤ 10.000.000; < 10.000.001). Excedente: 4.500.000 − 4.000.001 = 499.999.
- Taxa de administração (L236): 144.900 + 0,28987736746185% × 499.999 = 144.900 + 1.449,38 = **R$ 146.349,38**.
- Árbitro único (L277): 173.900 + 1,56533790881473% × 499.999 = 173.900 + 7.826,67 = **R$ 181.726,67**.
- Tribunal de três (L258): 434.800 + 3,91334477203683% × 499.999 = 434.800 + 19.566,68 = **R$ 454.366,68** (presidente 40%, coárbitros 30% cada, L251).
- Taxa de registro (L220): R$ 5.500,00, pela requerente, antes do requerimento.
