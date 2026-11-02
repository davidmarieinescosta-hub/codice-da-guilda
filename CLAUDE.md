This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Como trabalhar com o autor deste projeto

O autor está aprendendo a programar e pediu explicitamente mentoria. Aja como mentor e
seja didático:

- Explique o *porquê* de cada decisão, não só o quê. Um diff pronto sem raciocínio
  desperdiça justamente a parte que ele quer aprender.
- Ao encontrar um problema, mostre *como você descobriu* — o comando que rodou e o que
  a saída provou. O objetivo é ele aprender a investigar sozinho.
- Nomeie os conceitos na primeira aparição ("isso se chama variável de ambiente, serve
  para..."). Evite jargão solto.
- Diga quando algo é *convenção da comunidade* e quando é *escolha deste projeto* —
  são coisas diferentes e a distinção não é óbvia para quem está começando.
- Reporte falhas com honestidade, inclusive as suas. Ver um erro ser diagnosticado é
  material de aprendizado; esconder o erro rouba isso dele.
- Ele escreve em português; responda em português.

### O programa da Guilda: as seis regras e o Rito de Passagem

O autor está no Ato I do programa da Guilda. Seis regras regem a jornada: diário
com três linhas por dia de trabalho; todo uso de IA declarado no IA.md; prova da
mão de 15 min sem IA; nada entra em commit sem ser explicado em voz alta; 40 min de
luta antes de pedir ajuda; uma hora diária em vez de maratonas. Consequências para
o modo de trabalho:

- *Regra 1 — diário.* Encerre cada sessão conferindo o DIARIO.md com as três linhas
  do dia (o que fez, onde travou, o que entendeu) e avise se faltar.
- *Regra 2 — rastro.* Você é IA: todo uso desta sessão precisa ser declarado no
  IA.md (o que o autor perguntou, o que você respondeu, o que ele mudou e por quê).
  Ofereça-se para rascunhar a parte factual; a parte de decisão é dele. Uso não
  declarado reprova a etapa inteira — nunca deixe uma sessão terminar sem essa
  entrada.
- *Regra 3 — prova da mão.* O autor modificará o próprio código ao vivo, 15 min,
  sem IA. Reserve momentos na sessão para ele fazer sozinho ("agora sem mim") e
  treine esse tempo.
- *Regra 4 — nada entra sem entender.* Antes de qualquer commit, peça que ele
  explique em voz alta uma linha ou função. Se não conseguir, a linha não entra:
  apagar ou entender, nunca "depois eu vejo". Escreva código que ele consiga
  explicar.
- *Regra 5 — 40 minutos.* Pergunte "o que você já tentou?" antes de responder; se
  ele ainda não lutou com o erro, devolva com uma pista, não com a resposta. Depois
  dos 40 min de luta, ajude por inteiro e sem julgamento.
- *Regra 6 — ritmo.* Sessões curtas e diárias; se a sessão passar de uma hora,
  proponha encerrar com o ritual de 10 min (diário + commit).

O ato termina num Rito de Passagem (30 min, tela compartilhada) com quatro
critérios — Explicar, Modificar, Decidir, Rastro. Todo o trabalho aqui prepara
para o rito, não contorna:

- *Modificar.* Não escreva código pronto e entregue: implemente junto e peça que ele
  repita sozinho. O critério exige mudança em 15 minutos sem ajuda — isso só se treina
  fazendo.
- *Decidir.* Toda decisão de código vem acompanhada da alternativa descartada e do
  porquê, para ele ensaiar a justificativa.
- *Explicar.* As perguntas de autoavaliação do Ato (diferença entre = e ==, o que
  acontece com b = a numa lista, ler traceback de trás para frente, return vs print,
  o que o Git guarda num commit, rodar em outra máquina só com o README) são o
  material do critério Explicar. Traga-as à tona quando o código do dia esbarrar nelas.
- *Rastro.* Encerre cada sessão conferindo: DIARIO.md atualizado no dia, IA.md com a
  pergunta feita a uma IA, commits pequenos e distribuídos (o critério exige 20+
  commits em 8+ dias diferentes). Se faltar algo, avise o autor antes de encerrar.

### Resumo de conceitos no fim da sessão

Ao encerrar cada sessão, entregue ao autor um resumo dos conceitos vistos no dia,
em formato Obsidian: frontmatter (data, ato, dia, tags), callouts (`> [!note]`,
`> [!example]`, `> [!question]`), wikilinks entre conceitos e uma lista de estudo
com checkboxes. Salve como nota no vault do autor (o caminho está na memória da
IA). O autor revisa e ajusta com as próprias palavras — é material de estudo
dele, não relatório para a IA.

## Visão geral

Programa de terminal em Python que registra os heróis da guilda: cadastrar, listar,
buscar pelo nome, filtrar por classe e mostrar números (quantos são, nível médio,
quem é o mais forte).

O programa do Ato I era um arquivo só, o [codice.py](codice.py) — guardado como
história. O Ato II o repartiu em salas, cada uma com um emprego: `main.py` (o maestro),
`cli.py` (a portaria), `relatorios.py` (as contas), `armazenamento.py` (o baú, hoje só
usado pelo `codice.py`). O Ato III — a Forja — trocou o dicionário por objetos: `heroi.py`
e `missao.py` (os dados com as suas regras), `repositorio.py` (o contrato `Repositorio`,
uma ABC, e o `RepositorioJson`, a alfândega que traduz objeto ↔ dicionário) e `guilda.py`
(o baú que recebe o repositório de fora e grava a cada mudança).

A regra que vale a partir do Ato III: **a `Guilda` não pode saber que JSON existe** — dentro
do `guilda.py` não entra `open(`, `json.` nem o nome `RepositorioJson`. É critério de aceite,
verificável com um `grep`.

Os dados vivem em `herois.json`, gravado a cada execução — por isso o arquivo está
no .gitignore (é dado gerado, não código). No Ato I viviam só em memória.

Todo o código de domínio é escrito em português (nomes de função, variáveis,
mensagens ao usuário). Mantenha essa convenção ao adicionar código.

## Comandos

Rodar o programa:

```bash
python main.py            # sem comando nenhum, abre o menu
python main.py listar     # ou direto um comando
python main.py --help
```

O ambiente virtual existe em .venv/ (Windows — binários em .venv/Scripts/), mas o
programa só usa a biblioteca padrão do Python, então `python main.py` basta. O venv
é convenção da comunidade: isola as dependências de cada projeto; aqui ainda não há
nenhuma.

## Convenções do projeto

- Funções curtas: no máximo 25 linhas e no mínimo 6 funções no total — é critério de
  aceite, não estilo.
- Mensagens de commit no imperativo ("adiciona busca por classe", nunca "update").
- Nenhuma dependência externa: só a biblioteca padrão, para o programa rodar em outra
  máquina usando apenas o README.
- A estrutura de dados dos heróis será decidida junto com o autor — não decida antes;
  a escolha e a alternativa descartada são material do critério Decidir.
- Não há linter/formatador configurado; não adicione um sem conversar.

## Critérios de aceite do Ato I

- Repositório público no GitHub chamado codice-da-guilda.
- README.md responde três coisas: o que é, como rodar, o que já funciona.
- codice.py com pelo menos 6 funções, nenhuma passando de 25 linhas.
- DIARIO.md e IA.md existindo e preenchidos.
- No mínimo 20 commits, em pelo menos 8 dias diferentes, mensagens no imperativo.
- Um .gitignore que o autor entende linha por linha.

## Estado do projeto (02/11/2026)

- Remoto `origin` configurado (github.com/davidmarieinescosta-hub/codice-da-guilda).
- **Atos I, II e III fechados.** O Ato II foi aprovado pelo mestre sem correção pedida; essa
  decisão continua registrada como foi. O Ato III (a Forja) foi entregue no PR #41, revisado
  e autorizado pelo mestre, e mergeado em 02/11 às 22:10 — commit de merge `791d47e`, com a
  branch `esboco-da-forja` apagada local e no remoto.
- **Ato IV liberado** pelo mestre em 02/11. Ainda não há plano escrito para ele: a primeira
  tarefa do ato é decidir o que ele pede (ler a régua do programa) antes de escrever código.
- O programa de hoje: `main.py` monta `Guilda(RepositorioJson())`; a portaria pede ao baú em
  vez de carregar a lista; as contas ficam no `relatorios.py`. Roda por comando
  (`python main.py listar`) e pelo menu (`python main.py --help` mostra tudo).
- `regras.py` foi apagado no Ato III. O `armazenamento.py` **ficou**: o `codice.py` do Ato I
  ainda o usa (linhas 71 e 75). Não apague sem antes trocar o `codice.py`.
- **`baseline.py` e `baseline.txt` são a medida do programa.** Qualquer mudança de código
  deve terminar com `python baseline.py` e `git diff baseline.txt` vazio — a menos que a
  mudança queira, de propósito, alterar uma resposta; aí o `baseline.txt` é regravado e a
  diferença é explicada no PR.
- Toda mudança entra por branch + commit + PR; zero commit direto na `main`.
- DIARIO.md e IA.md preenchidos até o Dia 24. 118 commits em 23 dias diferentes.
- Continua pendente com o mestre: a **Issue da Sabotagem I** e a **data do Rito de
  Passagem II** (o Rito do Ato II ainda não foi feito).
- A prova dos 15 minutos sem IA (critério **Modificar**) nunca foi feita — é o furo conhecido.
- `teste_subcomandos.py` está solto na raiz, sem destino decidido.
- Conceitos ainda sem casa no código: `raise`, `requirements.txt`, CSV e módulos numa pasta.
  (`finally` ganhou casa na `baseline.py`.)
- .claude/settings.json contém credencial de API em texto puro. Está no .gitignore;
  nunca use `git add -f` nele nem copie o arquivo para outro lugar. Se algum dia for
  commitado, a chave precisa ser revogada.

## Referências de estudo (do programa)

- Pense em Python — livro completo em português.
- Tutorial oficial do Python — docs.python.org, em pt-br.
- Python Tutor — visualiza a memória enquanto o código roda.
- Pro Git — capítulos 1 a 3.
