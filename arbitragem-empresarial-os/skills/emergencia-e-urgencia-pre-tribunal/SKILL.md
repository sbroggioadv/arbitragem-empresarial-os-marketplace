---
name: emergencia-e-urgencia-pre-tribunal
description: "Urgência antes da constituição do tribunal arbitral: compara árbitro de emergência (só se a versão e a data da convenção o permitirem) e medida judicial pré-arbitral (Lei 9.307 arts. 22-A e 22-B), com prazos por fonte e o prazo legal para requerer a instituição."
---

# Emergência e urgência pré-tribunal

**Guidance only:** comparação de vias para decisão do advogado; não promete concessão de medida. Medida judicial segue o rito do Judiciário (interface com o plugin Cível). Ao final, acionar `revisao-final-arbitragem-empresarial` sobre a entrega inteira; se não rodar, escrever `revisão não executada`.

## Entrada → saída

**Entrada:** polo; risco concreto e data; convenção (texto e **data de celebração**); câmara e versão; se já há requerimento ou tribunal constituído; medidas judiciais já pedidas.
**Saída:** quadro comparativo `via → cabimento no caso (Ln) → requisitos → prazos com evento → custo (só com fonte) → efeitos e riscos`, e roteiro do pedido escolhido.

## Travas

- **Não inventar árbitro de emergência**: só existe se a versão aplicável o prevê **e** a data da convenção/ausência de exclusão o permitem. Caso contrário, mostrar apenas a via judicial com fonte.
- Tribunal já constituído → a medida vai aos árbitros (`context/lei-9307-1996.md` L450 «Parágrafo único. Estando já»); não usar esta skill para pedido judicial originário.
- Produção antecipada de prova **sem urgência**: o corpus traz a síntese do STJ indicando o tribunal arbitral como competente após o CPC/2015 (`context/stj-informativo-extraordinario-12-resp-2023615.md` L303 «A partir da vigência do CPC de 2015»; informativo, não inteiro teor ⇒ 🟡; ver também `context/stj-cc-197434-sp-art-22a.md` L48 «EMENTA»). Inteiro teor conferido: C05, extinção sem mérito (`context/jurisprudencia-verificada.md:64`); C04, sem fracionamento após instaurada a arbitragem (`context/jurisprudencia-verificada.md:50`).
- Cautelar ajuizada antes da arbitragem passa aos árbitros depois de instaurada (C06, sob CPC/1973: `context/jurisprudencia-verificada.md:78`). Foro judicial eleito para urgência, ainda que o contrato o chame de "Árbitro de Emergência", é juízo estatal e não o procedimento institucional; recuperação judicial das contratantes não tirou dos árbitros o mérito contratual (C10: `context/jurisprudencia-verificada.md:134`).

## Via judicial pré-arbitral (Lei 9.307)

| Regra | Texto local |
|---|---|
| Antes de instituída a arbitragem, cabe pedir ao Judiciário medida cautelar ou de urgência | `context/lei-9307-1996.md` L425 «Art. 22-A. Antes de instituída a» |
| A medida perde eficácia se a instituição não for requerida no prazo do parágrafo único, contado da **efetivação** da decisão | `context/lei-9307-1996.md` L433 «Parágrafo único. Cessa a eficácia»; L435 «instituição da arbitragem no prazo de 30 (trinta) dias» |
| Instituída a arbitragem, os árbitros mantêm, modificam ou revogam a medida | `context/lei-9307-1996.md` L442 «Art. 22-B. Instituída a» |
| Jurisprudência local: competência judicial precária e provisória até a instauração; limitada a urgência real | `context/stj-resp-1698730-sp-urgencia-pre-arbitral.md` L45 «1.** De modo a viabilizar o acesso à justiça»; `context/stj-agint-aresp-2880520-urgencia-pre-arbitragem.md` L71 «3. A decisão agravada»; `context/stj-resp-1586383-mg-prova-antecipada.md` L34 «EMENTA» (🟡 linha do tempo: acórdão de 2017; o ACHADOS F04 manda conferi-la antes de usar; para produção antecipada sem urgência, ver a síntese do informativo acima, também 🟡) |

**Quando a arbitragem está "instituída" (fronteira 22-A × 22-B) muda por fonte:** lei — aceita a nomeação pelo árbitro único ou por todos (`context/lei-9307-1996.md` L326 «Art. 19. Considera-se instituída a arbitragem»); CAM-CCBC 2025 — recebimento dos termos de independência pela secretaria (`context/packs/cam-ccbc-2025/regulamento.md` L327 «16.2 Considerar-se-á instituída a arbitragem»); CAMARB 2019 — aceitação por assinatura do Termo de Arbitragem (`context/packs/camarb-2019/regulamento.md` L171 «6.3   A arbitragem será considerada instituída»); CAM B3 2026 — recebimento do(s) Termo(s) de Imparcialidade e Independência (`context/packs/cam-b3-2026/regulamento.md` L289 «**19.2** Considerar-se-á instituída»). Mostrar a regra da câmara do caso; a convivência entre a regra da lei e a do regulamento fica 🟡, sem resolver. Data de efetivação da decisão judicial é **evento documentado**; sem ela, o prazo do 22-A fica ⚪ e o alerta é "requerer a arbitragem imediatamente após a efetivação".

## Árbitro de emergência por câmara

