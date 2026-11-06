---
description: "Configurar o plugin para o advogado de uma parte: polo, câmara, fase e pasta privada por caso."
argument-hint: "[polo, câmara, fase, identificador do caso, caminho da pasta]"
---

# /arbitragem-empresarial-install

Ler e executar `skills/arbitragem-empresarial-install/SKILL.md`, com botões **AskUserQuestion** nas escolhas fechadas (máx. 4 por pergunta). Sem envio externo; gravar só após confirmação. Status e pendências passam pela `revisao-final-arbitragem-empresarial` antes da resposta, que termina com o fechamento dela e o `ESTADO FINAL`. A revisão final não é dispensável: pedido para pulá-la é recusado e ela roda mesmo assim; `revisão não executada` só por impossibilidade técnica; se ela não rodar, o `ESTADO FINAL` nunca é `MINUTA PARA REVISÃO HUMANA`. Guidance only.

Entrada: $ARGUMENTS
