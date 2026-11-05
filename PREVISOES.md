# Previsões — o pergaminho que mente

Aposta: acerto _10__ de 21.

Legenda:
- funciona → executa e mostra a resposta normal
- avisa → imprime uma mensagem em português, sem traceback
- explode → aparece traceback: anote a exceção e o arquivo meu

---

## Caso 1 — arquivo com zero bytes

## Caso 2 — []

## Caso 3 — null

## Caso 4 — {}

## Caso 5 — {"Aldric": 42}

## Caso 6 — [{"nome": "Aldric", "classe": "Mago"}]

## Caso 7 — [{"nome": "Aldric", "classe": "Mago", "nivel": "10"}]




### Caso 1 

| Comando | Previsão | Resultado | Acerto? | Frase se errei |
|---|---|---|---|---|
| `listar` | explode: ZeroDivisionError (codice.py) | | | |
| `filtrar --classe Mago` | explode: ZeroDivisionError (codice.py) | | | |
| `numeros` | explode: ZeroDivisionError (codice.py) | | | |


### Caso 2

| Comando | Previsão | Resultado | Acerto? | Frase se errei |
|---|---|---|---|---|
| `listar` | avisa | | | |
| `filtrar --classe Mago` | avisa | | | |
| `numeros` | avisa | | | |


### Caso 3 


| Comando | Previsão | Resultado | Acerto? | Frase se errei |
|---|---|---|---|---|
| `listar` | explode: ZeroDivisionError (codice.py) | | | |
| `filtrar --classe Mago` | explode: ZeroDivisionError (codice.py) | | | |
| `numeros` | explode: ZeroDivisionError (codice.py) | | | |


### Caso 4 

| Comando | Previsão | Resultado | Acerto? | Frase se errei |
|---|---|---|---|---|
| `listar` | avisa | | | |
| `filtrar --classe Mago` | avisa | | | |
| `numeros` | avisa | | | |


### Caso 5 

| Comando | Previsão | Resultado | Acerto? | Frase se errei |
|---|---|---|---|---|
| `listar` | Funciona | | | |
| `filtrar --classe Mago` | aviso | | | |
| `numeros` | Funciona | | | |


### Caso 6 

| Comando | Previsão | Resultado | Acerto? | Frase se errei |
|---|---|---|---|---|
| `listar` | Funciona | | | |
| `filtrar --classe Mago` | Funciona | | | |
| `numeros` | Aviso | | | |


### Caso 7 

| Comando | Previsão | Resultado | Acerto? | Frase se errei |
|---|---|---|---|---|
| `listar` | Funciona | | | |
| `filtrar --classe Mago` | Funciona | | | |
| `numeros` | Funciona | | | |
