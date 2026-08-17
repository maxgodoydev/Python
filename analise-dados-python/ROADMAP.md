# Roadmap — Análise de Dados em Python

Pré-requisito: módulos 1–6 do repo `logica-programacao-python` concluídos
(especialmente comprehensions e manipulação de CSV/JSON puro). Sem isso,
pandas vira "copiar código do Stack Overflow sem entender".

## Módulo 1 — NumPy
- [ ] Arrays vs listas: por que numpy é mais rápido (vetorização, sem loop Python)
- [ ] Operações element-wise, broadcasting
- [ ] Indexação e slicing multidimensional
- [ ] Estatística básica com numpy (`mean`, `std`, `median`, `percentile`)

## Módulo 2 — Pandas básico
- [ ] `Series` vs `DataFrame`
- [ ] Leitura de CSV/Excel/JSON (`read_csv`, `read_excel`, `read_json`)
- [ ] Seleção: `.loc`, `.iloc`, filtros booleanos
- [ ] `groupby`, `agg`, `pivot_table`
- [ ] Reescrever o `desafio_02.py` (funcionários) inteiro em pandas — comparar linhas de código e legibilidade

## Módulo 3 — Limpeza de dados
- [ ] Valores nulos: `isna`, `dropna`, `fillna` — e **quando cada estratégia é apropriada** (não é sempre `dropna`)
- [ ] Duplicatas: `duplicated`, `drop_duplicates`
- [ ] Tipos de dados incorretos (`astype`, `pd.to_datetime`, `pd.to_numeric`)
- [ ] Outliers: identificação visual e por IQR/z-score
- [ ] Projeto: pegar um dataset público "sujo" (ex: Kaggle) e documentar cada decisão de limpeza e por quê

## Módulo 4 — Análise Exploratória (EDA)
- [ ] Estrutura de uma EDA: shape, dtypes, describe, valores únicos
- [ ] Correlação entre variáveis (`corr()`, matriz de correlação)
- [ ] Formulação de hipóteses a partir dos dados (antes de rodar qualquer teste)
- [ ] Projeto: EDA completa de um dataset, com conclusões escritas — não só gráficos

## Módulo 5 — Visualização
- [ ] Matplotlib: gráficos de linha, barra, dispersão, histograma
- [ ] Seaborn: heatmap de correlação, boxplot, pairplot
- [ ] Quando NÃO usar cada tipo de gráfico (ex: pizza para muitas categorias)
- [ ] Dashboard simples (Streamlit) a partir de um dos datasets já limpos

## Módulo 6 — Estatística (a etapa mais pulada por autodidatas — não pule)
- [ ] Medidas de tendência central e dispersão (o que cada uma esconde)
- [ ] Distribuições (normal, e por que ela é assumida com frequência sem verificar)
- [ ] Correlação ≠ causalidade — explicar com exemplo real dos seus próprios dados
- [ ] Teste de hipótese básico (teste t) — o que ele realmente responde
- [ ] Amostragem e viés de amostragem

## Módulo 7 — SQL (fundamento comum a análise E engenharia)
- [ ] `SELECT`, `WHERE`, `ORDER BY`, `LIMIT`
- [ ] `JOIN` (inner, left, right) — a maior fonte de erro de analistas juniores
- [ ] `GROUP BY` + `HAVING`
- [ ] Subqueries e CTEs (`WITH`)
- [ ] Window functions (`ROW_NUMBER`, `RANK`, `LAG`/`LEAD`)
- [ ] Conectar Python (pandas/sqlalchemy) a um banco real (Postgres/SQLite) e substituir um dos projetos de CSV por consulta SQL

## Módulo 8 — Projeto integrado
- [ ] Pipeline manual: ingestão (CSV/API) → limpeza → EDA → visualização → conclusão escrita
- [ ] Publicar como notebook (Jupyter) documentado, não só código solto

---

## ⚠️ Sobre "virar engenheiro de dados depois"

Isto aqui NÃO é o roadmap de engenharia de dados — é o de análise. Quando
você terminar este repositório, você vai saber extrair, limpar e interpretar
dados. Engenharia de dados exige um conjunto quase separado de habilidades
que este repo não cobre:

- Modelagem de banco de dados (normalização, schemas, índices)
- ETL/ELT e orquestração (Airflow, Dagster)
- Processamento distribuído (Spark)
- Data warehousing (BigQuery, Snowflake, Redshift)
- Infraestrutura e containers (Docker, e depois Kubernetes)
- Streaming (Kafka)

O módulo 7 (SQL) e a base de Python são o que realmente carrega de um
caminho para o outro. O resto — estatística, visualização, EDA — não é
usado no dia a dia de um engenheiro de dados. Quando chegar nesse ponto,
o correto é abrir um terceiro repositório (`engenharia-dados`) com um
roadmap próprio, não tentar espremer os dois aqui.

## Como executar

Cada módulo terá notebooks (`.ipynb`) e/ou scripts (`.py`) conforme o
conteúdo for sendo produzido. Ambiente recomendado:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install numpy pandas matplotlib seaborn jupyter
```
