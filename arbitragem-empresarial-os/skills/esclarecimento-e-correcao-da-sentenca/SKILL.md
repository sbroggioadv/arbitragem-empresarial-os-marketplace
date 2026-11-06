---
name: esclarecimento-e-correcao-da-sentenca
description: "Após a sentença arbitral: análise de requisitos, erro material, omissão, obscuridade e contradição; pedido de esclarecimento com prazos da lei e do regulamento mostrados lado a lado (nunca prazo único) e efeito sobre o prazo da ação de nulidade."
---

# Esclarecimento e correção da sentença arbitral

**Guidance only:** análise e minuta para revisão do advogado. A escolha entre o prazo legal e o do regulamento é **questão jurídica aberta** que depende da convenção e do regulamento aplicáveis ao caso. Ao final, acionar `revisao-final-arbitragem-empresarial` sobre a entrega inteira; se não rodar, escrever `revisão não executada`.

## Entrada → saída

**Entrada:** sentença (parcial ou final) com a **data de recebimento** da notificação; convenção; Termo; câmara e versão; pedidos das partes; polo.
**Saída:** (1) checagem de requisitos e limites da sentença; (2) quadro de prazos com fonte e evento; (3) minuta de pedido de esclarecimento/correção, se cabível; (4) reflexo no prazo da ação de nulidade (ver `apoio-e-interface-judicial-arbitragem`).

## Travas

- **Nunca um prazo único.** Mostrar o prazo da lei **e** o do regulamento aplicável, com a ressalva legal de "outro prazo acordado", e marcar 🟡 a definição; recomendar observar o mais curto enquanto a questão não for resolvida pelo advogado.
- **Versão primeiro:** câmara e versão pela data do caso (`selecao-caminho-institucional`); versão sem pack (ex.: CAM-CCBC com requerimento antes de 03/11/2025 sem a opção do 43.3; CAM B3 instaurada antes de 30/06/2026) ⇒ linhas de regulamento `PENDENTE DE FONTE`, mesmo que o número pareça igual.
- Sem data de recebimento documentada → prazos ⚪ (mostrar a regra, não a data). Contagem: a do regulamento aplicável (ver `calendario-e-ordens-processuais`); a lei capturada não define dias úteis ou corridos — nunca usar a contagem do CPC por padrão.
- Pedido de esclarecimento não é recurso de mérito. **O rol muda por fonte:** lei — erro material, obscuridade, dúvida, contradição, omissão (`context/lei-9307-1996.md` L573 «- corrija qualquer erro material»; L576 «- esclareça alguma obscuridade, dúvida ou contradição»); CAMARB — o mesmo rol (`context/packs/camarb-2019/regulamento.md` L255 «10.10 Na hipótese de erro material»); CAM-CCBC — contradição, omissão ou obscuridade (`context/packs/cam-ccbc-2025/regulamento.md` L492 «31.1 As partes poderão»); CAM B3 — erro material, obscuridade, omissão ou contradição, sem «dúvida» (`context/packs/cam-b3-2026/regulamento.md` L371 «**i.** corrija erro material»; L373 «**ii.** esclareça alguma obscuridade»). Hipótese fora do rol do regulamento ⇒ mostrar lei × regulamento, 🟡.

## Requisitos e limites da sentença (checagem)

