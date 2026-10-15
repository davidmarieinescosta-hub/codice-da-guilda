# Codice da Guilda

O projeto é um programa de terminal em Python que registra heróis de uma guilda,
para depois organizá-los em classe e em nível.

No Ato 1 os dados viviam só na memória: fechou o programa, sumiram. No Ato 2 isso
mudou — agora eles são gravados no arquivo `herois.json`, na própria pasta, e
continuam lá na próxima vez que o programa abrir.

## Como rodar

- Python instalado (só isso — sem dependências).
- No terminal, dentro da pasta do projeto:

### Com o menu

```bash
python main.py
```

Sem nenhum comando, o programa abre o menu e pergunta o que você quer fazer.

### Com comandos

```bash
python main.py listar
python main.py buscar --nome Aldric
python main.py filtrar --classe Mago
python main.py numeros
python main.py cadastrar --nome Aldric --classe Mago --nivel 42
```

As duas portas levam às mesmas funções: o menu e os comandos chamam o mesmo
código, só mudando quem pergunta os dados.

Para ver a lista de comandos e o que cada um quer: `python main.py --help`

## O que já funciona

- **cadastrar um herói** — pelo menu ou por `python main.py cadastrar ...`;
- **listar** todos os heróis da guilda;
- **buscar** um herói escolhido pelo usuário e mostrar o seu nome;
- **filtrar** por classe e mostrar os heróis que têm aquela classe;
- **mostrar os números** — quantos são, a média de nível e o herói mais forte;
- **salvar e carregar** os dados em `herois.json`, avisando em português quando o
  arquivo ainda não existe (a guilda começa vazia) ou quando ele está quebrado.

## Como o código está organizado

Cinco arquivos, um emprego cada:

| arquivo | emprego |
|---|---|
| `main.py` | o maestro: lê a linha de comando e comanda o ciclo |
| `cli.py` | a portaria: é quem fala com o usuário (`input` e `print`) |
| `regras.py` | as regras da guilda: criar, buscar e filtrar herói |
| `relatorios.py` | conta e formata os números |
| `armazenamento.py` | o baú: lê e grava o `herois.json` |

O `codice.py` é o programa do Ato 1, de um arquivo só, guardado como história.

Obs: eu escolhi fazer o repositório em português porque todo o programa está nessa língua.
