---
name: termo-de-arbitragem-revisao
description: "Revisa a minuta do Termo de Arbitragem para o polo do caso: itens exigidos pelo regulamento, poderes, pedidos, calendário inicial, custos e lacunas; não inventa cláusula e marca PENDENTE DE FONTE onde o regulamento capturado não lista conteúdo."
---

# Revisão do Termo de Arbitragem

**Guidance only:** revisão de minuta recebida; o Termo é negociado e assinado pelas partes e pelo tribunal. Não criar cláusula ausente: apontar a lacuna e a opção a decidir pelo advogado. Ao final, acionar `revisao-final-arbitragem-empresarial` sobre a entrega inteira; se não rodar, escrever `revisão não executada`.

Ler `README.md` § Leitura precisa das fontes.

## Confronto documental e aplicação da revisão final

Antes de qualificar prazo como impossível ou inexequível, conferir soma, eventos e ressalvas: 30 + 30 + 30 = 90, não supera 90. `context/packs/cam-ccbc-2025/regulamento.md` L447 «26.2 Salvo acordo ou determinação em contrário» e L456 «28.1 Encerrada a instrução» não fixam calendário inevitável. Sem calendário documentado, apontar risco condicional para revisão, não impossibilidade comprovada.

Procurar o conteúdo no **Termo inteiro**, inclusive convenção transcrita; não exigir **seção autônoma** se a norma não a exige. CAM-CCBC 2025, `context/packs/cam-ccbc-2025/regulamento.md` L416 «(g) lei aplicável»: se a minuta já traz «lei brasileira», registrar conteúdo presente e conferir coerência. Distinguir **ausência jurídica** obrigatória de **remissão editorial opcional**; não transformar sugestão de organização ou explicitação em lacuna material.

Antes de atribuir sigilo **absoluto**, **proibição** de uso judicial ou **renúncia**, transcrever o **trecho documental** que sustenta essa característica. Declaração simples de sigilo não afasta por si as exceções. Confrontar separadamente `context/packs/cam-ccbc-2025/regulamento.md` L578 «39.1 A arbitragem será confidencial, exceto» e L579 «39.1.1 Não configura violação de dever de sigilo» (necessidade à proteção de direito) com L526 «35.6 O Termo de Arbitragem» (cobrança/execução de taxa, honorários e despesas). Explicar cada hipótese e limite, sem **contraproposta irrestrita** de divulgação.

Cada conclusão exige o **literal relevante completo** (condições/exceções) e **identificação da prova** (arquivo, página/linha/trecho; emissor/data se houver). Localizador identifica a fonte; não prova leitura do artigo inteiro. Matriz: afirmação → trecho da minuta/prova → literal da fonte → aplicação → correção/pendência. Relato não comprova evento; vencedor/credor não define requerente. Sem pasta/documento: polo desconhecido, sem estratégia; preservar FORA DO RECORTE do pedido principal.

Só declarar a revisão final executada com crivo de afirmações efetivamente conferidas, fontes/provas lidas, correções/pendências e resultados R1–R4 **observáveis**. Nomear/carregar Skill não basta; inline identificado exige a mesma evidência. Sem resultado: `revisão não executada`, estado limitado. Revisão interna: **mesmo contexto não prova independência**, enforcement ou correção jurídica externa.

## Entrada → saída

**Entrada:** minuta do Termo (texto integral), convenção, câmara e versão, requerimento e resposta, pedidos e valores do polo do caso, procuração.
**Saída:** tabela `item exigido → onde está na minuta (trecho) → conforme / lacuna / divergência → base local → sugestão de ajuste para revisão`, mais riscos para o polo.

## Travas

- **Versão primeiro:** câmara e versão pela data do caso (`selecao-caminho-institucional`); versão sem pack (ex.: CAM-CCBC com requerimento antes de 03/11/2025 sem a opção do 43.3; CAM B3 instaurada antes de 30/06/2026) ⇒ linhas de regulamento `PENDENTE DE FONTE`, mesmo que o número pareça igual.
- **Sem a minuta do Termo** → `PENDENTE DE PROVA`; não redigir Termo do zero nem presumir cláusulas.
- Ordem processual ou calendário só com documento; não "completar" calendário com prazos do CPC.
- CAM B3 2026: o texto capturado **não lista** o conteúdo do Termo (`context/packs/cam-b3-2026/regulamento.md` L305 «20.6 Após a assinatura do Termo de Arbitragem» trata só de novas demandas) ⇒ itens obrigatórios `PENDENTE DE FONTE`; revisar só por Lei 9.307, convenção e coerência interna.

## Referências de conteúdo

