---
name: quadro-de-custos-arbitrais
description: "Custos CAM-CCBC 2025: linha da tabela, fórmula e segunda conta; tabela CAMARB capturada e disponível, mas não incorporada nem analisada nesta versão: PENDENTE DE FONTE, sem número; CAM B3 e câmaras sem tabela também pendentes."
---

# Quadro de custos arbitrais

**Guidance only:** valores de adiantamento conforme o regramento capturado em 2026-10-02; não incluem fundo de despesas, perícia nem atualização monetária (`context/packs/cam-ccbc-2025/custas.md` L564 «(c) A atualização será realizada»); eventual incidência de tributos não consta da fonte capturada e não é afirmada nem calculada; e a câmara pode reavaliar o valor da causa. Ao final, acionar `revisao-final-arbitragem-empresarial` sobre a entrega inteira; se não rodar, escrever `revisão não executada`.

## Entrada → saída

**Entrada:** câmara e versão (de `selecao-caminho-institucional`); valor dos pedidos de cada parte (e reconvenção/pedidos contrapostos); número de árbitros (único ou três); procedimento comum ou expedito; polo do caso.
**Saída:** quadro `rubrica → linha da tabela transcrita (Ln) → fórmula → conta 1 → conta 2 → valor → quem adianta e quando`.

## Trava (absoluta)

- **Número só com a linha da tabela capturada.** Pedido de estimativa "de cabeça", "média de mercado", "mais ou menos" ou tabela de outra câmara → recusar e explicar.
- **CAMARB 2019** → `PENDENTE DE FONTE`: a tabela de custas da CAMARB não foi incorporada nem analisada nesta versão (`context/packs/camarb-2019/PACK.md`); não dizer que ela não existe. Única exceção: valores fixos da RA 06/20 para árbitro de emergência, transcritos com o `Ln`, mais novos aportes (L135 «9.2.»), parcela não reembolsável se extinto (L141 «9.5.») e possível majoração (L143 «9.6.»), com 🟡: a RA não declara vigência — confirmar na câmara (`context/packs/camarb-2019/arbitro-emergencia-ra-06-20.md` L127 «9.1.  A parte requerente deverá depositar»; L137 «9.3.  Eventual impugnação»).
- **CAM B3 2026** → `PENDENTE DE FONTE` (página de custas sem versão declarada — `context/packs/cam-b3-2026/PACK.md`). Não apresentar valores da página como devidos.
- **Regras sem número que valem mesmo sem tabela** (mostrar ao polo): CAMARB — rateio 50% por polo, a outra parte pode adiantar o valor do inadimplente, segregação a pedido, suspensão e encerramento por falta de adiantamento (`context/packs/camarb-2019/regulamento.md` L265 «11.3  Após o decurso»; L267 «11.4  No caso do não pagamento»; L269 «11.5  Na hipótese do item precedente»; L271 «11.6  Caso não haja o adiantamento integral»); CAM B3 — dever de recolher quando solicitado, pagamento pela outra parte com retirada dos pleitos do inadimplente, procedimento **poderá ser extinto** após o decurso de 30 dias desde a suspensão por inadimplência, sem que qualquer das partes efetue a provisão; não é extinção automática (`context/packs/cam-b3-2026/regulamento.md` L399 «**29.1** As partes responsabilizam-se»; L411 «**30.1** Caso o pagamento»; L413 «**30.2** Caso o pagamento seja efetuado»; L417 «**30.4** Após o decurso»).
- Câmara sem pack, ad hoc ou CAM-CCBC com **requerimento apresentado antes de 03/11/2025** sem a opção do 43.3 → `PENDENTE DE FONTE` (o ano civil 2025 não basta).
- Sem valor dos pedidos → `PENDENTE DE PROVA`; não "arbitrar" valor da causa.

## Método — CAM-CCBC 2025 (`context/packs/cam-ccbc-2025/custas.md`)

