# Roadmap — Lógica de Programação em Python

Trilha de fixação de lógica, do zero até você estar pronto para atacar o
repositório de análise de dados. Ordem importa: cada módulo assume que o
anterior está sólido, não só "feito".

Marque `[x]` conforme for concluindo.

## Módulo 1 — Fundamentos ✅
- [x] Desafio 01 — Produtos entregues (listas de dicionários, soma condicional)
- [x] Desafio 02 — Funcionários e salários (múltiplos loops → identificar ineficiência)
- [x] Desafio 03 — Variável dentro do `for`
- [ ] Desafio 04 — `if`/`elif`/`else` com múltiplos status *(pendente)*

## Módulo 2 — Strings
- [ ] Desafio 05a — Validador de formato (e-mail simples, CPF sem dígito verificador): fatiamento, `.split()`, `.strip()`
- [ ] Desafio 05b — Contador de palavras/caracteres em um texto
- [ ] Desafio 05c — Normalização de texto (maiúsculas/minúsculas, remoção de acentos com `unicodedata`)

## Módulo 3 — Funções
- [ ] Desafio 06a — Refatorar os desafios 01–03 extraindo lógica repetida em funções
- [ ] Desafio 06b — Funções com `*args`, `**kwargs`
- [ ] Desafio 06c — Funções como parâmetro (`sorted(key=...)`, `map`, `filter`)

## Módulo 4 — Comprehensions
- [ ] Desafio 07a — Reescrever o `desafio_02.py` (3 loops) usando list/dict comprehension
- [ ] Desafio 07b — Comprehension aninhada (matriz → lista achatada)
- [ ] Desafio 07c — Dict comprehension para agrupar dados (ex: funcionários por status)

## Módulo 5 — Tratamento de erros
- [ ] Desafio 08a — `try`/`except`/`else`/`finally` validando entrada de usuário
- [ ] Desafio 08b — Exceções customizadas (`class SaldoInsuficienteError(Exception)`)
- [ ] Desafio 08c — Validação de dados de um dicionário (chave ausente, tipo errado)

## Módulo 6 — Arquivos, CSV e JSON
- [ ] Desafio 09a — Ler/escrever `.txt`
- [ ] Desafio 09b — Ler/escrever `.csv` com o módulo `csv` (sem pandas ainda — entender o básico primeiro)
- [ ] Desafio 09c — Ler/escrever `.json` com o módulo `json`

## Módulo 7 — POO básica
- [ ] Desafio 10a — Modelar `Funcionario` como classe (os desafios 02–04 viram um `Funcionario.status`)
- [ ] Desafio 10b — Herança simples (`FuncionarioCLT`, `FuncionarioPJ`)
- [ ] Desafio 10c — Métodos especiais (`__str__`, `__repr__`, `__eq__`)

## Módulo 8 — Recursão
- [ ] Desafio 11a — Fatorial e Fibonacci recursivos
- [ ] Desafio 11b — Soma de lista aninhada de profundidade arbitrária

## Módulo 9 — Estruturas de dados
- [ ] Desafio 12a — Pilha (stack) implementada com lista
- [ ] Desafio 12b — Fila (queue) implementada com `collections.deque`
- [ ] Desafio 12c — Quando usar `set` vs `list` vs `dict` (custo de busca — introdução a complexidade)

## Módulo 10 — Busca e ordenação (fundamento para SQL/análise depois)
- [ ] Desafio 13a — Busca linear vs busca binária (implementação manual)
- [ ] Desafio 13b — Bubble sort (entender, não usar em produção)
- [ ] Desafio 13c — Comparar com `sorted()`/`.sort()` nativo e explicar por que usar o nativo

## Bônus
- [x] Triângulo retângulo com `*`

---

## Critério de "concluído" (não é só rodar sem erro)

Um desafio só está de fato pronto quando você consegue responder:
1. Existe alguma iteração/loop redundante que poderia virar 1 passagem só?
2. O nome das variáveis e chaves de dicionário está consistente?
3. O código quebra se a lista de entrada estiver vazia? Você testou isso?
4. Você consegue explicar a complexidade aproximada (quantas vezes o código
   passa pelos dados) sem rodar o código?

Se a resposta de qualquer um for "não sei", o desafio não está concluído —
está funcionando por acaso.

## Próximo passo

Depois do Módulo 6 (arquivos/CSV/JSON) você já tem base suficiente para
começar o repositório **analise-dados-python** em paralelo — CSV manual e
`json` puro são a ponte natural para `pandas`.
