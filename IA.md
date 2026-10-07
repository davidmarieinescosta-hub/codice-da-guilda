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

## Dia 9
- Pergunta: como enviar o repositório para o mestre, que me passou o e-mail dele.
- Resposta: a IA mostrou que o repositório público se envia pelo link (e pelo git clone), avisou que o ZIP do GitHub não carrega a história dos commits — e rascunhou o e-mail. Depois, quando o Ato II chegou, mapeou os 7 critérios e propôs a sequência de etapas.
- O que mudei/decidi: enviei o link do repositório ao mestre e recebi o Ato II e decidi que a primeira etapa dele seria a arquitetura.

## Dia 10
- Pergunta: como começar o Ato II — a arquitetura (quem fala, quem decide, quem lembra), o que fazer com o rastro pendente do Dia 9, e como organizar os resumos de conceitos no Obsidian.
- Resposta: a IA propôs começar pela arquitetura no papel e guiou com quatro perguntas (partir as funções mistas, o armazenamento vazio, a quarta sala, o dono do baú); ensinou o ciclo branch + PR na prática; rascunhou o ARQUITETURA.md — que eu expliquei em voz alta antes do merge; localizou o vault no disco e escreveu a nota de conceitos do dia com callouts, wikilinks e mermaid.
- O que mudei/decidi: escolhi começar pela arquitetura; decidi as quatro salas (menu na entrada, mostrar_numeros nos relatórios); entendi que o baú não tem dono — passa por todas e volta para o arquivo; e pedi que a IA salve o resumo de conceitos no meu vault no fim de cada sessão.

## Dia 11
- Pergunta: como fazer o armazenamento — o nome do arquivo, o formato, e um passo a passo explicativo do salvar.
- Resposta: a IA me deu as peças (with, json.dump, encoding), o passo a passo para eu digitar, testou o José no pergaminho provando o acento, destrinchou o with e o dump quando eu disse "não sei" na Regra 4, e investigou o mistério do herois.json teimando no git status — o commit não tinha levado a linha do .gitignore. Me ensinou o git check-ignore.
- O que mudei/decidi: escolhi o nome herois.json; primeiro decidi commitar o arquivo de dados, e depois de ouvir o argumento mudei de ideia — dado gerado a cada execução fica no .gitignore.

## Dia 12
- Pergunta: como escrever a carregar_herois (eu nunca tinha visto isso no meu curso) e por que o herois.json sumiu do VSCode e acusava erro.
- Resposta: a IA me deu o passo a passo do espelho (três trocas: modo "r", json.load, return); me fez reproduzir os dois monstros antes de me dar a arma (try/except); explicou o traceback longo — pular os arquivos dos outros e achar o meu; confirmou que o primeiro except já existia quando duvidei; e provou os três mundos num teste só.
- O que mudei/decidi: escrevi as mensagens de erro em português e escolhi o return [] como baú honesto — quando não há pergaminho (ou ele está rasgado), a guilda começa vazia e o programa segue vivo.

## Dia 13
- Pergunta: qual import é mais eficiente, em que documento escrever as linhas da integração, e conferir se o que eu fiz estava certo.
- Resposta: a IA mostrou que os dois imports têm a mesma eficiência — o eixo certo é legibilidade; guiou os três atos da ignição (carregar → menu → salvar); provou a memória com duas execuções seguidas e revelou o "Mafo" gravado no pergaminho; e corrigiu o endereço da docstring (primeira instrução da função, senão o Python a descarta).
- O que mudei/decidi: escolhi o import armazenamento pela origem explícita; matei o herois = [] da linha 1 — o carregar virou a única fonte do baú; e escrevi as docstrings com as minhas palavras.

## Dia 14
- Pergunta: se o plano no papel era exigência do projeto, qual desenho deixaria o programa mais completo, e qual organização ficaria melhor para a listagem, os números e o menu.
- Resposta: a IA esclareceu que o papel é exigência do Rito II (não dos critérios de aceite), recomendou com justificativas os desenhos — relatório prepara e cli imprime (B), dicionário para os três números, main.py como maestro — me relembrou o None com prova, e corrigiu a sala da busca (decisão vai para regras, não armazenamento).
- O que mudei/decidi: escolhi conversa agora e papel na reta final do Ato; fechei as escolhas B, dicionário e main.py; e montei o plano completo das cinco salas, começando a implementação pela regras.py.
- Adendo (2ª sessão): pedi à IA para organizar o arquivo e preencher as docstrings; ela testou as três funções — inclusive a busca que devolve None e o filtro que devolve lista vazia — e me corrigiu na explicação: a função pura não imprime, ela devolve; quem fala é a cli.

## Dia 15
- Pergunta: qual opção adotar para o baú vazio na mostrar_numeros, e preencher as docstrings do relatorios.
- Resposta: a IA recomendou a opção A (o guarda na porta), organizou o arquivo com as transformações do meu próprio código, preencheu as docstrings e me corrigiu mais uma vez: a função não imprime — devolve; o print do teste era meu, no REPL.
- O que mudei/decidi: escolhi A porque o relatório responde com a verdade da guilda vazia — zero, zero, ninguém — e descartei deixar explodir, que esconderia a resposta de uma pergunta legítima.
- Adendo (2ª sessão): pedi para testar o menu; a IA provou o "None, é o mais forte" da guilda vazia e me deu o padrão is None (irmão do buscar). Perguntei por que ela anda entregando mais código pronto — ela explicou a diferença entre transformação (pistas) e montagem (andaime) e me desafiou a reescrever o cli.py de memória na próxima sessão.
- O que mudei/decidi: aceitei o desafio da reescrita de memória — 15 minutos, sem olhar, como treino do critério Modificar do Rito.  


