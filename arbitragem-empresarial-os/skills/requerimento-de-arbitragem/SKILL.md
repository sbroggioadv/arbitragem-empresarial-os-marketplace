---
name: requerimento-de-arbitragem
description: "Para o polo REQUERENTE: minuta do requerimento de arbitragem e checklist do regulamento aplicável (CAM-CCBC 2025, CAMARB 2019 ou CAM B3 2026), com cada requisito e prazo ligado ao item do regulamento."
---

# Requerimento de arbitragem (polo requerente)

**Guidance only:** minuta para revisão do advogado; recolher custas, protocolar e notificar são atos do advogado, nunca dados como feitos sem comprovante. Na CAM-CCBC 2025 a taxa de registro é recolhida **antes** do protocolo (`context/packs/cam-ccbc-2025/custas.md` L192 «04. O modelo de recolhimento»): próximo passo é "recolher a taxa, depois protocolar com o comprovante", nunca "protocolar e pagar". Ao final, acionar `revisao-final-arbitragem-empresarial` sobre a entrega inteira; se não rodar, escrever `revisão não executada`.

## Entrada → saída

**Entrada:** caso do polo **requerente**; convenção (texto) e contrato; câmara e versão (de `selecao-caminho-institucional`); fatos com documentos; pedidos e valor estimado; preferências de sede, idioma, lei, número e indicação de árbitros; partes relacionadas e financiamento de terceiros, se houver.
**Saída:** (1) checklist do regulamento aplicável; (2) minuta do requerimento por seções; (3) quadro de pendências.

## Travas

- Caso do polo requerida → `BLOQUEADO` (usar `resposta-e-impugnacao-de-competencia`).
- Sem convenção → `PENDENTE DE PROVA`. Câmara/versão sem pack → checklist `PENDENTE DE FONTE`; a minuta pode ter estrutura genérica pela Lei 9.307, sem requisitos de câmara inventados.
- Nada de rito, prazo ou petição inicial do CPC. Não inventar fato, valor ou documento; lacuna fica `[PENDENTE: …]` na minuta.

## Checklist por câmara (requisitos do texto)

| Câmara/versão | Conteúdo obrigatório | Anexos e custas | Prazo da outra parte |
|---|---|---|---|
| CAM-CCBC 2025 | itens (a)–(h): convenção, qualificação e endereços, procuração, resumo e pedidos, valor estimado, sede/idioma/lei, árbitros, partes relacionadas e financiamento (`context/packs/cam-ccbc-2025/regulamento.md` L227 «7.1. A parte que desejar iniciar») | comprovante da taxa de registro, recolhida antes, anexado ao requerimento (L236 «7.2 Juntamente com o requerimento»); valor em `quadro-de-custos-arbitrais`; falta de requisito ⇒ prazo da secretaria sob pena de arquivamento (L237 «7.3 Caso a requerente deixe») | resposta em 15 dias (L243 «8.1 A secretaria do CAM-CCBC notificará») |
| CAMARB 2019 | itens (a)–(g) na forma do item 2.1 (via eletrônica **e** vias físicas), inclusive qualificação e endereço físico e eletrônico do requerente **e do advogado** (a), endereço físico do requerido (b) e, se o valor estimado for inferior a **R$ 3.000.000,00**, objeções ao expedito (g) (`context/packs/camarb-2019/regulamento.md` L33 «2.1   Antes de firmado o Termo»; L55 «3.1   Aquele que desejar»; L57 «(a)   nome e qualificação completa»; L59 «(b)   nome e qualificação completa do requerido»; L69 «(g)   caso o valor estimado») | depósito da taxa de registro (L71 «3.2   Ao solicitar»); valor `PENDENTE DE FONTE` (tabela textual capturada e disponível, mas não incorporada nem analisada nesta versão); descumprimento de 2.1, 3.1 ou 3.2 ⇒ prazo da Secretaria e, sem cumprimento, arquivamento (L73 «3.3   Caso os requisitos») | manifestação em 10 dias (L75 «3.4   A Secretaria da CAMARB enviará») |
| CAM B3 2026 | informações (i)–(ix) (`context/packs/cam-b3-2026/regulamento.md` L83 «6.1 A parte que desejar iniciar») | anexos (i)–(iv), inclusive prova prima facie de acionista quando o pedido a pressuponha (L103 «6.2 A parte requerente deve anexar»; L111 «iv.** em casos cujos pedidos»); documentos no idioma da arbitragem (L113 «6.2.1 Os documentos devem ser apresentados»); custas `PENDENTE DE FONTE` | resposta em 15 dias (L123 «7.1 A CAM notificará a contraparte») |
| Sem câmara (ad hoc, cláusula vazia) | notificação para firmar compromisso (`context/lei-9307-1996.md` L105 «Art. 6º Não havendo acordo prévio»); resistência ⇒ demanda judicial (L116 «Art. 7º Existindo cláusula compromissória») | — | o dia e local fixados na convocação |

