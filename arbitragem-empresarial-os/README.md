# Arbitragem Empresarial OS

`arbitragem-empresarial-os` · versão 0.1.0 · Sbroggio Advocacia & IA Combativa · suporte: **luis@sbroggio.io**

Plugin para o **advogado de uma parte** — requerente **ou** requerida — em arbitragem empresarial com sede no Brasil. Cobre o percurso enquadramento → instituição → tribunal e Termo → prova e audiência → sentença → apoio judicial, com cada prazo, custo e procedimento ligado a uma fonte local e a um evento (lei, convenção, regulamento e versão, Termo ou ordem).

## Instalação pelo marketplace

A distribuição é pelo **marketplace GitHub público**, no modelo da família IA Combativa: `https://github.com/sbroggioadv/arbitragem-empresarial-os-marketplace`.

- **Cowork (Claude Desktop):** Personalização (pode aparecer como Customize) → **Plugins** → **+ Adicionar** → **Adicionar marketplace** → **Adicionar de um repositório** → cole a URL acima, deixe *Sincronizar automaticamente* ligado e clique em **Sincronizar**. Depois, em **Plugins › Meus**, localize `arbitragem-empresarial-os` e instale.
- **Claude Code:** `claude plugin marketplace add sbroggioadv/arbitragem-empresarial-os-marketplace` e `claude plugin install arbitragem-empresarial-os@arbitragem-empresarial-os-marketplace`. No Claude Code os comandos levam o prefixo do plugin, como `/arbitragem-empresarial-os:arbitragem-empresarial-install`.
- Não instale por upload de ZIP no Cowork nem distribua ZIP do plugin ao cliente como forma de instalação: há histórico de rejeição opaca ("Plugin validation failed") na família. O pacote do produto (manual em PDF e capa) não instala o plugin.

**O plugin não foi testado no Cowork nativo**: foi verificado localmente por linha de comando com casos fictícios. A renderização dos botões e o comportamento no app dependem do ambiente. Se a instalação falhar, registre a mensagem e peça suporte a **luis@sbroggio.io**.

Separe os documentos por cliente, matéria e polo em uma pasta privada de trabalho, fora do código do plugin. A organização local não certifica sigilo: confira as condições do provedor antes de inserir dados. Use sempre a mesma pasta privada de trabalho para preservar o contexto, mantendo os casos e polos separados em subpastas. Depois da instalação, use `/arbitragem-empresarial-install` para configurar o caso.

