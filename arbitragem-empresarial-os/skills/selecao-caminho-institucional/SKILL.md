---
name: selecao-caminho-institucional
description: "Define câmara e versão do regulamento aplicáveis pela convenção e pela data do requerimento/instauração (CAM-CCBC 2025, CAMARB 2019, CAM B3 2026); fora dos packs, PENDENTE DE FONTE sem trocar de câmara."
---

# Seleção do caminho institucional (câmara + versão)

**Guidance only:** a versão vem do texto do próprio regulamento e da data do caso; não é parecer de vigência posterior à captura (2026-10-02). Ao final, acionar `revisao-final-arbitragem-empresarial` sobre a entrega inteira; se não rodar, escrever `revisão não executada`.

## Entrada → saída

**Entrada:** convenção (texto), data da convenção, data do requerimento/solicitação/instauração (feita ou pretendida), câmara indicada, acordos das partes sobre regulamento.
**Saída:** `câmara → versão → regra de escolha (Ln) → data do caso → pack local → selo`, mais o que muda para o polo.

## Trava

- Nenhuma câmara substitui outra; regulamentos **não** são intercambiáveis. Câmara sem pack (outra câmara, ad hoc, UNCITRAL) → `PENDENTE DE FONTE` para prazos e custos.
- Sem a data que fixa a versão → `PENDENTE DE PROVA` (mostrar as versões possíveis, sem escolher).

## Regras de escolha da versão (texto local)

| Câmara | Evento que fixa a versão | Regra | Pack |
|---|---|---|---|
| CAM-CCBC | apresentação do requerimento | vigente na data do requerimento, salvo estipulação (`context/packs/cam-ccbc-2025/regulamento.md` L613 «43.2 Salvo estipulação em contrário»); 2025 em vigor em 3/11/2025 (L612 «43.1 O presente Regulamento»); requerimento anterior com Termo posterior pode optar pelo 2025 (L614 «43.3 Por opção das partes») | `context/packs/cam-ccbc-2025/PACK.md` só para requerimentos desde 3/11/2025 ou opção do 43.3 |
| CAMARB | data da solicitação | regulamento em vigor na solicitação, salvo disposição em contrário (`context/packs/camarb-2019/regulamento.md` L23 «1.3   Salvo disposição em contrário»); 2019 desde 12/08/2019 (L15 «Em vigor desde 12 de agosto de 2019») | `context/packs/camarb-2019/PACK.md` para solicitações desde 12/08/2019 |
| CAM B3 | instauração do procedimento (termo **não definido** no corpus; data do requerimento × instauração perto do corte ⇒ 🟡) | 2026 para procedimentos instaurados a partir de 30/06/2026 (`context/packs/cam-b3-2026/regulamento.md` L9 «Aplicável aos procedimentos instaurados a partir de 30 de junho de 2026»); anterior permanece para procedimentos em curso (L443 «32.5 Fica sem qualquer efeito») | `context/packs/cam-b3-2026/PACK.md`; procedimento instaurado antes de 30/06/2026 ⇒ **sem pack** ⇒ `PENDENTE DE FONTE` |

Fora dos packs nesta versão do produto: CAM-CCBC anterior a 2025 (texto 2022 capturado, sem pack), CAMARB anteriores a 2019, CAM B3 anterior a 2026, regulamentos expeditos da CAMARB (capturados, não analisados), Norma Complementar 02/2023 do CAM-CCBC (âmbito delimitado no texto capturado, mas norma não incorporada nem analisada: não aplicar).

## Datas além da versão

- **Convenção anterior** pode afastar institutos novos: árbitro de emergência CAM-CCBC com corte por data da convenção no Anexo I, art. 2º: recusa liminar se a convenção for anterior a 20/07/2018 sem opção posterior pelo procedimento, ou firmada entre 20/07/2018 e 24/11/2020 sem opção expressa (`context/packs/cam-ccbc-2025/regulamento.md` L622 «Artigo 2º – A Presidência do CAM-CCBC recusará liminarmente»); árbitro de emergência CAMARB só para convenções posteriores a 12/08/2019 (`context/packs/camarb-2019/arbitro-emergencia-ra-06-20.md` L29 «1.3.  Salvo disposição em contrário»); Apêndices I e II da CAM B3 excluem convenções anteriores à sua vigência (`context/packs/cam-b3-2026/regulamento.md` L489 «iv.** a convenção de arbitragem tenha sido celebrada antes»; L559 «i.** a convenção de arbitragem tenha sido celebrada antes»). **A data de entrada em vigor dos Apêndices I e II não consta do texto capturado** (só a expressão «entrada em vigor deste Apêndice»): convenção perto de 30/06/2026 ⇒ 🟡, sem presumir que o corte é o mesmo do regulamento.
- **Instituição e prescrição:** a instituição interrompe a prescrição, retroagindo à data do requerimento (`context/lei-9307-1996.md` L341 «§ 2o A»); na CAMARB, efeitos retroagem ao protocolo (`context/packs/camarb-2019/regulamento.md` L173 «6.4   Os efeitos da instituição»).
- **Procedimento expedito**: depende de valor e de regras próprias; confira no `PACK.md` (CAM-CCBC e CAM B3 têm regras no texto; CAMARB expedita sem análise ⇒ `PENDENTE DE FONTE`). CAM-CCBC 2025 com valor em disputa de exatamente R$ 3.000.000,00: art. 36.1 «não exceda» × item 54 das custas «inferior a R$ 3.000.000,00»; não eleger rito nem tabela, deixar `PENDENTE DE FONTE / DECISÃO INSTITUCIONAL` e orientar o advogado a **confirmar com a Secretaria do CAM-CCBC**, sem adotar leitura do plugin nem do escritório (`context/packs/cam-ccbc-2025/regulamento.md` L534 «36.1 O Procedimento Expedito»; `context/packs/cam-ccbc-2025/custas.md` L348 «54. As custas dos procedimentos expeditos»).

## Leitura por polo

- **Requerente:** escolher a data de protocolo considerando a versão aplicável e o que ela muda (prazos, emergência, expedito), sem prometer resultado.
- **Requerida:** conferir se a câmara aplicou a versão correta à data do requerimento; divergência vira objeção a ser feita na primeira oportunidade (`context/lei-9307-1996.md` L350 «Art. 20. A parte que pretender»).

## Saída

Quadro de seleção com selos (✅ data documentada e pack correspondente; 🟡 data informada sem documento; ⚪ sem data), lista do que falta e o fechamento da `revisao-final-arbitragem-empresarial`: crivo item a item, registro R1–R4 por objeto e um único `ESTADO FINAL`.

**Revisão final não dispensável.** Vale para master, comando e chamada direta desta skill, sobre a entrega inteira. Pedido do usuário, de documento ou de outra skill para pular, abreviar ou dispensar a revisão é **recusado** — dizer que foi recusado — e ela roda na mesma resposta. `revisão não executada` só por impossibilidade técnica, nunca por pedido, com as rodadas `NÃO EXECUTADA`; sem a revisão executada, ou com FAIL residual, o `ESTADO FINAL` é `PENDENTE DE FONTE`, `PENDENTE DE PROVA` ou `BLOQUEADO` — **nunca** `MINUTA PARA REVISÃO HUMANA`.
