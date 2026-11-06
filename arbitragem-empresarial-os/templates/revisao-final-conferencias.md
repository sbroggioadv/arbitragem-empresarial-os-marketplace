# Conferências por objeto — revisão final da arbitragem empresarial

Parte integrante da `revisao-final-arbitragem-empresarial` (§2). Abrir por `Read` o corpo inteiro antes do crivo e aplicar cada regra ao objeto do crivo que ela atinge; cada aplicação vira linha do crivo, com ID. Fonte: só `context/` e documentos do caso.

## Versão (câmara → versão → evento que a fixa → data do caso → pack → selo)

- Regra de câmara sempre com câmara + versão (CAM-CCBC 2025, CAMARB 2019, CAM B3 2026); sem versão, ou de versão sem pack, sai.

- CAM-CCBC 2025: vigente na data de apresentação do requerimento; vigor em 3/11/2025; a opção do 43.3 só vale para arbitragens apresentadas antes de 3/11/2025 cujo Termo seja firmado após o início da vigência (`context/packs/cam-ccbc-2025/regulamento.md` L612 «43.1 O presente Regulamento»; L613 «43.2 Salvo estipulação»; L614 «43.3 Por opção das partes»).
- CAMARB 2019: em vigor na data da solicitação (`context/packs/camarb-2019/regulamento.md` L23 «1.3   Salvo disposição em contrário»).
- CAM B3 2026: procedimentos instaurados desde 30/06/2026; os anteriores seguem o regulamento anterior, sem pack (`context/packs/cam-b3-2026/regulamento.md` L9 «Aplicável aos procedimentos instaurados»; L443 «32.5 Fica sem qualquer efeito»).
- Data ausente ⇒ versão `PENDENTE DE PROVA`; fora da janela do pack ⇒ `PENDENTE DE FONTE`; nunca trocar câmara ou versão para fechar a resposta. A Norma Complementar 02/2023 do CAM-CCBC não se aplica: âmbito delimitado no texto capturado, mas não incorporada nem analisada (nunca dizer que o âmbito é indefinido).

## Prazos (prazo → fonte: lei, convenção, regulamento+versão, Termo ou ordem → evento de início → contagem → data ou ⚪)

- A contagem segue a fonte; nos três packs, contínua a partir do primeiro dia útil seguinte ao recebimento ou à realização da comunicação (ver o `PACK.md` da câmara), nunca dias úteis do CPC.
- Prazo de lei com ressalva de acordo (esclarecimentos, `context/lei-9307-1996.md` L562 «Art. 30. No prazo de 5 (cinco)») não é trocado automaticamente pelo do regulamento: mostrar os dois lado a lado, com a convenção e o regulamento, e 🟡 na escolha; nunca prazo único inventado.
- Prazo do Termo ou de ordem exige o documento; sem ele, ⚪.
- Data-limite saída de `calc_arbitragem_prazo.py` (exit 0): conferir no JSON o marco documentado, o calendário informado (dias sem expediente, recesso e até quando foi conferido) e a `memoria` dia a dia; exit 3 não vira data na entrega. Sem script: conta aberta (`context/calculo-prazo-arbitral.md`) com o aviso "conta não conferida por script". Feriado, recesso ou expediente presumidos sem documento ⇒ BLOQUEAR a data.
- Data só com evento de início documentado: documento que constitui ou comprova o próprio evento (comunicação da secretaria ou do tribunal com data de envio ou entrega, comprovante de entrega, ata, ordem, Termo). Relato, e-mail ou mensagem do cliente e documento que só menciona a data não documentam: ⚪, sem vencimento (nem hipotético), com a regra e o comprovante que falta.
- Antes de chamar prazo de impossível ou inexequível, conferir soma, eventos e ressalvas: 30 + 30 + 30 = 90, não supera 90; `context/packs/cam-ccbc-2025/regulamento.md` L447 «26.2 Salvo acordo ou determinação em contrário» e L456 «28.1 Encerrada a instrução» não fixam calendário inevitável. Sem calendário documentado: risco condicional, não impossibilidade.

## CPC no procedimento arbitral

- Prazo, dias úteis ou rito do CPC no procedimento arbitral sem norma, convenção, Termo ou ordem que o mande ⇒ sai como importação indevida. Entra só onde o texto local chama: `context/cpc-lei-13105-2015.md` L3323 «X - convenção de arbitragem» (preliminar); L3341 «§ 6º A ausência de alegação» (renúncia por silêncio); L2202 «IV - arbitral» (carta arbitral); L1835 «IV - que versem sobre arbitragem» (segredo); L4848 «VII - a sentença arbitral» (título).