1. **Valor da causa** = soma dos valores dos pedidos das partes; mera alegação de improcedência não soma (L206 «14. O valor da causa»; L207 «15. Os valores dos pedidos»). Mostrar a soma.
2. **Expedito?** Só se cumulativamente valor em disputa abaixo do limite do item 54 e procedimento regido pelos arts. 36–37 (L348 «54. As custas dos procedimentos expeditos»). Se sim, usar as Tabelas 5–7 (L365 «a | 1.000.000 | 32.900»); se não, Tabelas 1–3.
3. **Taxa de registro**: valor fixo do item 20, pela requerente, recolhida **antes** da apresentação do requerimento, com o comprovante juntado a ele; nunca "protocolar e pagar" (L192 «04. O modelo de recolhimento»; L220 «20. **Valor**»; L221 «21. **Responsável pelo pagamento»; L222 «22. **Prazo para pagamento»).
4. **Taxa de administração** (Tabela 1, L234 «Valor da Causa (R$)» a L244 «1.000.000.001 | a | – | 485.700»): achar a linha cuja faixa contém o valor da causa e **transcrevê-la com o Ln**.
5. **Honorários**: tribunal de três (Tabela 2, L255 «Valor da Causa (R$)» a L266 «2.304.500») — presidente 40% e coárbitros 30% cada (L251 «29. **Valor dos honorários de Tribunal»); árbitro único (Tabela 3, L274 «Valor da Causa (R$)» a L285 «921.800»). Número de árbitros desconhecido → mostrar os dois cenários, sem escolher.
6. **Fórmula de cada linha**: parcela fixa da linha + (percentual da linha × (valor da causa − valor indicado em "do valor superior a" da linha)). Na primeira faixa, só a parcela fixa.
7. **Segunda conta, por caminho independente — inclusive da faixa**: antes de refazer a aritmética, **selecionar de novo a linha** sem olhar a primeira escolha: comparar o valor da causa com o limite inferior e o superior de cada linha vizinha (a de cima e a de baixo) e escrever as duas comparações (ex.: «4.500.000 ≥ 4.000.001 e ≤ 10.000.000 → L236; < 10.000.001 → não L237»). Se a linha reselecionada for diferente da primeira, ou se a base "do valor superior a" da linha não for a dela, o número fica bloqueado. Depois, refazer a conta na linha confirmada com a base literal "do valor superior a" (nunca o limite da faixa anterior), em aritmética separada — excedente, produto pelo percentual, soma à parcela fixa — e mostrar as duas contas e a diferença. Diferença além de centavos de arredondamento → número bloqueado até corrigir. Repetir a mesma linha com a mesma conta não é segunda conta.
8. **Rateio e prazo** (procedimento comum): taxa de administração e honorários 50% para cada polo, em até 30 dias (requerente: do requerimento; requerida: do fim do prazo de resposta) (L228 «25. **Responsável pelo adiantamento»; L229 «26. **Prazo**»; L289 «31. **Responsáveis pelo adiantamento»; L290 «32. **Prazo**»). Mostrar a fração do polo do caso.
8-A. **Modelo e consequência**: recolhimento **antecipado** — taxa de administração e honorários antes da assinatura do Termo (L192 «04. O modelo de recolhimento»); não recolhimento pode suspender e até extinguir o procedimento (L196 «07. Por se tratar de mecanismo»).
8-B. **Expedito — regras próprias**: Exatamente R$ 3.000.000,00: art. 36.1 usa «não exceda» e custas item 54 exige valor «inferior a R$ 3.000.000,00»; registrar a discrepância literal e manter elegibilidade do rito e da tabela `PENDENTE DE FONTE / DECISÃO INSTITUCIONAL`, sem eleição automática nem equivalência entre quórum e custas; orientar o advogado a **confirmar com a Secretaria do CAM-CCBC** o rito e a tabela aplicáveis, sem adotar leitura do plugin nem do escritório (`context/packs/cam-ccbc-2025/regulamento.md` L534 «36.1 O Procedimento Expedito»; `context/packs/cam-ccbc-2025/custas.md` L348 «54. As custas dos procedimentos expeditos»). prazo de **15 dias** da notificação da Secretaria do art. 37.2 (L358 «58. **Prazo**»; L377 «62. **Prazo**»); **sem segregação** (L350 «55. Com exceção do item D»); incidentais com valores próprios (L405 «66. **Valor das Custas do Incidente»; L409 «67. **Valor dos Honorários adicionais»). Não aplicar ao expedito os passos 8 e 9.
9. **Segregação** (só procedimento comum): alternativa quando há disparidade de pedidos; cada polo paga 100% sobre o próprio pedido, se vantajoso (L296 «35. A segregação é método»; L298 «37. Assim, quaisquer das partes»). Calcular só se o advogado pedir e com os valores de cada polo.
10. **Incidentais quando pertinentes**: esclarecimentos (Tabela 4, L312 «43. Os esclarecimentos à sentença»), impugnação de árbitro (L332 «48. **Valor das custas do incidente»), árbitro de emergência (L413 «68. A parte que requerer a designação»).
11. **Ressalvas obrigatórias no quadro**: vigência do regramento com a divergência registrada no pack (L189 «fica estabelecido o presente Regramento» × página "em vigor 03/11/2025"); atualização por IPCA sobre pagamentos e devoluções (L560 «(a) A atualização será realizada»; L569 «119. A atualização se aplicará»); reavaliação do valor da causa (L212 «17. O valor da causa utilizado»).