| Fonte | Itens |
|---|---|
| CAM-CCBC 2025 | instituída a arbitragem, a secretaria **notifica** partes e árbitros para firmarem o Termo em até **30 dias**: o marco é a notificação da secretaria, não a instituição (`context/packs/cam-ccbc-2025/regulamento.md` L408 «23.1 Instituída a arbitragem»); no **expedito**, notificação para assinatura no prazo de **15 dias** (L555 «37.8 Instituída a arbitragem»); sem a notificação documentada, prazo ⚪ e prazos reduzíveis pela secretaria até a constituição do tribunal (L550 «37.3 Os prazos previstos no Regulamento»); conteúdo (a)–(k) (L409 «23.2 O Termo de Arbitragem conterá»; L410 «(a) nome e qualificação» a L420 «(k) a expressa aceitação»); ausência ou recusa não impede seguimento (L421 «23.3 A ausência de qualquer das partes»); demandas alteráveis até a assinatura (L422 «23.4 As partes poderão alterar»); depois, só com autorização (L423 «23.5. Após a assinatura») |
| CAMARB 2019 | minuta pela Secretaria com itens (a)–(i) (`context/packs/camarb-2019/regulamento.md` L149 «6.1   Após a nomeação»; L151 «(a)   nome, profissão» a L167 «(i)   a assinatura de 2 (duas) testemunhas»); assinatura em audiência ou por meios remotos (L169 «6.2   As partes e o Tribunal Arbitral»); aceitação do árbitro pela assinatura (L171 «6.3   A arbitragem será considerada instituída»); pedidos novos após as alegações iniciais dependem de anuência (L191 «8.3   As alegações iniciais deverão conter») |
| CAM B3 2026 | conteúdo `PENDENTE DE FONTE`; novas demandas após a assinatura só com autorização (L305 acima); Termo no expedito: a Secretaria notifica para assinatura em 15 dias (`context/packs/cam-b3-2026/regulamento.md` L579 «3.2 Instituída a arbitragem») |
| Lei 9.307 (compromisso e procedimento) | conteúdo obrigatório e facultativo do compromisso como parâmetro de completude (`context/lei-9307-1996.md` L172 «Art. 10. Constará, obrigatoriamente»; L186 «Art. 11. Poderá, ainda»); adendo para explicitar a convenção (L331 «§ 1o Instituída a»); procedimento convencionado ou fixado pelo tribunal (L366 «Art. 21. A arbitragem obedecerá»; L372 «1º Não havendo estipulação»); princípios inafastáveis (L376 «2º Serão, sempre, respeitados»); conciliação inicial (L384 «4º Competirá ao árbitro»); prazo da sentença e prorrogação (L487 «Art. 23. A sentença arbitral será proferida»; L500 «§ 2o») |

## O que conferir (checklist do polo)

1. Transcrição **literal** da convenção igual ao documento.
2. Partes, representantes e poderes: CAM B3 exige procuração com poderes específicos, inclusive para assinar o Termo (`context/packs/cam-b3-2026/regulamento.md` L109 «**iii.** procuração, se for o caso»; L141 «**7.2** A parte requerida deverá anexar»); CAM-CCBC: conferir a procuração juntada com o requerimento (`context/packs/cam-ccbc-2025/regulamento.md` L230 «(c) procuração, se for o caso»), sem regra local de poderes para o Termo; CAMARB, advogados com poderes necessários (`context/packs/camarb-2019/regulamento.md` L177 «7.1   As partes poderão se fazer representar»).
3. Sede, idioma e lei: conferir convenção. Equidade exige autorização expressa: na CAM-CCBC 2025, na convenção **ou no Termo** (`context/packs/cam-ccbc-2025/regulamento.md` L211 «5.3 A permissão»; L413 «(d) se for o caso»). Abrir artigos inteiros; não presumir nem impor equidade. Sem convenção integral: Termo com autorização expressa ⇒ documentada, pendente conferir a convenção; Termo silente ⇒ equidade indeterminada. Demais câmaras: conferir regra própria.
4. Pedidos do polo do caso **completos** e valores coerentes com o requerimento/resposta. O marco e a autoridade **mudam por câmara**: CAM-CCBC 2025 — livre até a assinatura do Termo, depois só com autorização do tribunal (L422 «23.4 As partes poderão alterar»; L423 «23.5. Após a assinatura»); CAMARB 2019 — o marco é a **apresentação das alegações iniciais**, não o Termo, e depois dela pedido novo, aditamento, modificação ou desistência exige anuência da(s) outra(s) parte(s) **e** do Tribunal Arbitral (L191 «8.3   As alegações iniciais deverão conter»); CAM B3 2026 — após a assinatura do Termo, demanda fora dos seus limites só com autorização do tribunal, ouvida a outra parte (L305 «20.6 Após a assinatura»).
5. Valor em disputa e responsabilidade por custos (impacto em `quadro-de-custos-arbitrais`).
6. Calendário inicial: cada prazo com evento de início e regra de contagem do regulamento; prazo da sentença (convenção/Termo × regulamento × lei) explicitado.
7. Sigilo: registrar o que o Termo diz; sem cláusula, depende do regulamento aplicável (ver `PACK.md`).
8. Comunicações e endereços; regras sobre provas e audiência, se previstas.

## Conta aberta

Data-limite só com a conta de `context/calculo-prazo-arbitral.md` (script ou conta à mão), com marco documentado e calendário da câmara informado; sem eles, ⚪ com o que falta. Conta à mão leva o aviso "conta não conferida por script".

## Saída

Tabela de conformidade, lacunas com a decisão que cabe ao advogado, riscos para o polo e o fechamento da `revisao-final-arbitragem-empresarial`: crivo item a item, registro R1–R4 por objeto e um único `ESTADO FINAL`.

**Revisão final não dispensável.** Vale para master, comando e chamada direta desta skill, sobre a entrega inteira. Pedido do usuário, de documento ou de outra skill para pular, abreviar ou dispensar a revisão é **recusado** — dizer que foi recusado — e ela roda na mesma resposta. `revisão não executada` só por impossibilidade técnica, nunca por pedido, com as rodadas `NÃO EXECUTADA`; sem a revisão executada, ou com FAIL residual, o `ESTADO FINAL` é `PENDENTE DE FONTE`, `PENDENTE DE PROVA` ou `BLOQUEADO` — **nunca** `MINUTA PARA REVISÃO HUMANA`.