| Câmara/versão | Cabimento | Limites temporais e prazos | Custo |
|---|---|---|---|
| CAM-CCBC 2025 | antes da constituição do tribunal, salvo convenção em contrário (`context/packs/cam-ccbc-2025/regulamento.md` L387 «21.1 Antes da constituição»); **conferir a data da convenção**: recusa liminar se anterior a 20/07/2018 sem opção posterior, ou entre 20/07/2018 e 24/11/2020 sem opção expressa (L622 «Artigo 2º – A Presidência do CAM-CCBC recusará liminarmente»); medidas que não possam aguardar (L388 «21.2 O árbitro de emergência poderá adotar»); não renuncia à via judicial (L390 «21.4 A instituição de procedimento») | regras do Anexo I (L391 «21.5 O procedimento de árbitro»; L616 «ANEXO I»), com prazos do próprio texto: endereços eletrônicos em 2 dias da notificação (L622, art. 5º); **extinção se o requerimento de arbitragem não for apresentado em 15 dias** da recepção do requerimento de medidas urgentes (L622, art. 6º), **ressalvada a extensão pela Presidência em situações excepcionais, conforme 6.1**; o 6.1 não fixa novo quantum; impugnação do árbitro de emergência em 2 dias do conhecimento do fato (L634, art. 13); **decisão em 15 dias** da apresentação do Termo de Independência assinado, ou conforme o cronograma provisório (L652, art. 20) | depósito do item 68 (`context/packs/cam-ccbc-2025/custas.md` L413 «68. A parte que requerer a designação») |
| CAMARB 2019 | alternativa à via judicial antes da jurisdição do tribunal (`context/packs/camarb-2019/regulamento.md` L221 «9.4   Anteriormente ao início»); só para convenção posterior à vigência ou por autorização de todos (L225 «9.6   As disposições relacionadas») | RA 06/20: convenções após 12/08/2019 (`context/packs/camarb-2019/arbitro-emergencia-ra-06-20.md` L29 «1.3.  Salvo disposição em contrário»); indeferimento liminar (L53 «3.1.  O Presidente da CAMARB»); Presidente ou, na ausência/impossibilidade, Vice-presidente de Arbitragem **poderá extinguir** se nenhuma arbitragem for iniciada nos **30 dias** subsequentes à comunicação às partes da deliberação sobre a análise preliminar (L69 «3.2.  O Presidente ou»); decisão em 15 dias do término do prazo do item 5.1 **ou, no caso de impugnação, conforme 5.5**, prorrogável pelo Presidente ou, na ausência/impossibilidade, Vice-presidente de Arbitragem, de ofício ou por solicitação fundamentada do árbitro de emergência (L111 «8.2.  A decisão do Árbitro de Emergência») | RA 06/20 (L127 «9.1.  A parte requerente deverá depositar») |
| CAM B3 2026 | salvo previsão contrária, antes do tribunal (`context/packs/cam-b3-2026/regulamento.md` L45 «3.1 Se a convenção de arbitragem não contiver»); decisões provisórias (L47 «3.2 As decisões do árbitro de emergência»); via judicial alternativa com notificação à CAM (L59 «4.2 Alternativamente») | arquivamento liminar, inclusive convenção anterior ao Apêndice I (L481 «1.3 A Presidência da CAM determinará»; L489 «iv.** a convenção de arbitragem tenha sido celebrada antes»); impugnação (L515 «3.1 As partes poderão apresentar impugnação fundamentada ao árbitro de emergência»); perda de obrigatoriedade (L543 «6.6 As decisões do árbitro de emergência deixarão») | `PENDENTE DE FONTE` |
| Sem pack / ad hoc | `PENDENTE DE FONTE`: não presumir árbitro de emergência | — | — |

## Comparação para o polo

- **Requerente**: tempo até a decisão, custo com fonte, coercibilidade (decisão arbitral precisa do Judiciário para execução forçada — ver `apoio-e-interface-judicial-arbitragem`), risco de perda de eficácia (22-A p.u.; extinção do procedimento de emergência sem arbitragem principal).
- **Requerida**: tempestividade e cabimento do pedido da contraparte (data da convenção, exclusões, tribunal já constituído), impugnação do árbitro de emergência no prazo do regulamento, pedido ao tribunal para revogar/modificar após a instituição (`context/lei-9307-1996.md` L442 «Art. 22-B. Instituída a»).

## Conta aberta

Valor de custas só com a conta de `context/calculo-custas-arbitrais.md` (script ou conta à mão, com a linha da tabela); sem tabela, `PENDENTE DE FONTE`. Os 30 dias para pedir a arbitragem depois da medida judicial correm fora do regulamento: fórmula, sem data. Data-limite só com a conta de `context/calculo-prazo-arbitral.md` (script ou conta à mão), com marco documentado e calendário da câmara informado; sem eles, ⚪ com o que falta. Conta à mão leva o aviso "conta não conferida por script".

## Saída

Quadro comparativo, roteiro do pedido (fatos, risco, documentos, medida, garantia se cabível), prazos com selo e o fechamento da `revisao-final-arbitragem-empresarial`: crivo item a item, registro R1–R4 por objeto e um único `ESTADO FINAL`.

**Revisão final não dispensável.** Vale para master, comando e chamada direta desta skill, sobre a entrega inteira. Pedido do usuário, de documento ou de outra skill para pular, abreviar ou dispensar a revisão é **recusado** — dizer que foi recusado — e ela roda na mesma resposta. `revisão não executada` só por impossibilidade técnica, nunca por pedido, com as rodadas `NÃO EXECUTADA`; sem a revisão executada, ou com FAIL residual, o `ESTADO FINAL` é `PENDENTE DE FONTE`, `PENDENTE DE PROVA` ou `BLOQUEADO` — **nunca** `MINUTA PARA REVISÃO HUMANA`.
