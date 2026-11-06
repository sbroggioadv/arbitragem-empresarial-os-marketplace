---
name: resposta-e-impugnacao-de-competencia
description: "Para o polo REQUERIDA: resposta ao requerimento de arbitragem com objeção de competência, existência, validade, eficácia ou escopo da convenção, no canal e prazo do regulamento aplicável e da Lei 9.307."
---

# Resposta e impugnação de competência (polo requerida)

**Guidance only:** minuta para revisão do advogado. A decisão sobre jurisdição é do tribunal arbitral; o exame da câmara, quando existe, é administrativo e preliminar. Ao final, acionar `revisao-final-arbitragem-empresarial` sobre a entrega inteira; se não rodar, escrever `revisão não executada`.

## Entrada → saída

**Entrada:** caso do polo **requerida**; notificação da câmara com data de recebimento; requerimento da contraparte (documento do caso); convenção e contrato; câmara e versão; fatos e documentos da defesa.
**Saída:** (1) mapa de objeções com base local; (2) minuta da resposta por seções; (3) prazos com fonte e evento; (4) riscos de preclusão.

## Travas

- Caso do polo requerente → `BLOQUEADO`. Não usar estratégia ou dado interno da requerente; o requerimento dela é documento do caso.
- Sem convenção nos autos → objeção por inexistência é possível, mas qualquer conclusão sobre competência fica `PENDENTE DE PROVA` até analisar o documento juntado pela requerente.
- Prazo só com notificação documentada; senão ⚪. Na **resposta arbitral**, nada de contestação ou prazo do CPC (a contestação do CPC só aparece na ação judicial, abaixo).

## Base das objeções

| Objeção | Texto local |
|---|---|
| Momento: primeira oportunidade após a instituição; se rejeitada, segue a arbitragem e o tema pode ir à ação do art. 33 (o texto compilado do art. 33 §1º ainda remete ao CPC/1973 — rito ao Cível) | `context/lei-9307-1996.md` L350 «Art. 20. A parte que pretender»; L362 «2º Não sendo acolhida a argüição» |
| Árbitro decide existência, validade e eficácia (competência-competência) | `context/lei-9307-1996.md` L156 «Parágrafo único. Caberá ao árbitro decidir» |
| Adesão sem os requisitos de eficácia | `context/lei-9307-1996.md` L80 «2º Nos contratos de adesão»; `context/stj-resp-1602076-sp-nulidade-clausula.md` L13 «3. Todos os contratos de adesão» |
| Autonomia da cláusula (contraponto: nulidade do contrato não a contamina necessariamente) | `context/lei-9307-1996.md` L152 «Art. 8º A cláusula compromissória é autônoma» |
| Escopo: pedido fora dos limites da convenção | art. 32, IV: `context/lei-9307-1996.md` L593 «Art. 32. É nula a sentença arbitral se»; L610 «for proferida fora dos limites» (nulidade futura, se ignorado) |
| Arbitrabilidade (matérias e sujeitos) | ver `matriz-arbitrabilidade-competencia` |
| Consequência do acolhimento | Lei: partes remetidas ao Judiciário (`context/lei-9307-1996.md` L356 «1º Acolhida a argüição»; L359 «serão as partes remetidas»); CAM B3: objeção sobre existência, validade ou **escopo** (o 8.1 não menciona eficácia) e possível arquivamento pela Presidência (`context/packs/cam-b3-2026/regulamento.md` L147 «**8.1** A parte que pretender apresentar objeção»; L157 «**ii.** pelo arquivamento»); CAMARB: efeito sobre honorários se não houve instrução de mérito (`context/packs/camarb-2019/regulamento.md` L105 «3.12  Na hipótese do item precedente») |
| Preclusão procedimental (além da competência) | por câmara, ver `calendario-e-ordens-processuais`: CAM B3 ciência do descumprimento pela parte contrária e continuidade da atuação sem objeção em até 15 dias contados da ciência do evento, conforme todas as condições do art. 20.5; primeira manifestação tardia, isoladamente, não prova renúncia (`context/packs/cam-b3-2026/regulamento.md` L303 «20.5 Caso uma parte tenha conhecimento»); CAM-CCBC primeira oportunidade (`context/packs/cam-ccbc-2025/regulamento.md` L606 «42.2 Eventuais objeções»); CAMARB primeira oportunidade em que couber manifestar (`context/packs/camarb-2019/regulamento.md` L209 «8.12  Eventual nulidade») |

