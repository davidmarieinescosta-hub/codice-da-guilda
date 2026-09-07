# Diário de Bordo

## Dia 1 (03/09/26)
- O que fiz: criei a estrutura inicial do repositório, criei o começo da estrutura do projeto e realizei os primeiros commits.
- Onde travei: Travei na criação do repositorio no github, e na criação das pastas.
- O que entendi hoje: como criar um repostório, colocar um venv, mecher com mais facilidade com o terminal, transformar um repositório em uma pasta, aprendi a fazer um commit para o github

## Dia 2 (04/09/26)
- O que fiz: aprendi o .gitignore linha por linha (expliquei cada uma em voz alta), decidi a estrutura dos heróis (dicionário dentro de lista, com justificativa), escrevi cadastrar_heroi junto com a IA e listar_herois sozinho — meu primeiro for.
- Onde travei: em dois NameError — um porque o arquivo não estava salvo, outro porque a linha herois = [] tinha sumido. No fim do dia descobri que o baú está no lugar errado (dentro da função) e o print da listar mostra o dicionário cru; o sono bateu e deixei a correção para amanhã.
- O que entendi hoje: ler traceback de trás para a frente, a diferença entre editor e disco (salvar!), escopo (o que nasce dentro da função morre com ela) e como o for percorre uma lista.

## Dia 3 (07/09/26)
- O que fiz: corrigi sozinho os dois bugs deixados do Dia 2 — movi o baú (`herois = []`) para o escopo global e formatei o print da listar com a f-string (três buracos, cada campo com o `heroi` na frente). Commitei as duas correções.
- Onde travei: tentei chamar a função no mundo do `>>>` e deu NameError (typo: cadastar sem o r, e o REPL não conhecia meu arquivo); no print, imprimi o baú inteiro e depois pus a vírgula dentro das chaves, o que criou uma tupla — a saída saiu toda entre parênteses.
- O que entendi hoje: a diferença entre `python` (REPL, mundo em branco) e `python -i codice.py` (roda o arquivo e deixa as funções vivas); cada `{...}` da f-string guarda uma única expressão e a vírgula de texto fica fora; `heroi` é um dicionário, não uma biblioteca; e o `git add -p` deixa escolher trecho por trecho no commit. 