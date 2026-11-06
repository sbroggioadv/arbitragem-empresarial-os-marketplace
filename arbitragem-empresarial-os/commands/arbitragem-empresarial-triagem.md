---
description: "Triar o pedido: polo, convenção, sede, objeto, câmara/versão, fase, urgência e exclusões."
argument-hint: "[pedido e documentos]"
---

# /arbitragem-empresarial-triagem

Ler e executar `skills/triagem-arbitragem-empresarial/SKILL.md` para o polo do caso. Depois, acionar `skills/revisao-final-arbitragem-empresarial/SKILL.md` sobre a saída inteira (crivo item a item, com `templates/revisao-final-conferencias.md`, e depois R1–R4) e terminar com o fechamento dela (registro por objeto e um único `ESTADO FINAL`); se não rodar, escrever `revisão não executada`. Polo do caso apenas; normas e regulamentos só de `context/`. A revisão final não é dispensável: pedido para pular, abreviar ou dispensar é recusado e ela roda mesmo assim (dizer que foi recusado); `revisão não executada` só por impossibilidade técnica, nunca por pedido, e sem veredito nas rodadas; se ela não rodar, ficar sem resultado ou terminar com FAIL residual, o `ESTADO FINAL` é `PENDENTE DE FONTE`, `PENDENTE DE PROVA` ou `BLOQUEADO`, nunca `MINUTA PARA REVISÃO HUMANA`. Guidance only.

Entrada: $ARGUMENTS