## Canal e prazo por câmara

| Câmara/versão | Resposta | Objeção à convenção |
|---|---|---|
| CAM-CCBC 2025 | 15 dias, conteúdo (a)–(g) (`context/packs/cam-ccbc-2025/regulamento.md` L243 «8.1 A secretaria do CAM-CCBC notificará») | objeção formal à Presidência na primeira oportunidade; exame prima facie administrativo; decisão de prosseguir é preliminar e o tribunal decide a jurisdição (L335 «17.1 A parte que pretender obstar»; L336 «17.2 A Presidência»; L337 «17.3 A decisão da Presidência») |
| CAMARB 2019 | manifestação em 10 dias, com eventual reconvenção (`context/packs/camarb-2019/regulamento.md` L75 «3.4   A Secretaria da CAMARB enviará»; L79 «3.6   Havendo interesse em reconvir») | inexistência formal: Diretoria decide prima facie, sem dilação; demais questões ao tribunal (L103 «3.11  Caso haja manifestação do requerido») |
| CAM B3 2026 | 15 dias, conteúdo (i)–(viii) (`context/packs/cam-b3-2026/regulamento.md` L123 «7.1 A CAM notificará a contraparte») | objeção na primeira oportunidade; falta de prova de acionista é matéria de objeção; Presidência decide prima facie (L147 «8.1 A parte que pretender apresentar objeção»; L149 «8.2 É matéria de objeção»; L153 «8.4 Apresentada a objeção») |

Ausência da requerida não impede o prosseguimento **desde que devidamente notificada** (`context/packs/cam-ccbc-2025/regulamento.md` L251 «8.2 O processo prosseguirá», «desde que devidamente notificadas»), e no CAM-CCBC a sentença **não pode fundar-se na revelia** (L472 «30.2 A sentença arbitral será expressa»); `context/packs/cam-b3-2026/regulamento.md` L143 «7.3 A ausência de qualquer das partes»). Revelia não impede a sentença (`context/lei-9307-1996.md` L405 «3º A revelia da parte»).

## Se a requerente for ao Judiciário

**No processo judicial** (não na arbitragem): se a contraparte ajuizar ação sobre a matéria da convenção, alegar a convenção como preliminar na contestação judicial: o juiz não a conhece de ofício e o silêncio implica renúncia (`context/cpc-lei-13105-2015.md` L3323 «X - convenção de arbitragem»; L3339 «§ 5º Excetuadas a convenção»; L3341 «§ 6º A ausência de alegação»). Rito judicial: interface com o plugin Cível (`apoio-e-interface-judicial-arbitragem`).

## Minuta (estrutura)

1. Identificação, procuração e endereços (itens do regulamento aplicável).
2. **Preliminar**: objeção à existência, validade, eficácia ou escopo da convenção, com fatos documentados e base local; pedido de exame pelo órgão previsto no regulamento e reserva de jurisdição ao tribunal.
3. Considerações sobre fatos e pedidos (sem prejuízo da preliminar), sede, idioma, lei, número de árbitros.
4. Pedidos contrapostos/reconvenção, se o regulamento admitir e o cliente decidir, com valor.
5. Partes relacionadas e financiamento de terceiros, quando exigido.
6. Pendências `[PENDENTE: …]` para fato, documento ou valor ausente.

## Conta aberta

Data-limite só com a conta de `context/calculo-prazo-arbitral.md` (script ou conta à mão), com marco documentado e calendário da câmara informado; sem eles, ⚪ com o que falta. Conta à mão leva o aviso "conta não conferida por script".

## Saída

Mapa de objeções, minuta, prazos com selo e o fechamento da `revisao-final-arbitragem-empresarial`: crivo item a item, registro R1–R4 por objeto e um único `ESTADO FINAL`.

**Revisão final não dispensável.** Vale para master, comando e chamada direta desta skill, sobre a entrega inteira. Pedido do usuário, de documento ou de outra skill para pular, abreviar ou dispensar a revisão é **recusado** — dizer que foi recusado — e ela roda na mesma resposta. `revisão não executada` só por impossibilidade técnica, nunca por pedido, com as rodadas `NÃO EXECUTADA`; sem a revisão executada, ou com FAIL residual, o `ESTADO FINAL` é `PENDENTE DE FONTE`, `PENDENTE DE PROVA` ou `BLOQUEADO` — **nunca** `MINUTA PARA REVISÃO HUMANA`.
