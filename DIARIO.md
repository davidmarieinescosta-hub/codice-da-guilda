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

## Dia 4 (08/09/26)
- O que fiz: escolhi a busca por nome como próxima função e a escrevi do zero em três tentativas — o `return` cortava o laço no primeiro giro (devolvia sempre o primeiro herói), o mesmo nome em duas caixas engolia o procurado, e a variável do `for` tinha que ser um nome simples. No fim digitei a versão certa: ela encontra Gandalf e fica em silêncio quando o nome não existe.
- Onde travei: na comparação — `if nome == str` nunca disparava, e `for heroi["nome"] in herois` dava NameError, porque a variável do `for` é uma caixa nova que o próprio loop cria, com nome simples; o `["nome"]` pertence à comparação, não ao `for`.
- O que entendi hoje: ler o TypeError de argumento faltando (a chamada precisa passar o que a função exige), que `str` é um tipo e não um valor, e que o `for` cria a caixa a cada giro — por isso a variável dele tem nome simples.

## Dia 5 (09/09/26)
- O que fiz: paguei a dívida da Regra 4 (expliquei a buscar_heroi em voz alta), aprovei o diário do Dia 4 e escrevi a filtrar_herois_por_classe — lista aprovados nascendo dentro da função, append do herói inteiro e return depois do loop. Commitei.
- Onde travei: chamei a função sem segurar o resultado — a caixa `magos` nunca tinha sido criada e o `print(magos)` deu NameError; a minha versão do meio dizia "é um mago" até para os Rangers (texto fixo dentro de função genérica mente); e filtrei "Magos" com s e recebi lista vazia — a comparação é letra por letra, e a lista vazia é a resposta honesta.
- O que entendi hoje: uma função sem return entrega None — o valor evapora; segurar o resultado é trabalho do `=` (mãos, não olhos); o return é o que deixa o chamador usar o resultado depois; e reconheci que o filtro é o mesmo esqueleto da busca — percorre, filtra, entrega.

## Dia 6 (12/09/26)
- O que fiz: fechei o rastro do Dia 5 (adendo no IA.md sobre o CLAUDE.md) e escrevi a mostrar_numeros — o total com len, o cofre acumulador para a média, e a caixa do campeão (duas caixas reescritas juntas pelo if, nível e nome).
- Onde travei: a buscar_heroi "não voltava nada" — o baú estava vazio (cada sessão nasce com baú novo; o programa não tem memória, e é de propósito); depois o "Gandalf " com espaço invisível no fim não era encontrado (o len provou: 8 letras, não 7); e o REPL insistia na função velha — editar o arquivo não alcança o Python que já está rodando.
- O que entendi hoje: as três camadas onde o código vive (editor, disco, processo), a sonda len para medir strings, e o coração do acumulador — caixa = caixa + x usa o valor velho para fabricar o novo; na caixa do campeão, a reescrita só acontece quando o if deixa entrar.

## Dia 7 (13/09/26)
- O que fiz: escrevi o menu — a porta giratória do while, o roteador de if/elif, as caixas nome e classe alimentando os parâmetros da busca e do filtro, o aprovados pegando a bola do return, e a chave de ignição menu() no fim do arquivo. O programa agora roda sozinho com python codice.py. Com isso, as seis funções estão completas.
- Onde travei: na condição do while (escrevi == no lugar de != — a porta girava ao contrário); na releitura da pergunta (deixei o "s ou n" fora do loop, inalcançável — e ainda inventei a recursão sem querer, menu() chamando menu()); e no filtrar, que devolvia a lista e o menu não pegava — silêncio total (num programa, ninguém mostra nada de graça, só o REPL mostra).
- O que entendi hoje: o contrato do while — roda ENQUANTO a condição for verdadeira e para quando vira falsa, e a pergunta refeita no fim do corpo alimenta a próxima verificação; que funções se chamam (o menu é o capitão); e que usabilidade é pensar em quem usa o programa, não em quem escreve. 