| Ponto | Texto local |
|---|---|
| Requisitos obrigatórios (relatório, fundamentos, dispositivo com prazo de cumprimento, data e lugar) | `context/lei-9307-1996.md` L527 «Art. 26. São requisitos obrigatórios» |
| Assinatura e certificação | `context/lei-9307-1996.md` L542 «Parágrafo único. A sentença arbitral será assinada» |
| Custas, despesas e má-fé | `context/lei-9307-1996.md` L546 «Art. 27. A sentença arbitral decidirá» |
| Prazo para proferir — **três camadas, nunca só a lei**: (1) convenção ou Termo; (2) regulamento da câmara e versão do caso, com o evento de início; (3) lei só como supletiva (6 meses da instituição ou da substituição do árbitro, `context/lei-9307-1996.md` L488 «Nada tendo sido convencionado») | convenção/Termo: documento do caso; CAM-CCBC 2025: 60 dias do recebimento das alegações finais, salvo outro prazo no Termo ou acordado, prorrogável por até 60 a critério do presidente (`context/packs/cam-ccbc-2025/regulamento.md` L464 «29.1 O tribunal arbitral proferirá a sentença»; L465 «29.2 O prazo do artigo 29.1»); CAMARB 2019: 60 dias do término do prazo das alegações finais, prorrogável por até 60 (`context/packs/camarb-2019/regulamento.md` L229 «10.1  O Tribunal Arbitral proferirá sentença»); CAM B3 2026: até 60 dias depois de findo o prazo das alegações finais, prorrogável por até 60 (`context/packs/cam-b3-2026/regulamento.md` L329 «**24.1** O tribunal arbitral proferirá»); lei supletiva: `context/lei-9307-1996.md` L487 «Art. 23. A sentença arbitral será proferida»; prorrogação L500 «§ 2o»; no expedito CAM-CCBC, 30 dias do encerramento da instrução, prorrogáveis por igual período (`context/packs/cam-ccbc-2025/regulamento.md` L562 «37.13 A sentença arbitral será proferida»). Mostrar as camadas lado a lado com o evento e a data documentada de cada uma; **não concluir nulidade por prazo** (art. 32, VII) só pelo prazo legal — depende de qual prazo vale no caso e da notificação do art. 12, III (`context/lei-9307-1996.md` L223 «III - tendo expirado o prazo») |
| Sentenças parciais | `context/lei-9307-1996.md` L493 «§ 1o Os árbitros» |
| Efeitos e título executivo | `context/lei-9307-1996.md` L589 «Art. 31. A sentença arbitral produz» |
| Causas de nulidade (para avaliar a via adequada) | `context/lei-9307-1996.md` L593 «Art. 32. É nula a sentença arbitral se» |
| Sentença que não decide todos os pedidos: complementar via judicial | `context/lei-9307-1996.md` L674 «§ 4o A» |

## Prazos de esclarecimento (lado a lado)

| Fonte | Pedido | Decisão | Texto local |
|---|---|---|---|
| Lei 9.307 | **5 dias** do recebimento da notificação ou da ciência pessoal, **salvo outro prazo acordado** | **10 dias**, ou prazo acordado | `context/lei-9307-1996.md` L562 «Art. 30. No prazo de 5 (cinco)»; L572 «I»; L575 «II»; L581 «Parágrafo único. O árbitro ou o tribunal arbitral decidirá» |
| CAM-CCBC 2025 | **15 dias** do recebimento da sentença | manifestação facultada em **15 dias** (31.2); decisão em **15 dias** da última ocorrência (31.3), prorrogável por até **15** (31.4); honorários adicionais antecipados | `context/packs/cam-ccbc-2025/regulamento.md` L492 «31.1 As partes poderão»; L493 «31.2 O tribunal arbitral poderá facultar»; L494 «31.3. O tribunal arbitral decidirá»; L495 «31.4. O prazo do artigo 31.3»; `context/packs/cam-ccbc-2025/custas.md` L312 «43. Os esclarecimentos à sentença» |
| CAMARB 2019 | **15 dias** do recebimento da sentença | decisão em até **20 dias** do recebimento do pedido, prorrogável por mais **10** | `context/packs/camarb-2019/regulamento.md` L255 «10.10 Na hipótese de erro material»; L257 «10.11 O Tribunal Arbitral decidirá» |
| CAM B3 2026 | **15 dias** do recebimento da decisão | manifestação em **15 dias** (25.2); decisão em **30 dias** da última manifestação ou do fim do prazo (25.3); a decisão integra a sentença (25.4) | `context/packs/cam-b3-2026/regulamento.md` L369 «25.1 No prazo de 15 (quinze) dias»; L375 «25.2 O tribunal arbitral poderá conceder»; L377 «25.3 O tribunal arbitral decidirá»; L379 «25.4 A decisão do pedido de esclarecimento» |