## Dia 15 (3ª sessão)
- Pergunta: como construir o main.py e o que fazer com os dois prints que sobraram no armazenamento.
- Resposta: a IA deu o esqueleto do maestro (carregar → menu → salvar, com o guarda `if __name__ == "__main__"`) e, nas sondas de conferência, achou dois furos: a correção da chave commitada direto na main (e sem push) e os prints fora da interface. Para o Furo 1 propôs o resgate (branch nascendo no commit que já existe + `reset --hard origin/main` + PR); para o Furo 2 propôs devolver `(baú, aviso)` em vez de imprimir. Testou os três mundos do pergaminho e o codice.py legado.
- O que mudei/decidi: resgatei o commit que tinha ido direto para a main — criei a branch nascendo nele, rebobinei a main e mandei a correção por PR — porque é necessário para respeitar as regras do Ato. E aceitei a mudança do armazenamento: ele deixa de imprimir e devolve (baú, aviso), porque é melhor para o programa em si.

## Dia 15 (4ª sessão)
- Pergunta: se a IA conseguia ler um link de artifact do Claude — e, depois que eu baixei o arquivo, o que o documento do programa (a Jornada do Escriba) dizia sobre o Ato II.
- Resposta: a IA não conseguiu ler o link (o conteúdo fica atrás do meu login; ela recebeu só a casca da página) e leu o HTML que eu baixei, extraindo o texto do arquivo. Comparando o documento com o repositório, achou três coisas que ela mesma tinha me dito errado antes: o argparse é requisito do Ato II, o PR com correções do mestre é critério separado da Sabotagem I, e o README não é critério de aceite do ato. Depois rascunhou o relatório corrigido para o mestre, que eu copiei e enviei.
- O que mudei/decidi: eu mandei o documento para a IA achando que era a melhor opção para ter certeza que estava avançando de forma correta em relação ao projeto, e com isso descobri que tinha algumas coisas faltando que precisavam ser resolvidas e reeditadas. Se eu não tivesse feito isso, o projeto ia ser entregue incompleto.

## Dia 16
- Pergunta: como se escreve argparse em Python — eu nunca tinha visto isso no curso, e no meio do caminho perguntei o que ia dentro dos parênteses vazios.
- Resposta: a IA me deu o mapa das quatro peças sem código (só os nomes e a ordem), me devolveu para tentar e, a cada erro, rodou o meu arquivo para provar — a ligação errada (chamar no módulo em vez de chamar no objeto), o `AttributeError` que prova que o `parse_args` não mora no `argparse`, e as saídas do `Namespace` nos três casos (com `--nome`, sem nada, e o `--help` que o argparse escreve sozinho). Explicou de onde vêm os valores do `parse_args` vazio (a linha de comando) e que o ponto do `parser.parse_args()` é a mesma regra do `herois.append()` do Ato I. No fim me aplicou o teste de memória do critério Modificar e, quando eu disse que não lembrava as letras, mudou o método do treino: parar de copiar olhando (isso treina o olho) e passar a tentar de memória e corrigir só o erro (isso treina a mão).
- O que mudei/decidi: decidi apagar o `teste_argparse.py` em vez de commitá-lo, porque o repositório é o programa e o diário é a memória do aprendizado — um rascunho solto na raiz viraria lixo que eu não saberia se posso apagar daqui a três semanas, e o argparse de verdade entra no `main.py` na próxima sessão. E decidi que o meu treino passa a ser de detalhe, não de conceito: tentar de memória e corrigir só o erro, em vez de copiar o arquivo várias vezes.
- Adendo (correção de rastro): a IA, conferindo o `git log` a meu pedido, achou que o Dia 15 do diário tem **duas datas de commit diferentes** — as sessões 1 a 3 em 02/10 e a 4ª sessão em 07/10 — mas o cabeçalho do dia só mostrava uma. Ela mesma tinha me oferecido a correção errada (trocar o cabeçalho para 07/10, o que estragaria as outras três sessões) e voltou atrás antes de mexer. Eu escolhi a V1.
- O que mudei/decidi: escolhi a V1 (manter o cabeçalho em 02/10 e dar data própria ao adendo da 4ª sessão) em vez da V2 (cabeçalho "02/10 a 07/10"), porque a V1 diz exatamente quais sessões aconteceram em qual dia, e a V2 esconderia isso numa faixa. O ciclo de git desta correção (branch, commit, push, PR e merge) foi rodado pela IA, porque eu estava cansado — as decisões foram minhas.

## Dia 16
- Pergunta: como se escreve argparse em Python — eu nunca tinha visto isso no curso.
- Resposta: a IA me deu o mapa das quatro peças SEM código (só os nomes e a ordem), me devolveu
  para tentar, e a cada erro rodou meu arquivo para provar — a ligação errada (chamar no módulo em
  vez do objeto), o AttributeError do parse_args, as saídas do Namespace e o --help que o argparse
  escreve sozinho. Explicou de onde vêm os valores do parse_args vazio (a linha de comando, sys.argv)
  e que o ponto do parser.parse_args() é a mesma regra do herois.append() do Ato I.
- O que mudei/decidi: eu decidi que o programa ia ser com comandos e com o menu porque assim o codice poderia ser usado e interpretado tanto para humanos e para outros programas. Também decidi em apagar o teste_argparse.py .