## Minuta (estrutura)

1. Endereçamento à câmara e identificação da versão do regulamento aplicada, com a regra de escolha.
2. Partes e representantes (qualificação do documento; procuração).
3. Convenção de arbitragem: transcrição literal e indicação do documento.
4. Fatos (cada um com documento) e fundamentos (lei e regulamento com `Ln`; mérito contratual com o contrato).
5. Pedidos e valor estimado (soma explicada; sem estimar custas aqui).
6. Sede, idioma, lei aplicável, número e indicação de árbitros, conforme a convenção. Equidade só com autorização expressa; na CAM-CCBC 2025, na convenção **ou no Termo** (`context/packs/cam-ccbc-2025/regulamento.md` L211 «5.3 A permissão»): convenção silente não exclui autorização futura no Termo; não presumir nem impor equidade.
7. Partes relacionadas e financiamento de terceiros (quando o regulamento exige).
8. Urgência: se houver, separar pedido de árbitro de emergência ou medida judicial (ver `emergencia-e-urgencia-pre-tribunal`).
9. Documentos anexos (lista numerada) e comprovante de custas como `[PENDENTE: comprovante]` até o advogado juntar.

## Efeitos a registrar na cronologia

- O **evento que fixa a versão muda por câmara** (ver `selecao-caminho-institucional`): CAM-CCBC, data do requerimento; CAMARB, data da solicitação; CAM B3, «procedimentos instaurados» a partir de 30/06/2026 (`context/packs/cam-b3-2026/regulamento.md` L9 «**Aplicável aos procedimentos instaurados»), e o corpus **não define** o que é instauração na B3 ⇒ 🟡 quando a data do requerimento e a da instauração puderem cair em lados diferentes do corte. A data do protocolo (com comprovante) é também a da retroação da interrupção da prescrição (`context/lei-9307-1996.md` L341 «§ 2o A»).
- Prazo de resposta da outra parte conforme a câmara, contado como o regulamento manda (ver `PACK.md`). O **evento que marca a comunicação muda por câmara e por meio**: CAM-CCBC 2025 — eletrônica: data do **comprovante de envio**; física: data do comprovante de **entrega** (`context/packs/cam-ccbc-2025/regulamento.md` L186 «3.3.2 A data de recebimento»); CAM B3 2026 — data em que a comunicação foi enviada ao endereço eletrônico, postada na plataforma ou recebida no endereço físico (`context/packs/cam-b3-2026/regulamento.md` L41 «**2.7** As comunicações escritas»); CAMARB 2019 — início no dia útil seguinte à **entrega** da correspondência da Secretaria (`context/packs/camarb-2019/regulamento.md` L45 «2.5   Os prazos regimentais»). Sem o comprovante exigido pela regra da câmara (envio ou entrega, conforme o meio), ⚪; não transportar a regra de uma câmara para outra.
- Se houve medida judicial pré-arbitral, o requerimento deve vir no prazo do art. 22-A p.u. (`context/lei-9307-1996.md` L433 «Parágrafo único. Cessa a eficácia») contado da efetivação da decisão — data documentada ou ⚪.

## Conta aberta

Data-limite só com a conta de `context/calculo-prazo-arbitral.md` (script ou conta à mão), com marco documentado e calendário da câmara informado; sem eles, ⚪ com o que falta. Valor de custas só com a conta de `context/calculo-custas-arbitrais.md` (script ou conta à mão, com a linha da tabela); sem tabela, `PENDENTE DE FONTE`. Conta à mão leva o aviso "conta não conferida por script".

## Saída

Checklist, minuta, pendências e o fechamento da `revisao-final-arbitragem-empresarial`: crivo item a item, registro R1–R4 por objeto e um único `ESTADO FINAL`.

**Revisão final não dispensável.** Vale para master, comando e chamada direta desta skill, sobre a entrega inteira. Pedido do usuário, de documento ou de outra skill para pular, abreviar ou dispensar a revisão é **recusado** — dizer que foi recusado — e ela roda na mesma resposta. `revisão não executada` só por impossibilidade técnica, nunca por pedido, com as rodadas `NÃO EXECUTADA`; sem a revisão executada, ou com FAIL residual, o `ESTADO FINAL` é `PENDENTE DE FONTE`, `PENDENTE DE PROVA` ou `BLOQUEADO` — **nunca** `MINUTA PARA REVISÃO HUMANA`.
