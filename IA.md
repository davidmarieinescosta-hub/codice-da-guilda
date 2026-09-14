# Registro de uso de IA

## Dia 1
- Pergunta: "como criar a estrutura do ato 1"
- Resposta: recebi os comandos de terminal para criar os arquivos e o conteúdo mínimo de .gitignore/README/DIARIO/IA
- O que mudei/decidi: por enquanto nada, já que tudo que eu fiz até agora foi aprender.

## Dia 1 (2ª sessão)
- Pergunta: "analise o CLAUDE.md" — e depois enviei as seis regras da Guilda para a IA ter consciência delas.
- Resposta: a IA reescreveu o CLAUDE.md para o Ato I (antes ele descrevia um projeto Django antigo), mantendo o contrato de mentoria e adicionando as seis regras. Também adicionou .claude/settings.json ao .gitignore, porque esse arquivo guarda uma credencial de API e o repositório é público.

- O que mudei/decidi: aceitei o que a IA propôs e entendi o motivo , já que o segrdo não pode ir para um repositório público.

## Dia 2
- Pergunta: usei a IA ao longo do dia para revisar o .gitignore, decidir como representar os heróis e depurar os erros do codice.py (dois NameError).
- Resposta: a IA guiou o teste do .gitignore (eu expliquei as linhas, ela completou as lacunas), me deixou decidir sozinho a estrutura dos heróis e, nos erros, me ensinou a ler o traceback de trás para a frente e a investigar com sondas (dir(), type, a bolinha do VSCode) em vez de entregar a resposta pronta.
- O que mudei/decidi: escolhi dicionário para cada herói porque o acesso é pelo nome do campo (descartando a lista, que exigiria lembrar posições) e uma lista como baú dos heróis. Parei antes de corrigir o baú mal posicionado — fica para amanhã.

## Dia 3
- Pergunta: retomei do ponto onde paramos e pedi ajuda ao longo do dia — por que `cadastar_heroi()` dava NameError, e como arrumar o print da `listar_herois`.
- Resposta: a IA explicou a diferença entre o REPL (mundo do `>>>`, em branco) e rodar o arquivo, me devolveu pistas em vez da resposta pronta (Regra 5), rodou a minha linha para mostrar a prova — a vírgula dentro das chaves criou uma tupla —, nomeou os conceitos (tupla, dicionário vs biblioteca, convenção de aspas simples dentro da f-string) e me ensinou o fechamento do dia: commit com explicação em voz alta, diário e rastro.
- O que mudei/decidi: decidi fazer um commit único com as duas correções em vez de dois (cheguei a testar o `git add -p`, mas preferi simplificar). Mantive as entradas do Dia 2 no diário como estavam, após releitura.

## Dia 4
- Pergunta: como escrever a função de busca por nome — e, no meio do caminho, perguntei se a IA me mostrava pronto ou se eu tentava mais.
- Resposta: a IA me devolveu para tentar (Regra 5) e, a cada erro meu, rodou meu código para mostrar a prova — o `return` devolvia sempre o primeiro herói, o `if` nunca disparava. Depois da minha terceira tentativa, implementou junto a versão final linha por linha, e eu digitei — não colei.
- O que mudei/decidi: eu escolhi buscar o nome porque eu acho que quando vc quer identificar alguém primeiramente, você procura o seu nome que é algo que a diferencia de todas as pessoas.

## Dia 5
- Pergunta: como fazer a função de filtrar por classe — e como exibir o resultado de forma bonita sem prender a mensagem dentro da função.
- Resposta: a IA me devolveu pistas a cada rodada e rodou meus testes para provar os erros — o None que o chamador recebe quando a função só usa print, e o "é um mago" aparecendo para os Rangers. Me ensinou que a função separa (return entrega os dados) e a exibição exibe (responsabilidade única); que a chamada entrega o valor entre aspas (o porteiro); e que segurar o resultado é trabalho do `=` (mãos, não olhos).
- O que mudei/decidi: escolhi filtrar antes dos números para fazer por etapas, construindo algo mais linear e com evolução mais organizada; e escolhi return em vez de print porque posso querer usar o resultado depois — o print mostraria e perderia. E depois de uma conversa coma IA, eu decidi não tirar o CLAUDE.md do github

## Dia 6
- Pergunta: se o "erro" da buscar_heroi era real (ela não voltava nada), como escrever a mostrar_numeros, e por que o Python não via as minhas edições.
- Resposta: a IA provou com testes que a buscar estava intacta (baú vazio = silêncio; depois achou a impressão digital do espaço invisível no "Gandalf "). Me deu as três peças dos números (len, acumulador, campeão), explicou as três camadas editor/disco/processo, e no fim do dia — eu estava exausto, depois dos meus 40 minutos de luta — me entregou a versão final da função linha por linha, e eu digitei.
- O que mudei/decidi: escolhi a opção A (substituir o filtro de nível pela mostrar_numeros de verdade). Eu decidi fazer a forma de verdade porque seria a forma correta e mais pratica.

## Dia 7
- Pergunta: como fazer o menu — se eu posso ligar funções, se vou precisar do if, e como passar os parâmetros da busca e do filtro.
- Resposta: a IA confirmou que funções se chamam (o menu é o capitão que grita as ordens), ensinou o while (a porta giratória), o elif e o !=, me avisou das armadilhas (a condição invertida, a pergunta que precisa ser refeita dentro do loop), nomeou a recursão que inventei sem querer (menu() chamando menu()), e testou o programa inteiro com uma sessão simulada — achando o return do filtrar evaporando no menu. Também corrigiu: o Ato II resolve persistência (salvar em arquivo), não o menu.
- O que mudei/decidi: escolhi "sair" escrito em vez de um número por usabilidade — quem abre o programa entende na hora, sem consultar legenda; e deixei a opção desconhecida ser ignorada sem quebrar, para polir depois.

## Dia 8
- Pergunta: como escrever o README — o que ele precisa responder, em que língua, e como colocar o comando de rodar.
- Resposta: a IA deu o tripé (o que é, como rodar, o que funciona), apontou a seção Como rodar que faltava, ensinou o bloco de código do markdown com três crases (depois que eu escrevi a instrução como texto), revisou as três versões e me lembrou do Ctrl+S quando o arquivo do disco ficou vazio.
- O que mudei/decidi: escolhi o português porque todo o programa está nessa língua (descartando o inglês, convenção do GitHub); e mantive a nota da escolha no README.
- Adendo: perguntei se o repositório era mesmo público (o navegador deu 404); a IA investigou — o ls-remote provou que é público, e o branch -vv revelou 15 commits locais nunca enviados. Eu rodei o push e publiquei o projeto completo. 

