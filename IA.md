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
- O que mudei/decidi: escolhi filtrar antes dos números para fazer por etapas, construindo algo mais linear e com evolução mais organizada; e escolhi return em vez de print porque posso querer usar o resultado depois — o print mostraria e perderia. 
