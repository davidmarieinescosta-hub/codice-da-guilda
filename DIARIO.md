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

## Dia 8 (14/09/26)
- O que fiz: escrevi o README sozinho, em três versões — título, o que é (com a honestidade do Ato I: os dados somem quando o programa fecha), as seis funções e a seção Como rodar com o bloco de código. Commitei.
- Onde travei: quase nada — o texto fluiu; o único tropeço foi deixar o documento só no editor (a lição das três camadas: o disco ficou vazio até o Ctrl+S) e escrever "o comando, em um bloco de código" como texto, antes de aprender que o bloco é formatação do markdown, três crases.
- O que entendi hoje: que o README é a vitrine e responde três perguntas — o que é, como rodar, o que funciona — garantindo o critério de rodar em outra máquina; que markdown usa ``` para blocos de código; e que justificativa de decisão (a língua) não precisa pedir desculpas na vitrine — ela mora no Rito.
- Adendo: descobri que meu GitHub estava 15 commits atrás — o commit local não é publicação; o push é a terceira camada do git. Rodei o push e o repositório público agora mostra o projeto inteiro.

## Dia 9 (15/09/26)
- O que fiz: enviei o link do repositório ao mestre e recebi dele o Ato II. No caminho,
  aprendi que repositório público se envia pelo link (ou pelo `git clone`) — o ZIP do
  GitHub baixa os arquivos, mas não carrega a história dos commits.
- Onde travei: em nada.
- O que entendi hoje: como apresentar os meus trabalhos para o mestre.


## Dia 10 (23/09/26)
- O que fiz: comecei o Ato II — primeiro ciclo branch + PR (o rastro pendente do Dia 9), decidi a arquitetura das quatro salas (entrada, decisões, relatórios, armazenamento), escrevi o ARQUITETURA.md e mergeei no segundo PR, e criei a nota de conceitos do dia no Obsidian com callouts, wikilinks e mermaid.
- Onde travei: na pergunta 4 da arquitetura — quem é o dono do baú? Demorei a ver que ninguém: ele circula por parâmetro e volta para o arquivo; e na hora de passar o caminho do vault (o link interno do Obsidian não é o caminho do disco — a IA achou a pasta no Explorador).
- O que entendi hoje: módulo é um arquivo com uma responsabilidade só; função pura recebe o que precisa e devolve o resultado sem mexer no mundo — efeito colateral é o contrário; branch é linha paralela e PR é a porta da frente da main; e arquitetura se desenha no papel antes de codar.

## Dia 11 (24/09/26)
- O que fiz: criei o armazenamento.py — a salvar_herois grava o baú no pergaminho herois.json em JSON, com o José saindo acentuado; decidi que o arquivo de dados fica fora do repositório e aprendi o git check-ignore. Dois PRs mergeados (o módulo e a linha do .gitignore).
- Onde travei: na explicação da Regra 4 — o with e o json.dump eu não sabia explicar, e a IA destrinchou linha por linha até eu re-explicar com as minhas palavras; e no mistério do herois.json que continuava no git status — o commit tinha levado só o armazenamento.py (editor aberto não é linha salva).
- O que entendi hoje: JSON é serialização — traduz estrutura da memória em texto e de volta; o with é o guarda-chuva que fecha o arquivo aconteça o que acontecer; "w" é o modo gravar; encoding utf-8 + ensure_ascii False são as duas chaves anti-"JosÃ©"; e dado gerado a cada execução não entra no repo — vai para o .gitignore.

## Dia 12 (27/09/26)
- O que fiz: escrevi a carregar_herois — o espelho do salvar (modo "r", json.load, return) — e, depois de ver os dois monstros explodirem na minha frente (FileNotFoundError e JSONDecodeError), armei os dois caçadores try/except com avisos em português. O critério 4 do Ato cumprido na prática, no oitavo PR.
- Onde travei: no traceback longo do JSON rasgado — quatro andares de arquivos internos do Python; e duvidei de mim mesmo achando que o primeiro except nem existia — ele estava lá, só não era o caçador daquele monstro.
- O que entendi hoje: exceção é um erro que interrompe o programa se ninguém capturar; try/except é o caçador específico — capturar Exception esconderia bugs de verdade; no traceback longo, a regra é pular os arquivos dos outros e achar o meu; e "r" lê sem apagar, json.load reconstrói e o return entrega.

## Dia 13 (28/09/26)
- O que fiz: integrei o ciclo do dia — a ignição em três atos (carregar → menu → salvar) — e vi o programa lembrar dos heróis entre duas vidas; depois documentei os contratos do armazenamento com type hints e docstrings. Três PRs no dia.
- Onde travei: na explicação do "herois = armazenamento.carregar_herois()" — eu disse que herois era igual ao armazenamento, quando na verdade a caixa RECEBE o baú que a função devolve; e na docstring fora do endereço — ela precisa ser a primeira instrução da função, senão é carta morta.
- O que entendi hoje: o import do próprio módulo faz as salas conversarem; a ignição vive no escopo global, por isso as funções enxergam o baú; a memória guarda até os erros (o "Mafo" ficou gravado no pergaminho); e type hints + docstrings documentam o contrato da função sem mudar o comportamento.

## Dia 14 (01/10/26)
- O que fiz: planejei a divisão dos módulos — as seis funções passaram pela mesa de operação, cada uma partida em pedaços de falar e decidir, com destino e troca de roupa. Saí com o plano completo das cinco salas: cli, regras, relatorios, armazenamento e main.
- Onde travei: mandei a buscar_heroi para o armazenamento — a regra de bolso me corrigiu (arquivo → armazenamento; decisão → regras); e não lembrava o valor surpresa do Dia 5 — o None voltou com prova.
- O que entendi hoje: o append fica com quem segura o baú (a portaria), não com a função pura; o silêncio da busca vira None — resposta explícita que o is None reconhece; o relatório devolve dicionário, repetindo a justificativa do Dia 2; e o main.py é o maestro — a ignição não mora na cli.
- Adendo (2ª sessão): implementei o regras.py — as três funções puras, testadas trabalhando juntas — e mergeei no 14º PR. Na Regra 4, achei que a busca ia imprimir o "não encontrado"; a correção: o conselho devolve, a portaria fala. Entendi o pipe `|` das placas ("dicionário OU None") e vi a primeira sala do castelo de pé.

## Dia 15 (02/10/26)
- O que fiz: construí a segunda sala — relatorios.py com a mostrar_numeros devolvendo o dicionário {"quantos", "media", "mais_forte"} e a formatar_lista devolvendo as frases prontas. Decidi o guarda do baú vazio (opção A) e mergeei no 16º PR.
- Onde travei: repeti o fantasma do dia anterior — disse que a função "ia printar o dicionário vazio"; a correção definitiva: sala que conta só devolve — o print do teste era meu, no REPL.
- O que entendi hoje: o guarda da porta (if len == 0) responde a pergunta legítima da guilda vazia com a verdade (zero, zero, None); o dicionário do relatório repete a justificativa do Dia 2; e procurar print em regras ou relatorios é não achar — o critério 2 em carne viva.
- Adendo (2ª sessão): construí a portaria — cli.py com o menu recebendo o baú por parâmetro e chamando as salas, mais a linha nova que traduz o None do campeão. Deixei escapar o "None, é o mais forte" — a IA provou no teste, e a correção era o padrão is None que eu já tinha no buscar. Todos os prints do programa moram na interface; o baú chega por parâmetro porque circula. PR #18.
- Adendo (3ª sessão): construí o main.py — o maestro que carrega o baú, passa o menu e salva no fim, com a ignição guardada pelo `if __name__ == "__main__"`. Na conferência, a sonda do `git status` ("ahead 1 commit") revelou dois furos: a correção da chave tinha ido DIRETO para a main (e nem publicada) e o armazenamento ainda imprimia os avisos. Resgatei o commit com `git branch <nome> <commit>` + `git reset --hard origin/main` e a correção entrou por PR #22.
- Onde travei: tratei a main como mesa de trabalho, e a main é a porta da frente — nem correção urgente entra sem PR. E no Furo 2, os prints do armazenamento esbarravam em dois critérios ao mesmo tempo (nenhum print fora da interface × avisar em português).
- O que entendi hoje: a tupla agora é de propósito — a vírgula no return faz dois valores viajarem juntos — e o desempacotamento (`herois, aviso = ...`) distribui nas caixas da esquerda; a sala que lembra não fala, devolve `(baú, aviso)` e a portaria lê o recado; e uma branch pode nascer apontando para um commit que já existe.
- Adendo (4ª sessão): não escrevi código — fui conferir o projeto contra a fonte primária, o documento do programa (a Jornada do Escriba). O link do artifact não abre para a IA (o conteúdo vive atrás do meu login), então baixei o HTML e ela leu o arquivo do disco. A comparação derrubou três coisas que a gente já dava como certas: o argparse é requisito do Ato II (não é passo opcional), o PR com correções pedidas pelo mestre é critério separado da Sabotagem I, e o README não é critério de aceite do ato. Com o documento na mão, reescrevi o relatório do mestre e enviei.
- Onde travei: no código, em nada. O erro da sessão foi da nossa lista de pendências — montada de memória, minha e da IA — e quem corrigiu foi o papel.
- O que entendi hoje: que critério de aceite é lista fechada e a fonte primária vence a lembrança; que ainda falta código de verdade no ato (o argparse, e os conceitos de `finally`, `raise` e `requirements.txt`); e que o único critério que só eu posso destravar é pedir a revisão do mestre num PR.

## Dia 16 (07/10/26)
- O que fiz: aprendi o argparse do zero — as quatro peças na ordem certa (a classe, o add_argument,
  o parse_args, a caixa args) e provei o Namespace rodando os três casos no terminal (--nome Aldric,
  sem nada, e --help). Não escrevi código de produção: hoje foi dia de aprender a peça nova.
- Onde travei: no teste de memória. Fechei o arquivo e tentei reescrever as cinco linhas sem olhar: acertei o `import` e não lembrei as letras específicas do resto (`ArgumentParser`, `add_argument`, `parse_args`). O teste mediu com precisão o que o painel do Obsidian já marcava como risco (o critério Modificar) — eu entendo o conceito e não retenho a peça. E descobri um padrão meu que se repetiu três vezes na conversa: eu respondia sobre o programa em vez de responder sobre a linha.
- O que entendi hoje: que o ponto em `parser.parse_args()` é a mesma regra do `herois.append()` do Ato I — o ponto diz de quem é a ação, por isso o `parse_args` mora no objeto e não no módulo (o Python provou com o erro: `module 'argparse' has no attribute 'parse_args'`); que o `input()` espera e o `parse_args()` busca, porque os dados já chegaram na linha de comando; e que o meu gap é de detalhe, não de conceito — o que muda o treino de amanhã.