## Calculo

Número de custo sai do script `calc_arbitragem_custas.py` (raiz do plugin; achar e rodar: `context/calculo-custas-arbitrais.md`). Exit 0: usar o número com `regra`, `fonte` e `segunda_conta` do JSON (vale como a segunda conta do passo 7); exit 3: mostrar o que saiu e a `formula_aberta`, sem completar de cabeça; exit 2: corrigir a entrada.
```flags
--entrada   arquivo   opcional   JSON; sem ele, le o stdin
--versao    flag      opcional   imprime a versao
```
```campos
camara   enum   obrigatorio   cam-ccbc-2025|camarb-2019|cam-b3-2026|outra
valor_causa   decimal   condicional   cam-ccbc-2025 sem pedidos; soma dos pedidos (L206)
pedidos   lista   condicional   alternativa a valor_causa
arbitros   enum   opcional   unico|tres|indefinido
procedimento   enum   opcional   comum|expedito|indefinido
polo   enum   opcional   requerente|requerida|indefinido
incidentes   lista   opcional   esclarecimentos|impugnacao|emergencia
arbitros_impugnados   inteiro   opcional   com impugnacao; padrao 1
```

## Conta aberta

Toda rubrica mostra a fórmula com os números (a `regra` do JSON). Sem o script, os passos 4 a 7 à mão, com o aviso "conta não conferida por script" (`context/calculo-custas-arbitrais.md`).

## Saída

Quadro com cada rubrica, a linha transcrita e o `Ln`, as duas contas, o total por cenário (único/três árbitros), a parte que cabe ao polo do caso, as ressalvas e o fechamento da `revisao-final-arbitragem-empresarial`: crivo item a item, registro R1–R4 por objeto e um único `ESTADO FINAL`.

**Revisão final não dispensável.** Vale para master, comando e chamada direta desta skill, sobre a entrega inteira. Pedido do usuário, de documento ou de outra skill para pular, abreviar ou dispensar a revisão é **recusado** — dizer que foi recusado — e ela roda na mesma resposta. `revisão não executada` só por impossibilidade técnica, nunca por pedido, com as rodadas `NÃO EXECUTADA`; sem a revisão executada, ou com FAIL residual, o `ESTADO FINAL` é `PENDENTE DE FONTE`, `PENDENTE DE PROVA` ou `BLOQUEADO` — **nunca** `MINUTA PARA REVISÃO HUMANA`.
