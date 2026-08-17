# 🗺️ Roadmap — Trilha de Análise & Ciência de Dados em Python

Este roadmap descreve a evolução teórica e prática para a trilha de **Dados, Analytics e BI**, mapeada em conjunto com o índice de 40 desafios do repositório.

> **Pré-requisito:** Conclusão dos Módulos 1 e 2 de Lógica de Programação (Desafios 01 a 20 — em especial manipulação de estruturas brutas, funções, tratamento de exceções e consumo de arquivos/APIs). Sem essa base de Python puro, bibliotecas como Pandas e NumPy tornam-se apenas "código copiado sem entendimento do fluxo".

---

## Módulo 1 — Vetorização e Fundamentos Estatísticos com NumPy
*Conexão com os Desafios 21 e 22*

- [ ] **Arrays vs Listas Nativas:** Entendimento de alocação de memória e por que o NumPy é performático (vetorização em C vs loops Python).
- [ ] **Broadcasting e Operações Element-wise:** Manipulação matricial sem a necessidade de laços `for`.
- [ ] **Indexação e Fatiamento Multidimensional:** Seleções avançadas, máscaras booleanas e fatiamentos de matrizes.
- [ ] **Estatística Computacional:** Cálculo de média, mediana, desvio padrão, variância e percentis via `np.mean`, `np.std`, `np.percentile`.

---

## Módulo 2 — Manipulação Estruturada com Pandas
*Conexão com os Desafios 23 a 25*

- [ ] **Estruturas Fundamentais:** Análise anatômica de `Series` e `DataFrames`.
- [ ] **Ingestão de Dados:** Leitura e otimização de arquivos `CSV`, `Excel`, `JSON` e `Parquet`.
- [ ] **Indexação Selecionada:** Uso correto de `.loc[]`, `.iloc[]` e filtros por condições múltiplas.
- [ ] **Reescrita Refatorada:** Pegar um desafio de lógica (ex: `desafio_02.py`) e reescrevê-lo completamente usando Pandas para comparar performance e legibilidade.

---

## Módulo 3 — Limpeza e Higienização de Dados (Data Cleaning)
*Conexão com os Desafios 25 a 27*

- [ ] **Tratamento de Nulos:** Estratégias de eliminação (`dropna`) e imputação (`fillna` via média, mediana ou regras de negócio) — definindo critérios técnicos para não enviesar a base.
- [ ] **Deduplicação e Tipagem:** Mapeamento de duplicatas (`duplicated`, `drop_duplicates`) e conversão de tipos com `astype`, `pd.to_datetime` e `pd.to_numeric`.
- [ ] **Transformações RÁPIDAS:** Aplicação de funções customizadas e expressões `lambda` com `.apply()`.
- [ ] **Detecção de Outliers:** Identificação por IQR (Intervalo Interquartil) e Z-Score.

---

## Módulo 4 — Agregações, Cruzamentos e Séries Temporais
*Conexão com os Desafios 27 a 30*

- [ ] **Agrupamentos e Tabelas Dinâmicas:** Operações com `.groupby()`, `.agg()` e `.pivot_table()`.
- [ ] **Junções e Relacionamentos:** Combinação de datasets via `merge` (Inner, Left, Right, Outer), `concat` e `join`.
- [ ] **Séries Temporais:** Análise de sazonalidade, reamostragem (`resample`), janelas móveis (`rolling`) e fatiamento por datas.
- [ ] **Exportação Performática:** Persistência de dados tratados em `CSV`, `Excel` e formato compacto `Parquet`.

---

## Módulo 5 — Análise Exploratória de Dados (EDA)
*Conexão com os Desafios 36 e 37*

- [ ] **Estruturação de EDA:** Inspeção de granularidade, `shape`, `dtypes`, distribuições e métricas descritivas (`describe`).
- [ ] **Análise de Correlação:** Avaliação de dependências entre variáveis numéricas (`.corr()`).
- [ ] **Formulação e Validação de Hipóteses:** Definição prévia de perguntas de negócio antes da execução dos testes nos dados.
- [ ] **Relatórios de Descobertas:** Documentação de cenários, anomalias e recomendações estratégicas baseadas em fatos extraídos da análise.

---

## Módulo 6 — Visualização e Storytelling de Dados
*Conexão com os Desafios 31 e 32*

- [ ] **Matplotlib:** Gráficos customizados de linha, barra, dispersão, histogramas e controle de múltiplos eixos.
- [ ] **Seaborn:** Análises estatísticas visuais com `heatmap`, `boxplot`, `violinplot` e `pairplot`.
- [ ] **Design de Informação:** Escolha do gráfico correto para cada tipo de dado e remoção de poluição visual.

---

## Módulo 7 — Integração SQL & Persistência Relacional
*Conexão com os Desafios 33 e 34*

- [ ] **Consultas Estruturadas:** `SELECT`, `WHERE`, `ORDER BY`, `LIMIT`.
- [ ] **Junções em Banco:** `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN` e tratamento de ambiguidades.
- [ ] **Agregações Avançadas:** `GROUP BY`, `HAVING` e Funções de Agregação.
- [ ] **Subqueries e CTEs:** Uso de `WITH` para modularização de queries complexas.
- [ ] **Window Functions:** `ROW_NUMBER()`, `RANK()`, `LEAD()`, `LAG()`.
- [ ] **Conectividade Python + SQL:** Integração de `SQLite3` e `SQLAlchemy` para consultar bancos relacionais diretamente em DataFrames do Pandas.

---

## Módulo 8 — Pipelines ETL, Dashboards e Entregáveis
*Conexão com os Desafios 35, 38, 39 e 40*

- [ ] **Arquitetura ETL:** Ingestão (API/SQL/Files) → Transformação/Regra de Negócio → Carga.
- [ ] **Automação de Relatórios:** Geração automatizada de entregáveis técnicos (PDF / HTML).
- [ ] **Dashboards Interativos:** Criação de interfaces web dinâmicas usando **Streamlit**.
- [ ] **Projeto Integrador (End-to-End):** Resolução de um problema completo do repositório, documentado em Jupyter Notebook com foco em arquitetura e clareza de conclusões.

---

## 📌 Delimitação do Canteiro: Análise vs Engenharia de Dados

Este roadmap foca em **Análise, BI e Ciência de Dados Aplicada**. Quando o objetivo for **Engenharia de Dados**, a arquitetura muda para um repositório dedicado (`engenharia-dados`) com foco em:

- **Modelagem dimensional e relacional** (Star Schema, Snowflake Schema, Normalização).
- **Orquestração de Pipelines** (Apache Airflow, Dagster).
- **Processamento em Larga Escala** (PySpark, Databricks).
- **Data Warehousing Cloud** (BigQuery, Snowflake, Redshift).
- **Infraestrutura e Conteinerização** (Docker, Kubernetes).

SQL e Python são os pilares transversais mantidos em ambas as áreas.

---

## Configuração do Ambiente

```powershell
# Criação e ativação do ambiente virtual (Windows PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Instalação dos pacotes principais
pip install numpy pandas matplotlib seaborn jupyter sqlalchemy streamlit