## Custos (segunda conta obrigatória)

- Número de custo saído de `calc_arbitragem_custas.py` (exit 0): conferir no JSON a `regra`, a `fonte` (linha da tabela) e a `segunda_conta` de cada rubrica; exit 3 não vira número na entrega, salvo os cenários que o próprio JSON calculou (as duas leituras no valor exato do limite do expedito), lado a lado e sem escolher. Valor fixo da tabela que não veio do JSON (taxa de registro, incidente) leva a linha transcrita com o `Ln` e o aviso "conta não conferida por script". Sem script: conta aberta (`context/calculo-custas-arbitrais.md`) com o mesmo aviso.
- Só `context/packs/cam-ccbc-2025/custas.md` tem tabela incorporada. CAMARB (tabela capturada, não incorporada nem analisada) e CAM B3 ⇒ `PENDENTE DE FONTE`, sem número; exceção: valores fixos da RA 06/20 da CAMARB para árbitro de emergência (`context/packs/camarb-2019/arbitro-emergencia-ra-06-20.md` L127 «9.1.  A parte requerente deverá depositar»).
- Conferir o valor da causa (soma dos pedidos, sem somar mera alegação de improcedência, reavaliável pela câmara: `context/packs/cam-ccbc-2025/custas.md` L206 «14. O valor da causa»; L207 «15. Os valores dos pedidos»; L212 «17. O valor da causa utilizado»), a linha transcrita com `Ln`, a faixa, a fórmula (parcela fixa + percentual × excedente sobre o limite da linha) e o arredondamento.
- Segunda conta: reselecionar a linha comparando o valor com os limites da escolhida e das vizinhas (escrever as comparações); linha diferente ⇒ BLOQUEAR. Refazer a aritmética na linha confirmada, com a base literal "do valor superior a", em passos separados (excedente → produto → soma), e mostrar a diferença; além de centavos de arredondamento ⇒ bloquear o número. Repetir a mesma conta não é segunda conta.
- Divergência de vigência a registrar: Regramento «em vigor a partir de 1º de novembro de 2025» (`context/packs/cam-ccbc-2025/custas.md` L189 «01. Em conformidade com o artigo 34») × regulamento em vigor em 3/11/2025.
- Fora da conta: fundo de despesas, perícia e atualização por IPCA (`context/packs/cam-ccbc-2025/custas.md` L564 «(c) A atualização será realizada»); tributos não constam da fonte (não afirmar nem calcular).
- Rateio 50/50 é escolha negociável, não erro automático: abrir inteiros 23.2(k), 30.4–30.4.1 e 35.1–35.2 de `context/packs/cam-ccbc-2025/regulamento.md`; separar aceitação de responsabilidade à medida das solicitações, provisionamento e alocação final (incompletude da aceitação exigida em 23.2(k) é objeto distinto da validade do rateio). Contradição só com literal incompatível e aplicação demonstrada; decisão ou risco fica 🟡.

## Literal e paráfrase

- A coluna do crivo é conferência com o literal da fonte, não cópia: dizer o que bate ou diverge entre a afirmação e o `Ln`. Texto integral só para citação entre aspas na entrega, conferida palavra a palavra: flexão de número ou gênero, palavra trocada, caput costurado ao inciso ou corte sem `[…]` ⇒ BLOQUEAR e trocar pelo literal integral. Mesmo com `[…]`, o corte não tira sujeito, dever, objeto, condição, limite, prazo nem ressalva da regra (quem, o quê, quando e até onde): se tirar, o alcance muda ⇒ BLOQUEAR e citar inteiro. Na coluna do crivo, o literal do trecho citado vai inteiro, do primeiro ao último termo, sem `[…]` nem `…`, ainda que a entrega corte. Vale para toda aspa da entrega, inclusive dentro de tabela, quadro de custos, calendário e do próprio crivo: o teto, o prazo ou a regra citada leva o objeto a que se aplica (que valor, que despesa, que parte, que evento).
- Paráfrase sem ampliar hipótese, sujeito ou condição: CAM-CCBC 35.6 (`context/packs/cam-ccbc-2025/regulamento.md` L526 «35.6 O Termo de Arbitragem») só cobre cobrança ou execução de taxa, honorários e despesas.
- Condição do literal: CAM B3 8.4.1 (`context/packs/cam-b3-2026/regulamento.md` L159 «**8.4.1** Caso a Presidência da CAM tenha decidido») só preserva os mesmos pedidos em outros procedimentos quando a Presidência decidiu que o procedimento «não deve prosseguir parcialmente», salvo o 6.3.2; «o arquivamento não impede novo procedimento», sem a condição, amplia a hipótese ⇒ BLOQUEAR.
- A remissão da Lei 9.307 ao CPC/1973 fica como está (`context/lei-9307-1996.md` L636 «§ 1o A demanda»).

