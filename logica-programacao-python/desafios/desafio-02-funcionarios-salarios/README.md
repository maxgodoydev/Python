# Desafio 02 — Funcionários e Salários

## Enunciado

Uma empresa possui os seguintes funcionários:

| Nome     | Salário   | Status  |
|----------|-----------|---------|
| Amanda   | R$ 2.500  | Ativa   |
| Carlos   | R$ 3.200  | Inativo |
| Fernanda | R$ 4.100  | Ativa   |
| João     | R$ 2.800  | Ativo   |
| Patrícia | R$ 3.600  | Inativa |

**Objetivo:** criar um programa que:

1. Armazene os funcionários e suas informações.
2. Calcule o total dos salários somente dos funcionários ativos.
3. Conte quantos funcionários estão ativos.
4. Conte quantos funcionários estão inativos.
5. Mostre os três resultados no terminal.

## Observação de revisão

A solução original percorre a lista `empresa` **três vezes** (um loop para
somar salário, outro para contar ativos/inativos, outro para imprimir
status), quando um único loop resolveria os cinco requisitos. Não é
crítico para 5 registros, mas é o padrão que não escala — em uma lista de
milhares de itens isso significa 3x mais iterações do que o necessário.
O `desafio_03.py` já resolve isso corretamente com um único loop; vale
usar o mesmo padrão aqui se quiser refatorar.

Também há inconsistência de nomenclatura na chave `"Salário"` (maiúscula)
contra `nome`, `moeda`, `ativo` (minúsculas) — não quebra o código, mas é
inconsistência de estilo.

## Como executar

```bash
python3 desafio_02.py
```
