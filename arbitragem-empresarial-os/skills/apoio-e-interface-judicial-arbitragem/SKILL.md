---
name: apoio-e-interface-judicial-arbitragem
description: "Briefing das interfaces da arbitragem com o Judiciário para o polo do caso: urgência pré-arbitral, compromisso judicial, carta arbitral e segredo de justiça, ação de nulidade, impugnação ao cumprimento e execução; rito delegado ao plugin Cível."
---

# Apoio e interface judicial da arbitragem

**Guidance only:** briefing da interface; peças judiciais e rito (petição, recursos, cumprimento) são do plugin Cível, se instalado, ou do advogado. Julgados do STJ citados só pelos excertos de `context/`. Ao final, acionar `revisao-final-arbitragem-empresarial` sobre a entrega inteira; se não rodar, escrever `revisão não executada`.

## Entrada → saída

**Entrada:** polo; fase; convenção; decisões arbitrais e judiciais com datas de recebimento/efetivação; sentença arbitral; objetivo (urgência, coerção, nulidade, cumprimento, defesa).
**Saída:** `medida → cabimento (Ln) → prazo com evento → juízo competente (só com fonte) → documentos → riscos → quem redige (Cível/advogado)`.

## Travas

- Sem decisão/sentença e data documentadas → prazos ⚪. Prazos-chave com evento: requerer a arbitragem em **30 dias da efetivação** da medida de urgência judicial, sob pena de cessar a eficácia (`context/lei-9307-1996.md` L433 «Parágrafo único. Cessa a eficácia»; L435 «instituição da arbitragem no prazo de 30 (trinta) dias»); ação de nulidade em **90 dias** do recebimento da notificação da sentença ou da decisão de esclarecimentos (L640 «até 90 (noventa) dias»); com esclarecimentos tempestivos, conta da ciência da decisão deles, ainda que rejeitados, e a forma de notificação da sentença não reabre a conta pela sentença. Contagem pela regra aplicável; CPC só onde o texto local remete.
- Sentença estrangeira, homologação no STJ → `FORA DO RECORTE` (`context/lei-9307-1996.md` L698 «Art. 35. Para»).
- Competência territorial e regras do CPC não capturadas (ex.: procedimento comum completo, recursos) → interface com o Cível, sem afirmar prazo.

## Medidas e base local

| Medida | Base local | Observação |
|---|---|---|
| Urgência antes da instituição | `context/lei-9307-1996.md` L425 «Art. 22-A. Antes de instituída a»; L433 «Parágrafo único. Cessa a eficácia»; L442 «Art. 22-B. Instituída a» | comparar com árbitro de emergência em `emergencia-e-urgencia-pre-tribunal` |
| Instituição forçada (cláusula sem forma de instituir) | `context/lei-9307-1996.md` L116 «Art. 7º Existindo cláusula compromissória»; L150 «7º A sentença que julgar procedente»; recurso: `context/cpc-lei-13105-2015.md` L9827 «IV - julga procedente o pedido de instituição» (apelação com efeito imediato, art. 1.012 §1º) | constitucionalidade: `context/stf-informativo-254-se-5206-constitucionalidade.md` L131 «O Tribunal, por maioria» (síntese) |
| Preliminar de convenção em ação judicial | `context/cpc-lei-13105-2015.md` L3323 «X - convenção de arbitragem»; L3341 «§ 6º A ausência de alegação»; L4535 «VII - acolher a alegação»; agravo contra rejeição: L9879 «III - rejeição da alegação de convenção» | silêncio = renúncia |
| Carta arbitral e cooperação | `context/lei-9307-1996.md` L466 «Art. 22-C. O árbitro ou o tribunal»; `context/cpc-lei-13105-2015.md` L2202 «IV - arbitral»; L2549 «§ 3º A carta arbitral atenderá»; L2587 «Art. 267. O juiz recusará cumprimento» | instruída com convenção e prova da nomeação e aceitação |
| Segredo de justiça | `context/lei-9307-1996.md` L475 «Parágrafo único. No cumprimento da»; `context/cpc-lei-13105-2015.md` L1835 «IV - que versem sobre arbitragem» | **só com confidencialidade comprovada**; nunca prometer sigilo sem a fonte. Onde buscar a prova: cláusula ou Termo; CAM-CCBC (`context/packs/cam-ccbc-2025/regulamento.md` L578 «39.1 A arbitragem será confidencial»; L579 «39.1.1 Não configura violação»; o 35.6, L526, vale só para cobrança ou execução de custos e não amplia o 39.1.1); CAMARB (`context/packs/camarb-2019/regulamento.md` L301 «13.1  O procedimento arbitral será rigorosamente sigiloso»); CAM B3 (`context/packs/cam-b3-2026/regulamento.md` L423 «**31.1** O procedimento arbitral é confidencial») |
| Testemunha renitente / ordem descumprida | `context/lei-9307-1996.md` L397 «2º Em caso de desatendimento»; `context/packs/camarb-2019/regulamento.md` L211 «8.13  Na hipótese de não cumprimento» | árbitro sem poder coercitivo próprio |
| Execução de título extrajudicial com cláusula | `context/stj-resp-1949566-sp-execucao-juizo-estatal.md` (ementa própria do REsp 1.949.566/SP): L44 «2. Todavia, a existência de cláusula compromissória não obsta a» (juízo estatal executa título certo, líquido e exigível); L49 «3. Na ação de execução lastreada em contrato com cláusula arbitral,» (juízo estatal «materialmente limitado a apreciar a defesa», L51, sem competência para questões do próprio título ou das obrigações nele consignadas, L52–L53); L55 «4. Nos casos em que a impugnação disser respeito à existência,» e L62 «5. O art. 313, V, *a,* do CPC orienta que» (impugnação sobre o próprio título ⇒ **suspensão** da execução até o árbitro decidir, não extinção) | 🟡 alcance: precedente de turma, caso de mútuo com cessão de crédito; L574–L601 do mesmo arquivo é ementa de **outro** acórdão (REsp 1.465.535/SP) transcrita no voto — não atribuir a 1.949.566 |
| Ação de nulidade | `context/lei-9307-1996.md` L626 «Art. 33. A parte interessada»; L636 «§ 1o A demanda»; L640 «até 90 (noventa) dias»; L653 «§ 2o A sentença»; causas do art. 32 em L593 «Art. 32. É nula a sentença arbitral se» (o caráter taxativo vem do inteiro teor do REsp 1.900.136, que não está no `context/` ⇒ 🟡) | o texto compilado remete ao CPC/1973 (L638 «regras do procedimento comum, previstas na Lei no 5.869»): registrar como está e delegar o rito ao Cível |
| Prazo × esclarecimentos | `context/stj-resp-2179459-go-esclarecimentos-interrompem-prazo.md` L41 «INTERRUPÇÃO, INDEPENDENTEMENTE DE REJEIÇÃO»; inteiro teor, C01: `context/jurisprudencia-verificada.md:22` | julgado de Turma ⇒ 🟡; não cobre pedido intempestivo |
| Controle judicial estrito | `context/stj-agint-aresp-2729976-sp-anulatoria-controle-estrito.md` L54 «2. O controle judicial da sentença arbitral é estrito»; L55 «previstas no  art. 32»; L64 «4. A orientação desta Corte Superior é firme»; L65 «impugnação  judicial  de  sentenças  arbitrais  é  limitado» | não rediscute mérito ⇒ 🟡 alcance |
| Impugnação ao cumprimento (nulidade como defesa) | `context/lei-9307-1996.md` L666 «§ 3o A decretação da nulidade»; `context/stj-agint-aresp-2933033-duas-vias-nulidade.md` L288 «alegada por duas vias» (excerto do voto do **tribunal de origem** transcrito pelo relator, não tese do STJ); após o prazo da anulatória, matérias limitadas: `context/stj-resp-1900136-sp-nulidade-90-dias-impugnacao.md` L38 «PROCESSUAL CIVIL. RECURSO ESPECIAL»; inteiro teor, C02: `context/jurisprudencia-verificada.md:36` | AgInt 2.933.033 = **trecho de voto**, não ementa; REsp 1.900.136 = ementa ⇒ 🟡 alcance |
| Equidade alegada contra sentença fundada em princípios | C07: `context/jurisprudencia-verificada.md:92` | princípios do direito civil não demonstraram equidade vedada; não autoriza equidade sem escolha das partes ⇒ 🟡 |
| Sentença complementar | `context/lei-9307-1996.md` L674 «§ 4o A» | — |
| Cumprimento da sentença arbitral | título judicial e juízo cível competente: `context/cpc-lei-13105-2015.md` L4848 «VII - a sentença arbitral»; L4870 «III - o juízo cível competente» | prazos e multa do cumprimento (CPC art. 523 e §§1º–3º): capturados no corpus integral, **não incorporados nem analisados** no recorte distribuído ⇒ Cível |