## Tese contrária (R3)

- Testar com o próprio corpus: competência do árbitro sobre a convenção (`context/lei-9307-1996.md` L156 «Parágrafo único. Caberá ao árbitro decidir»); via judicial excepcional para cláusula patológica (`context/stj-resp-1602076-sp-nulidade-clausula.md` L14 «4. O Poder Judiciário pode»; inteiro teor, C09: `context/jurisprudencia-verificada.md:120`).

## Precedentes da lista verificada (regra de citação)

- Lista fechada: `context/jurisprudencia-verificada.md` (C01, C02, C04–C10 e, no fim, as fichas `context/stj-*.md`/`context/stf-*.md`). Conclusão que depende de julgado fora dela ⇒ `PENDENTE DE FONTE`; C03 está fora (acesso restrito, só notícia) e não é citado.
- Aspas só no trecho literal do caso, com `context/jurisprudencia-verificada.md:<linha>`, sempre junto da linha **O que decidiu** do mesmo caso; ficha `stj-`/`stf-`, só pelo `[Ln]`. Abrir o registro e conferir tribunal, número, órgão, data e trecho palavra a palavra; divergência ⇒ BLOQUEAR.
- **O que decidiu** não é literal nem amplia a tese. **Nota do plugin (não citável)** nunca é resultado do julgado nem fundamento: lei revogada (C09: Lei 8.955/1994, revogada pela Lei 13.966/2019), limites e ressalvas ficam como contexto, sem aspas.
- Julgado de Turma, Seção ou TJSP ⇒ 🟡 de alcance. Precedente não supre documento do caso: sem prova, `PENDENTE DE PROVA`. Armadilhas: C01 não cobre pedido intempestivo; C02 preserva as defesas do art. 525, § 1º (`context/jurisprudencia-verificada.md:36`); C06 tem a demanda originária sob o CPC/1973 (contexto da Nota do plugin, sem aspas); C07 não autoriza equidade sem escolha; C10 chama de "Árbitro de Emergência" o juízo estatal eleito, não o procedimento da CAMARB.

## Objetos com armadilha conhecida

- Termo: procurar o conteúdo no Termo inteiro, inclusive na convenção transcrita; não exigir seção autônoma que a norma não exige (`context/packs/cam-ccbc-2025/regulamento.md` L416 «(g) lei aplicável»: «lei brasileira» presente ⇒ conteúdo presente, conferir coerência). Ausência jurídica obrigatória ≠ remissão editorial opcional.
- Sigilo: confidencialidade só com fonte (cláusula, regulamento com `Ln`, lei); sem fonte, a promessa sai.
- Sigilo absoluto, proibição de uso judicial ou renúncia: transcrever o trecho documental que sustenta; declaração simples de sigilo não afasta as exceções. Confrontar `context/packs/cam-ccbc-2025/regulamento.md` L578 «39.1 A arbitragem será confidencial, exceto» e L579 «39.1.1 Não configura violação de dever de sigilo» (proteção de direito) com L526 «35.6 O Termo de Arbitragem» (cobrança ou execução de taxa, honorários e despesas); explicar cada hipótese e limite, sem contraproposta irrestrita de divulgação.
- Art. 4º §2º: iniciativa ou concordância expressa com a instituição, por escrito em documento anexo ou em negrito, com assinatura ou visto especialmente para a cláusula; assinatura ou visto sozinhos não substituem a concordância.
- Art. 37: I sentença (original ou cópia certificada, autenticação consular, tradução oficial) e II convenção (original ou cópia certificada, tradução oficial); não transportar a autenticação consular ao II.
- Condições cumulativas: confrontar cada uma e preservar as alternativas; atendimento parcial não fecha o item.
