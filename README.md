# Arbitragem Empresarial OS

Marketplace do plugin **arbitragem-empresarial-os** (versão 0.1.0), da Sbroggio Advocacia & IA Combativa. Apoio ao advogado de **uma parte** — requerente **ou** requerida — em arbitragem empresarial com sede no Brasil: enquadramento, convenção, câmara e versão do regulamento, tribunal e Termo, prova e audiência, sentença e apoio judicial. Escopo e limites no [README do plugin](arbitragem-empresarial-os/README.md).

**18 skills** em 6 camadas · 18 comandos · fontes locais: Lei 9.307/1996 e dispositivos conexos, regulamentos CAM-CCBC 2025, CAMARB 2019 e CAM B3 2026, tabela de custas do CAM-CCBC 2025 e uma lista fechada de nove julgados conferidos.

Produto vendido sob licença de uso: o código está em repositório público para viabilizar a instalação, mas não é software livre. Condições em [LICENSE](LICENSE) (a mesma licença está em `arbitragem-empresarial-os/LICENCA`).

## Instalação

- **Claude Desktop (Cowork):** Personalização → Plugins → Adicionar → Adicionar marketplace → Adicionar de um repositório → `https://github.com/sbroggioadv/arbitragem-empresarial-os-marketplace` → Sincronizar; depois instale **arbitragem-empresarial-os** em Plugins.
- **Claude Code:** `claude plugin marketplace add sbroggioadv/arbitragem-empresarial-os-marketplace` e `claude plugin install arbitragem-empresarial-os@arbitragem-empresarial-os-marketplace`.

Instale pela interface do Cowork: a interface e a linha de comando têm listas de marketplace separadas. Não instale por upload de ZIP.

Depois de instalar, rode `/arbitragem-empresarial-install` e conduza o caso por `/arbitragem-empresarial-master`.

## O que cobre

- **Advogado da requerente:** convenção, câmara e versão, requerimento, custos pela linha da tabela, árbitros, urgência antes do tribunal e instrução, com cada prazo ligado à fonte e ao evento.
- **Advogado da requerida:** resposta e objeção de competência no canal do regulamento, impugnações, revisão do Termo, provas e defesa contra a sentença pelas vias legais.

## O que não cobre

- Atuar como árbitro, secretário ou câmara; arbitragem com sede no exterior, homologação de sentença estrangeira e arbitragem de investimento.
- Consumo, trabalho individual, insolvência em si, família e o procedimento próprio de entes públicos (só o enquadramento pelo texto legal).
- Custos gerais da CAMARB e da CAM B3 e câmaras ou versões sem pack: ficam `PENDENTE DE FONTE`.

## Como o plugin evita inventar

Prazo, custo, artigo, item de regulamento e julgado só entram com o arquivo de `context/` e a linha do texto capturado. Toda entrega termina na revisão final única: crivo item a item contra a fonte e, depois, R1 a R4. É instrução ao modelo, não trava técnica, e não substitui a conferência do advogado. Estados finais: `MINUTA PARA REVISÃO HUMANA` · `PENDENTE DE PROVA` · `PENDENTE DE FONTE` · `BLOQUEADO` · `FORA DO RECORTE`.

Custas e datas-limite saem de scripts locais (`arbitragem-empresarial-os/scripts/`, Python só com a biblioteca padrão, sem rede), com a regra e a fonte de cada número; sem Python, a conta aparece aberta, com o aviso de que não foi conferida por script. Calendário da câmara e feriados da sede são sempre informados pelo advogado.

Verificado localmente por linha de comando com casos fictícios; **não foi testado no Cowork nativo**.

Suporte: **luis@sbroggio.io**.