**Divergência 5 × 15 dias:** a lei dá 5 dias salvo prazo acordado; os três regulamentos dão 15. Divergência documental registrada no corpus (ACHADOS E03): a convenção pode incorporar o regulamento (`context/lei-9307-1996.md` L99 «Art. 5º Reportando-se as partes»), mas a aplicação ao caso é 🟡 e decisão do advogado.

## Efeito sobre a ação de nulidade

O prazo da demanda de nulidade conta do recebimento da notificação da sentença **ou da decisão do pedido de esclarecimentos** (`context/lei-9307-1996.md` L636 «§ 1o A demanda»; L640 «até 90 (noventa) dias»); o STJ, em julgado de Turma, entendeu que o pedido de esclarecimentos interrompe o prazo independentemente de acolhimento (`context/stj-resp-2179459-go-esclarecimentos-interrompem-prazo.md` L39 «RECURSO ESPECIAL. AÇÃO ANULATÓRIA»; L41 «INTERRUPÇÃO, INDEPENDENTEMENTE DE REJEIÇÃO»; ementa ⇒ 🟡; trecho do inteiro teor, C01: `context/jurisprudencia-verificada.md:22`). Com pedido tempestivo, o termo inicial é a ciência da decisão dos esclarecimentos, mesmo rejeitados; a forma de notificação da sentença (ex.: publicação interna) não reabre a conta pela sentença. Registrar na cronologia as duas datas (recebimento da sentença; recebimento da decisão dos esclarecimentos). O julgado trata de rejeição ou acolhimento, **não** de pedido intempestivo: não afirmar que um pedido fora do prazo da lei ou do regulamento interrompe a anulatória.

## Minuta do pedido

Endereçamento ao tribunal arbitral (com cópia à câmara e comunicação à outra parte quando a lei ou o regulamento exigir); identificação da sentença; para cada ponto: trecho literal da sentença → vício (erro material, obscuridade, dúvida, contradição, omissão) → esclarecimento pedido; sem rediscutir mérito; comprovante de honorários adicionais quando o regulamento exigir (`[PENDENTE: comprovante]`).

## Conta aberta

Data-limite só com a conta de `context/calculo-prazo-arbitral.md` (script ou conta à mão), com marco documentado e calendário da câmara informado; sem eles, ⚪ com o que falta. A ação de nulidade (90 dias) corre fora do regulamento: o script devolve fórmula, sem data. Valor de custas só com a conta de `context/calculo-custas-arbitrais.md` (script ou conta à mão, com a linha da tabela); sem tabela, `PENDENTE DE FONTE`. Conta à mão leva o aviso "conta não conferida por script".

## Saída

Checagem, quadro de prazos lado a lado com selos, minuta e o fechamento da `revisao-final-arbitragem-empresarial`: crivo item a item, registro R1–R4 por objeto e um único `ESTADO FINAL`.

**Revisão final não dispensável.** Vale para master, comando e chamada direta desta skill, sobre a entrega inteira. Pedido do usuário, de documento ou de outra skill para pular, abreviar ou dispensar a revisão é **recusado** — dizer que foi recusado — e ela roda na mesma resposta. `revisão não executada` só por impossibilidade técnica, nunca por pedido, com as rodadas `NÃO EXECUTADA`; sem a revisão executada, ou com FAIL residual, o `ESTADO FINAL` é `PENDENTE DE FONTE`, `PENDENTE DE PROVA` ou `BLOQUEADO` — **nunca** `MINUTA PARA REVISÃO HUMANA`.
