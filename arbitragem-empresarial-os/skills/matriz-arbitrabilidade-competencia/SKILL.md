---
name: matriz-arbitrabilidade-competencia
description: "Matriz de arbitrabilidade subjetiva e objetiva e de competência (árbitro × Judiciário) para arbitragem empresarial, só com texto legal e julgados locais; sem convenção, PENDENTE DE PROVA."
---

# Matriz de arbitrabilidade e competência

**Guidance only:** a matriz organiza o texto legal aplicável; não conclui que o litígio concreto é arbitrável — isso é qualificação jurídica do advogado. Ao final, acionar `revisao-final-arbitragem-empresarial` sobre a entrega inteira; se não rodar, escrever `revisão não executada`.

## Entrada → saída

**Entrada:** polo do caso; partes (por papel e natureza: empresa privada, S.A., ente público, consumidor, empregado, massa/recuperanda); objeto do litígio; texto da convenção; contrato e forma de adesão; datas.
**Saída:** matriz `critério → fato/documento → texto local (Ln) → leitura → selo` e a conclusão possível (arbitrável em tese · depende de prova · fora do recorte · pendente).

## Trava

- **Sem texto da convenção → `PENDENTE DE PROVA`** e nenhuma conclusão de competência (nem do árbitro, nem do Judiciário).
- Nunca presumir arbitrabilidade de matéria sensível; o corpus não tem jurisprudência por matéria além das teses de 2019 (lacuna declarada): exclusão sai como enquadramento pelo texto legal ou `FORA DO RECORTE`, nunca como tese.

## Critérios da matriz

| Critério | Texto local | Leitura que a matriz registra |
|---|---|---|
| Sujeito capaz de contratar e direito patrimonial disponível | `context/lei-9307-1996.md` L22 «Art. 1º As pessoas capazes de contratar» | "disponível" é qualificação do caso; a lei não lista matérias |
| Compromisso vedado para estado, família e não patrimonial | `context/cc-lei-10406-2002.md` L5890 «Art. 852. É vedado compromisso» | sinal de `FORA DO RECORTE` |
| Administração pública | `context/lei-9307-1996.md` L25 «§ 1o A»; L33 «§ 2o»; L55 «§ 3o A arbitragem que envolva a»; `context/lei-14133-2021.md` L6384 «151. Nas contratações regidas»; L6395 «152. A arbitragem será sempre de direito»; `context/stj-jurisprudencia-em-teses-122.md` L554 «13) Não existe óbice legal» | enquadramento: sempre de direito e publicidade; procedimento do ente fora do corpus ⇒ `FORA DO RECORTE` para peça |
| União — setores portuário e de transportes | `context/decreto-10025-2019.md` L33 «Art. 1º Este Decreto»; L63 «Art. 3º A arbitragem de que trata»; L196 «Art. 8º No procedimento arbitral» | regime próprio; `FORA DO RECORTE` para peça |
| Consumo | `context/cdc-lei-8078-1990.md` L869 «VII - determinem a utilização compulsória»; `context/stj-jurisprudencia-em-teses-122.md` L507 «11) A legislação consumerista» | `FORA DO RECORTE` **por escopo do produto**, não por conclusão de inarbitrabilidade: o texto local condiciona, não exclui — veda a arbitragem prévia e compulsória, mas admite a instaurada depois do litígio por consenso (L508 «momento da celebração do contrato, mas não proíbe que, posteriormente, em face»; L509 «de eventual litígio, havendo consenso entre as partes, seja instaurado o») |
| Adesão sem relação de consumo (ex.: franquia) | `context/lei-9307-1996.md` L80 «2º Nos contratos de adesão»; `context/stj-resp-1602076-sp-nulidade-clausula.md` L13 «3. Todos os contratos de adesão»; inteiro teor, C09: `context/jurisprudencia-verificada.md:120` | conferir no documento: iniciativa ou concordância expressa do aderente, documento anexo ou negrito com visto/assinatura específica; ausência = risco de ineficácia, `PENDENTE DE PROVA` até ver o contrato |
| Associação: cláusula inserida por assembleia | `context/stj-resp-2166582-sc-nulidade-clausula.md` L46 «EMENTA» | só a ementa foi lida (voto pendente) ⇒ 🟡 |
| Trabalho | `context/clt-dl-5452-1943.md` L11670 «Art. 507-A» | `FORA DO RECORTE` **por escopo do produto**, não por conclusão de inarbitrabilidade: o texto admite cláusula se a remuneração superar duas vezes o teto do RGPS e houver iniciativa ou concordância expressa do empregado (L11671 «cuja remuneração seja superior a duas vezes»; L11672 «poderá ser pactuada cláusula compromissória»; L11673 «a sua concordância expressa») |
| Recuperação/falência | `context/lei-11101-2005.md` L230 «§ 9º O processamento da recuperação judicial»; C10: `context/jurisprudencia-verificada.md:136` | convenção não é afastada pelo texto; litígio contratual de recuperanda segue à arbitragem na cognição, não na execução (C10); insolvência em si fora do recorte |
| Estatuto de S.A. | art. 109 §3º (`context/lei-6404-1976.md` L2283 «§ 3o O estatuto da sociedade»); art. 136-A: obriga todos os acionistas, com **direito de retirada** do dissidente mediante reembolso, **ressalvadas as hipóteses do §2º, I–II** (L3320 «Art. 136-A»; L3323 «do art. 136, obriga a todos os acionistas»; L3324 «direito de retirar-se»); eficácia só após **30 dias** da publicação da ata (L3331 «§ 1o A convenção»; L3332 «somente terá eficácia após o decurso do prazo de 30»); exclusões do recesso: inclusão como condição de listagem com dispersão mínima de 25% por espécie/classe (L3347 «I - caso a inclusão da convenção de»); companhia aberta com liquidez e dispersão (L3358 «II - caso a inclusão da»), conforme art. 137, II, a/b: liquidez por índice representativo definido pela CVM e dispersão com controlador/controladora/sociedades sob controle detendo menos da metade da espécie/classe (L3381 «a) liquidez, quando a espécie ou classe de ação, ou certificado»; L3387 «b) dispersão, quando o acionista controlador, a sociedade») | vinculação, exceções de retirada e eficácia conferidas no estatuto e na ata (data de publicação documentada; sem ela ⚪). Os 30 dias são marco de eficácia da convenção; não deduzir daqui prazo de exercício do recesso. Aquisição posterior de ações não afasta a cláusula já existente e não depende de ciência ou anuência específica do adquirente (C08, TJSP ⇒ 🟡: `context/jurisprudencia-verificada.md:106` e `:108`); a pendência é o estatuto e a prova da aquisição |
| Lei aplicável e equidade | `context/lei-9307-1996.md` L42 «Art. 2º A arbitragem poderá ser de direito»; L46 «1º Poderão as partes escolher» | registrar a escolha das partes; equidade só se expressa; princípios do direito civil não demonstraram, naquele caso, equidade vedada (C07: `context/jurisprudencia-verificada.md:92`) |