Referências técnicas de apoio: [plugins no Claude](https://support.claude.com/en/articles/13837440-use-plugins-in-claude) e [plugins no Claude Code](https://code.claude.com/docs/en/plugins). Uso sujeito à LICENCA e à revisão do advogado.

## Portas

- `/arbitragem-empresarial-install` — configura polo, câmara, fase e a pasta privada do caso (`caso/<id>/<polo>/`), com botões nas escolhas fechadas.
- `/arbitragem-empresarial-master` — conduz o caso: triagem, skill produtora certa, cronologia única e revisão integral.
- `/arbitragem-empresarial-revisar` e um comando por etapa (`-triagem`, `-arbitrabilidade`, `-convencao`, `-caminho`, `-requerimento`, `-resposta`, `-custos`, `-arbitros`, `-termo`, `-urgencia`, `-calendario`, `-provas`, `-audiencia`, `-sentenca`, `-apoio`).

Master, comandos e skills chamadas diretamente são **instruídos** a fechar a entrega pela `revisao-final-arbitragem-empresarial`, uma revisão única que abre com o crivo item a item (cada fato, norma, item e versão de regulamento, prazo, custo e precedente contra o `context/` ou o documento do caso) e depois roda R1–R4; a recusar pedido para pular essa revisão; e a mostrar o crivo, o registro por rodada e o `ESTADO FINAL`. É instrução ao modelo, não trava técnica: confira o crivo em cada resposta; sem a revisão final executada, a saída não pode ser `MINUTA PARA REVISÃO HUMANA`. O único hook é o aviso de início de sessão; nenhum hook grava, bloqueia ou certifica entrega. Toda saída termina em um estado: `MINUTA PARA REVISÃO HUMANA`, `PENDENTE DE PROVA`, `PENDENTE DE FONTE`, `BLOQUEADO` ou `FORA DO RECORTE`.

## Skills (18)

Chassi: `arbitragem-empresarial-install`, `arbitragem-empresarial-master`, `triagem-arbitragem-empresarial`, `revisao-final-arbitragem-empresarial`.
Enquadramento: `matriz-arbitrabilidade-competencia`, `analise-convencao-arbitral`, `selecao-caminho-institucional`.
Instituição: `requerimento-de-arbitragem`, `resposta-e-impugnacao-de-competencia`, `quadro-de-custos-arbitrais`.
Tribunal e Termo: `indicacao-e-impugnacao-de-arbitros`, `termo-de-arbitragem-revisao`, `emergencia-e-urgencia-pre-tribunal`.
Instrução: `calendario-e-ordens-processuais`, `pedidos-provas-e-pecas-arbitrais`, `preparacao-de-audiencia-arbitral`.
Encerramento: `esclarecimento-e-correcao-da-sentenca`, `apoio-e-interface-judicial-arbitragem`.

## Fontes locais (`context/`)

Excertos literais de fontes oficiais capturadas em 2026-10-02: Lei 9.307/1996 (texto compilado), dispositivos do CPC, CC, CDC, CLT, CF, Leis 6.404, 11.101 e 14.133, Decretos 10.025/2019 e 4.311/2002, e ementas/sínteses de julgados do STJ e do STF. Cada arquivo traz no topo o identificador, a URL, a data de captura e o sha256 do texto-fonte; cada linha `[Ln]` reproduz a linha n do texto capturado.

Julgados citáveis: lista fechada em `context/jurisprudencia-verificada.md` (nove julgados conferidos no inteiro teor em 25/10/2026 e as fichas do corpus), com a regra de citação: aspas só no trecho literal com arquivo e linha, mais a linha "O que decidiu"; a "Nota do plugin" nunca é resultado do julgado; julgado fora da lista ⇒ `PENDENTE DE FONTE`. Manifesto com SHA-256 dos brutos em `context/fontes-jurisprudencia.json`; índice em `context/INDICE.md`.

Packs por câmara e versão (`context/packs/`):

| Pack | Conteúdo | Custos |
|---|---|---|
| `cam-ccbc-2025` | Regulamento 2025 (vigor 03/11/2025) e Regramento de Custas 2025 | tabela textual — quadro com linha da tabela e segunda conta |
| `camarb-2019` | Regulamento 2019 (vigor 12/08/2019) e Resolução Administrativa 06/20 (árbitro de emergência) | `PENDENTE DE FONTE` (tabela de custas capturada, mas não incorporada nem analisada nesta versão), salvo os valores fixos da RA 06/20 |
| `cam-b3-2026` | Regulamento 2026 com Apêndices I e II (procedimentos instaurados desde 30/06/2026) | `PENDENTE DE FONTE` (página de custas sem versão declarada) |

## O que o plugin NÃO faz

- Não é parecer jurídico, não substitui o advogado responsável e não promete resultado.
- Não representa as duas partes; troca de polo abre caso novo sem copiar memória; atuar pelo polo oposto na mesma disputa é bloqueado.
- Não atua como árbitro, secretário ou câmara; não trata arbitragem com sede no exterior, homologação de sentença estrangeira nem arbitragem de investimento (`FORA DO RECORTE`).
- Não trata consumo, contrato individual de trabalho, insolvência em si, estado/família nem o procedimento específico de entes públicos (`FORA DO RECORTE` após o enquadramento pelo texto legal).
- Não estima custo "de cabeça" nem usa tabela de outra câmara; não aplica o calendário do CPC sem norma, convenção, Termo ou ordem que o determine; não promete sigilo sem fonte.
- Não consulta câmaras, tribunais ou a internet em tempo real; vigência posterior à captura não é verificada.
- Não envia autos nem dados de clientes a serviço externo.

## Bloqueios por fonte nesta versão

Nenhuma skill inteira está bloqueada; ficam `PENDENTE DE FONTE` (sem pack ou sem número):

- custos CAMARB e custos CAM B3;
- CAM B3 para procedimentos instaurados antes de 30/06/2026 (regulamento anterior sem pack);
- CAM-CCBC para requerimentos anteriores a 03/11/2025 sem a opção de transição do art. 43.3 (regulamento 2022 sem pack);
- regulamentos expeditos da CAMARB; conteúdo do Termo de Arbitragem na CAM B3 2026 (o texto capturado não o lista);
- Norma Complementar 02/2023 do CAM-CCBC (societária): o texto capturado delimita o âmbito, mas a norma não foi incorporada nem analisada nesta versão — não aplicada;
- jurisprudência por matéria além das teses de 2019 e inteiro teor de julgados disponíveis só em ementa ou informativo (usados com 🟡).

## Estado de teste

Verificado localmente: estrutura (limites de tamanho, front-matter, hook só com `echo`), conferência literal de cada `[Ln]` contra o texto capturado e de cada localizador citado nas skills, e cenários fictícios executados por linha de comando. **Não foi testado no Cowork nativo** (instalação pelo marketplace, botões, hooks e backend). Uso sujeito à [LICENCA](LICENCA) e à revisão do advogado.

## Leitura precisa das fontes

**Guidance only, mesmo contexto/modelo.** Antes da aplicação, ler este guia. Índices e offsets de `Read` são **linhas físicas do arquivo**, não os números `[Ln]` da captura. Localizar o `[Ln]` ou ID por `Grep`, obter a posição física e abrir o dispositivo inteiro com sua continuação, condições, incisos e exceções. Match isolado, arquivo parcial, resultado vazio ou trecho não aberto **não prova ausência** nem leitura integral. Registrar na matriz pública o arquivo, intervalo físico realmente aberto, `[Ln]` correspondente e limite de leitura; não apresentar memória do modelo como fonte.

- Antes de **cada Read com offset**, executar **Grep com números de linhas físicas** no arquivo exato. Usar a posição física retornada, nunca o número do label `[Ln]`.
  Abrir até o fim do dispositivo, incluindo alíneas; paginação, `Omitted long line` ou resultado vazio exige nova abertura.
- Conferir a cobertura **por artigo e subitem**, do início ao fim, contra os retornos efetivamente recebidos: caput, parágrafos, incisos, alíneas e continuações. Trechos de buscas diferentes podem completar a leitura, mas identificar eventuais lacunas; ter lido o caput não autoriza dizer “artigo inteiro”. Isso vale também para artigos mencionados em encaminhamentos. Se faltar trecho, completar a leitura ou retirar a referência normativa e declarar a limitação, sem alegar integralidade.
- Antes de publicar cada localizador, conferir que o literal pertence ao arquivo e ao `[Ln]` indicado. Rotular separadamente **linhas físicas** e **labels da captura**; não converter um intervalo físico em `L...`. O localizador de item vizinho não sustenta o claim.
- Lei invocada precisa ser aberta: artigo inteiro, parágrafos e incisos. **Não citar artigo sem abertura integral**, nem com selo 🟡.
  Se não abrir, retirar o claim normativo; texto de skill ou tabela não substitui a norma. Para CAM-CCBC, abrir 43.1–43.3 inteiros: 43.2 é a regra na data do requerimento; 43.3 é opção de transição para os anteriores, com Termo posterior à vigência (`context/packs/cam-ccbc-2025/regulamento.md` L612 «43.1 O presente Regulamento»; L613 «43.2 Salvo estipulação»; L614 «43.3 Por opção das partes»). Não substituir essa leitura pela tabela da revisão final.
- Documento não juntado ou não aberto é **não comprovado**, não inexistente. Sem comprovante de protocolo/comunicação, escrever **protocolo/comunicação não comprovado**.
  Não converter isso em “não protocolado”, “não ocorrido” ou “inexistente”, inclusive no residual e no fechamento da revisão final. Abrir o documento antes de afirmar seu polo; declaração expressa de cliente requerida não se converte em requerente por vitória ou crédito. Documento residual de polo oposto pode ser identificado, sem uso de estratégia nem troca de representação.
- Sentença estrangeira e homologação continuam `FORA DO RECORTE`; fase pós-sentença não prova ausência de urgência. O art. 37 está no contexto distribuído (`context/lei-9307-1996.md` L711 «Art. 37. A homologação de sentença arbitral estrangeira» a L721 «de tradução oficial.»). Ler o art. 37 inteiro e manter **dois objetos separados** na matriz:
  **I — sentença:** original ou cópia devidamente certificada, autenticada pelo consulado brasileiro e acompanhada de tradução oficial.
  **II — convenção:** original ou cópia devidamente certificada, acompanhada de tradução oficial.
  O inciso II **não exige textualmente autenticação consular**; não usar “na mesma forma” nem transferir requisito do I ao II. Essa presença **não homologa**, não torna peça pronta nem amplia o rito do STJ; preservar a remissão histórica ao CPC como capturada. `context/decreto-4311-2002-nova-york.md` distribui só art. 1º do Decreto; a Convenção está no corpus integral privado capturado, sem incorporação/análise integral nesta versão. Dizer **não incorporada/analisada integralmente no contexto distribuído**.
  Nunca afirmar ausência no corpus privado inacessível: falta no contexto não prova falta na captura privada.
- Para qualquer fonte, distinguir **não consultada nesta sessão**, **não localizada na busca descrita**, **não incorporada ao contexto distribuído** e **ausente do corpus**. Declarar o alcance efetivamente verificado; a última conclusão exige conferência do corpus pertinente e de seu inventário. Sem acesso ou busca suficiente, não generalizar a ausência nem inferir a presença; manter a pendência de fonte ou de análise e o encaminhamento cabível.
- Conferir separadamente cada condição cumulativa, preservando alternativas e exceções do literal. Atendimento parcial não equivale a item completo: em `context/packs/cam-ccbc-2025/regulamento.md` L227 «7.1. A parte que desejar iniciar» e L234 «(g) propostas ou outras informações relevantes», o conteúdo do requerimento exige confronto próprio do número e escolha dos árbitros, ou da indicação acordada; prever apenas o número na cláusula não comprova o restante do requerimento. Descrever o conteúdo presente e a pendência sem presumir invalidade da convenção.
- Distinguir **minuta preparatória não assinada**, **ato futuro proposto** e **ato documentado**. Campo a preencher ou presidente a indicar pode ser pendência para assinatura, sem provar inversão de fase consumada. Para afirmar violação da sequência institucional, identificar o ato efetivamente praticado, sua prova e a regra integral aplicável; se faltarem, formular condição ou risco, sem inventar ocorrência.
- Atraso da sentença exige ler a ressalva completa do art. 12, III: prazo expirado **e** notificação do árbitro ou presidente, concedendo-lhe dez dias para prolação e apresentação (`context/lei-9307-1996.md` L223 «III - tendo expirado o prazo»; L224 «interessada tenha notificado o árbitro»; L225 «concedendo-lhe o prazo de dez dias»; L226 «arbitral.»); confrontar art. 32, VII, sem nulidade automática (`context/lei-9307-1996.md` L620 «VII - proferida fora do prazo»). Soma de etapas não substitui calendário e prova da notificação.

No crivo da revisão final, publicar a matriz: **ID → claim final → tipo → arquivo → intervalo físico e Ln lidos → trecho literal → aplicação → correção/pendência**.
Toda afirmação material, inclusive ficha e residual, recebe ID. Contadores são derivados dos IDs publicados, sem totais autoalegados.
Conferir IDs únicos e objetos efetivamente revisados antes de totalizar; repetição de fonte ou do mesmo objeto em outra rodada não cria afirmação adicional. Uma retirada/correção exige ID, proposição anterior concreta e destino (retirada ou redação corrigida); prevenção genérica de erro não conta como correção realizada. Sem contagem conferida, declarar que não foi conferida, sem estimar total nem inventar IDs para fechá-lo.
Publicar R1–R4 **por objeto/IDs**, com achado, prova, veredito, correção e residual; declarar “não aplicável” com motivo quando não houver objeto.

A revisão final pode aplicar-se **inline no mesmo contexto**, com o corpo carregado e resultados observáveis. Este guia não impõe agentes separados, piso de veredictos, independência ou garantia de comportamento.
