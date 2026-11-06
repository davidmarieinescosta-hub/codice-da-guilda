# Previsões — o pergaminho que mente

Aposta: acerto _10__ de 21.

Legenda:
- funciona → executa e mostra a resposta normal
- avisa → imprime uma mensagem em português, sem traceback
- explode → aparece traceback: anote a exceção e o arquivo meu

Resultado pela régua escrita antes do teste: 8 de 21.
Com uma régua mais fina — "o programa percebeu que o pergaminho
estava errado?" — seriam 2 de 21. Não troco a régua: ela foi escrita
antes. A diferença entre 8 e 2 é o tamanho do que eu não sabia sobre
o programa.

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
| `listar` | explode: ZeroDivisionError (codice.py) | Aviso | Erro| pensei que por conta do arquivo não ter iria dar um erro de ZeroDivisionError, mas o arquivo não é importado nem pela main.py ou seja nada divide nada, eu errei completamente no mecanismo que seria usado. tudo está relaciona com o json.load que levanta JSCONDecodeError num arquivo de zero bytes. E vendo que o pergaminha está rasgado, avisa isso. |
| `filtrar --classe Mago` | explode: ZeroDivisionError (codice.py) | Aviso| Erro| pensei que por conta do arquivo não ter iria dar um erro de ZeroDivisionError, mas o arquivo não é importado nem pela main.py ou seja nada divide nada, eu errei completamente no mecanismo que seria usado. tudo está relaciona com o json.load que levanta JSCONDecodeError num arquivo de zero bytes. E vendo que o pergaminha está rasgado, avisa isso.
| `numeros` | explode: ZeroDivisionError (codice.py) | Aviso| Erro | pensei que por conta do arquivo não ter iria dar um erro de ZeroDivisionError, mas o arquivo não é importado nem pela main.py ou seja nada divide nada, eu errei completamente no mecanismo que seria usado. tudo está relaciona com o json.load que levanta JSCONDecodeError num arquivo de zero bytes. E vendo que o pergaminha está rasgado, avisa isso.|


### Caso 2

| Comando | Previsão | Resultado | Acerto? | Frase se errei |
|---|---|---|---|---|
| `listar` | avisa | avisa | Acerto | |
| `filtrar --classe Mago` | avisa | avisa |  Acerto | |
| `numeros` | avisa | avisa | Acerto | |


### Caso 3 


| Comando | Previsão | Resultado | Acerto? | Frase se errei |
|---|---|---|---|---|
| `listar` | explode: ZeroDivisionError (codice.py) | explode | Erro | Eu sabia que ia dar erro, mas errei na hora de identificar qual seria o erro, achei de novo por estar escrito "null" que interpretei como "nulo", poderia dar um erro de ZeroDivisionError, mas va verdade o json.load(arquivo) e o json.load(texto), devolovem None, e sendo que for d in None → TypeError: 'NoneType' object is not iterable, é por isso que o programa explode ai. |
| `filtrar --classe Mago` | explode: ZeroDivisionError (codice.py) | explode |Erro |  Eu sabia que ia dar erro, mas errei na hora de identificar qual seria o erro, achei de novo por estar escrito "null" que interpretei como "nulo", poderia dar um erro de ZeroDivisionError, mas va verdade o json.load(arquivo) e o json.load(texto), devolovem None, e sendo que for d in None → TypeError: 'NoneType' object is not iterable, é por isso que o programa explode ai.  |
| `numeros` | explode: ZeroDivisionError (codice.py) |explode | Erro |  Eu sabia que ia dar erro, mas errei na hora de identificar qual seria o erro, achei de novo por estar escrito "null" que interpretei como "nulo", poderia dar um erro de ZeroDivisionError, mas va verdade o json.load(arquivo) e o json.load(texto), devolovem None, e sendo que for d in None → TypeError: 'NoneType' object is not iterable, é por isso que o programa explode ai.|


### Caso 4 

| Comando | Previsão | Resultado | Acerto? | Frase se errei |
|---|---|---|---|---|
| `listar` | avisa | avisa | acerto | |
| `filtrar --classe Mago` | avisa | avisa | acerto | |
| `numeros` | avisa | avisa | acerto | |


### Caso 5 

| Comando | Previsão | Resultado | Acerto? | Frase se errei |
|---|---|---|---|---|
| `listar` | Funciona | explode  | erro | não olhei direito na hora de fazer a previsão não vi que estava {"Aldric": 42}, e que claramente ia dar erro de AttributeError, e isso ocorre porque é um modelo errado sobre o que o for entrega se rodar for x in {"Aldric": 42}, que entrega uma str enquanto se esperava um dicionário, por isso que ocorre um erro de AttributeError.|
| `filtrar --classe Mago` | aviso | explode | erro |não olhei direito na hora de fazer a previsão não vi que estava {"Aldric": 42}, e que claramente ia dar erro de AttributeError, e isso ocorre porque é um modelo errado sobre o que o for entrega se rodar for x in {"Aldric": 42}, que entrega uma str enquanto se esperava um dicionário, por isso que ocorre um erro de AttributeError.| 
| `numeros` | Funciona | explode  | erro | não olhei direito na hora de fazer a previsão não vi que estava {"Aldric": 42}, e que claramente ia dar erro de AttributeError, e isso ocorre porque é um modelo errado sobre o que o for entrega se rodar for x in {"Aldric": 42}, que entrega uma str enquanto se esperava um dicionário, por isso que ocorre um erro de AttributeError.|


### Caso 6 

| Comando | Previsão | Resultado | Acerto? | Frase se errei |
|---|---|---|---|---|
| `listar` | Funciona | explode:KeyError| erro  | Interperrei errado denovo, achando que por conta de não ter nìvel poderia dar errado, só que também não faria sentido ter posto KeyError, o que realmente acontece é que o missões tem plano B caso dé agluem erro, mas o nivel não tem. |
| `filtrar --classe Mago` | Funciona | explode:KeyError| erro  |  Interperrei errado denovo, achando que por conta de não ter nìvel poderia dar errado, só que também não faria sentido ter posto KeyError, o que realmente acontece é que o missões tem plano B caso dé agluem erro, mas o nivel não tem.|
| `numeros` | Aviso | explode:KeyError| erro  |  Interperrei errado denovo, achando que por conta de não ter nìvel poderia dar errado, só que também não faria sentido ter posto KeyError, o que realmente acontece é que o missões tem plano B caso dé agluem erro, mas o nivel não tem.|


### Caso 7 

| Comando | Previsão | Resultado | Acerto? | Frase se errei |
|---|---|---|---|---|
| `listar` | Funciona | Funciona | acerto | |
| `filtrar --classe Mago` | Funciona | Funciona | acerto | |
| `numeros` | Funciona | explode:TypeError | erro  | interpretei errado , chega um momento em que vai ter que somar o nivel nos numeros, e não tem como somar um str.|