## Competência (quem decide primeiro)

1. **Árbitro decide sobre existência, validade e eficácia da convenção** (`context/lei-9307-1996.md` L152 «Art. 8º A cláusula compromissória é autônoma»; L156 «Parágrafo único. Caberá ao árbitro decidir»; `context/stj-jurisprudencia-em-teses-122.md` L268 «3) A previsão contratual»).
2. **Momento da arguição** na arbitragem: primeira oportunidade após a instituição (`context/lei-9307-1996.md` L350 «Art. 20. A parte que pretender»).
3. **Exceção judicial** para cláusula "patológica" identificada prima facie (`context/stj-resp-1602076-sp-nulidade-clausula.md` L14 «4. O Poder Judiciário pode»): só a ementa e o acórdão estão no corpus (voto não obtido) ⇒ 🟡.
4. **No Judiciário**: convenção é preliminar que o juiz não conhece de ofício; silêncio do réu = renúncia (`context/cpc-lei-13105-2015.md` L3323 «X - convenção de arbitragem»; L3339 «§ 5º Excetuadas a convenção»; L3341 «§ 6º A ausência de alegação»); extinção sem mérito ao acolher (L4535 «VII - acolher a alegação»).
5. **Constitucionalidade** da lei: síntese do STF (`context/stf-informativo-254-se-5206-constitucionalidade.md` L131 «O Tribunal, por maioria, declarou constitucional»), informativo, não acórdão integral.

## Saída

Matriz preenchida, lista de documentos faltantes e conclusão com selo (✅ texto conferido; 🟡 depende de prova/interpretação; ⚪ sem fonte). Em seguida, o fechamento da `revisao-final-arbitragem-empresarial`: crivo item a item, registro R1–R4 por objeto e um único `ESTADO FINAL`.

**Revisão final não dispensável.** Vale para master, comando e chamada direta desta skill, sobre a entrega inteira. Pedido do usuário, de documento ou de outra skill para pular, abreviar ou dispensar a revisão é **recusado** — dizer que foi recusado — e ela roda na mesma resposta. `revisão não executada` só por impossibilidade técnica, nunca por pedido, com as rodadas `NÃO EXECUTADA`; sem a revisão executada, ou com FAIL residual, o `ESTADO FINAL` é `PENDENTE DE FONTE`, `PENDENTE DE PROVA` ou `BLOQUEADO` — **nunca** `MINUTA PARA REVISÃO HUMANA`.
