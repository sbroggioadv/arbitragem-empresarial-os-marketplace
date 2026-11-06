# Índice do corpus local — Arbitragem Empresarial OS

Os excertos de lei, decreto e julgado capturados em 02/10/2026 trazem na primeira linha o identificador, a URL, a data de captura e o SHA-256 do texto-fonte; cada linha `[Ln]` reproduz a linha n da captura. Corpus capturado não certifica vigência nem tese. Os regulamentos e custas por câmara ficam em `context/packs/` (ver o `PACK.md` de cada câmara).

## Leis e decretos

`context/lei-9307-1996.md` · `context/cpc-lei-13105-2015.md` · `context/cc-lei-10406-2002.md` · `context/cdc-lei-8078-1990.md` · `context/clt-dl-5452-1943.md` · `context/cf-1988.md` · `context/lei-6404-1976.md` · `context/lei-11101-2005.md` · `context/lei-14133-2021.md` · `context/decreto-10025-2019.md` · `context/decreto-4311-2002-nova-york.md`

## Julgados — lista fechada

- `context/jurisprudencia-verificada.md`: lista fechada dos julgados citáveis, com a regra de citação. Nove julgados conferidos no inteiro teor (C01, C02, C04–C10, incorporados em 26/10/2026, acesso 25/10/2026), cada um com trecho literal, **O que decidiu** e **Nota do plugin (não citável)**; no fim, as fichas `stj-`/`stf-` de 02/10/2026. Não é cópia integral byte a byte. Julgado fora da lista ⇒ `PENDENTE DE FONTE`.
- `context/fontes-jurisprudencia.json`: manifesto dos nove brutos (URL oficial, data UTC da captura, SHA-256 do bruto e da resposta, SHA-256 do trecho). Os brutos ficam fora do plugin.
- Fichas literais de 02/10/2026 (`[Ln]`): `context/stj-resp-2179459-go-esclarecimentos-interrompem-prazo.md` (C01) · `context/stj-resp-1900136-sp-nulidade-90-dias-impugnacao.md` (C02) · `context/stj-cc-197434-sp-art-22a.md` (C04) · `context/stj-informativo-extraordinario-12-resp-2023615.md` (C05, informativo) · `context/stj-resp-1586383-mg-prova-antecipada.md` (C06) · `context/stj-resp-1602076-sp-nulidade-clausula.md` (C09) · `context/stj-agint-aresp-2729976-sp-anulatoria-controle-estrito.md` · `context/stj-agint-aresp-2880520-urgencia-pre-arbitragem.md` · `context/stj-agint-aresp-2933033-duas-vias-nulidade.md` · `context/stj-jurisprudencia-em-teses-122.md` · `context/stj-resp-1698730-sp-urgencia-pre-arbitral.md` · `context/stj-resp-1949566-sp-execucao-juizo-estatal.md` · `context/stj-resp-2166582-sc-nulidade-clausula.md` · `context/stj-resp-2215990-sp-dever-revelacao.md` · `context/stf-informativo-254-se-5206-constitucionalidade.md`

## Cálculo (conta aberta e scripts)

- `context/calculo-prazo-arbitral.md`: regra de contagem de cada regulamento, como rodar `scripts/calc_arbitragem_prazo.py`, catálogo de prazos, conta aberta e caso de referência resolvido à mão. Calendário da câmara e feriados da sede são sempre entrada.
- `context/calculo-custas-arbitrais.md`: tabela capturada do CAM-CCBC 2025 e valores fixos da RA 06/20 da CAMARB, como rodar `scripts/calc_arbitragem_custas.py`, conta aberta e caso de referência resolvido à mão.
- Dados dos scripts: `scripts/data/` (tabelas e regras com arquivo de origem, linha e data de captura).