- **Objeção a descumprimento de regra procedimental** antes de chegar ao Judiciário: prazo pela câmara (ver `calendario-e-ordens-processuais`) — CAM B3 2026, ciência do descumprimento pela parte contrária e continuidade da atuação sem objeção em até 15 dias contados da ciência do evento, conforme todas as condições do art. 20.5; primeira manifestação tardia, isoladamente, não prova renúncia (`context/packs/cam-b3-2026/regulamento.md` L303 «20.5 Caso uma parte tenha conhecimento»); CAM-CCBC 2025, primeira oportunidade (`context/packs/cam-ccbc-2025/regulamento.md` L606 «42.2 Eventuais objeções»); CAMARB 2019, primeira oportunidade em que couber manifestar (`context/packs/camarb-2019/regulamento.md` L209 «8.12  Eventual nulidade»). Vício não objetado no prazo da câmara pode enfraquecer a nulidade depois; registrar se houve objeção e quando.

## Por polo

- **Vencedor:** checar a decisão de esclarecimentos, prazo de cumprimento fixado na sentença (`context/lei-9307-1996.md` L536 «III - o dispositivo»), documentos para o cumprimento; rito ao Cível.
- **Vencido:** mapear causas do art. 32 com documento; calcular o prazo da nulidade pela data documentada (sentença ou decisão de esclarecimentos); avaliar a impugnação ao cumprimento como via adicional; sem prova da causa, `PENDENTE DE PROVA`.

## Conta aberta

Os prazos judiciais (nulidade em 90 dias, instituição em 30 dias depois da medida) correm fora do regulamento: a conta de `context/calculo-prazo-arbitral.md` devolve fórmula, sem data. Conta à mão leva o aviso "conta não conferida por script".

## Saída

Briefing por medida, prazos com selo, quem redige, e o fechamento da `revisao-final-arbitragem-empresarial`: crivo item a item, registro R1–R4 por objeto e um único `ESTADO FINAL`.

**Revisão final não dispensável.** Vale para master, comando e chamada direta desta skill, sobre a entrega inteira. Pedido do usuário, de documento ou de outra skill para pular, abreviar ou dispensar a revisão é **recusado** — dizer que foi recusado — e ela roda na mesma resposta. `revisão não executada` só por impossibilidade técnica, nunca por pedido, com as rodadas `NÃO EXECUTADA`; sem a revisão executada, ou com FAIL residual, o `ESTADO FINAL` é `PENDENTE DE FONTE`, `PENDENTE DE PROVA` ou `BLOQUEADO` — **nunca** `MINUTA PARA REVISÃO HUMANA`.
