# Desafio 04 — `if` / `elif` / `else` com múltiplos status

## Enunciado

Praticar `if`, `elif` e `else` para verificar diferentes situações de
funcionários.

| Nome     | Salário   | Status   |
|----------|-----------|----------|
| Amanda   | R$ 2.500  | Ativo    |
| Patrícia | R$ 3.600  | Férias   |
| Carlos   | R$ 3.200  | Inativo  |
| Fernanda | R$ 4.100  | Afastado |
| João     | R$ 2.800  | Ativo    |

**Objetivo:** criar um programa que:

1. Percorra todos os funcionários.
2. Mostre o nome e o status de cada um.
3. Conte quantos estão ativos, de férias, afastados e inativos.
4. Some os salários apenas dos funcionários ativos.

## ⚠️ Status: PENDENTE

Nenhum arquivo `.py` foi enviado para este desafio. Diferente dos
anteriores, aqui o campo `ativo: True/False` não é suficiente — os dados
têm **4 status distintos** (`Ativo`, `Férias`, `Inativo`, `Afastado`), então
a estrutura de dados precisa de um campo `status` (string), não mais um
booleano `ativo`. Isso muda a modelagem do dicionário em relação aos
desafios 02 e 03, não é só trocar `if/else` por `if/elif/else`.

Quando tiver o código, me envie para eu revisar antes de subir aqui.
