# Codice da Guilda

O projeto é um programa de terminal em Python que registra heróis de uma guilda,
para depois organizá-los em classe e em nível.

No Ato 1 os dados viviam só na memória: fechou o programa, sumiram. No Ato 2 isso
mudou — agora eles são gravados no arquivo `herois.json`, na própria pasta, e
continuam lá na próxima vez que o programa abrir. No Ato 3 o programa foi reescrito
em objetos, sem mudar nenhum comando nem nenhuma resposta.

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

Um arquivo por emprego:

| arquivo | emprego |
|---|---|
| `main.py` | o maestro: lê a linha de comando e comanda o ciclo |
| `cli.py` | a portaria: é quem fala com o usuário (`input` e `print`) |
| `guilda.py` | o baú: guarda os heróis, responde listar/buscar/filtrar e grava a cada mudança |
| `heroi.py` | o herói: nome, classe, nível e missões; sabe se é o procurado e se é de uma classe |
| `missao.py` | a missão: nome e dificuldade |
| `repositorio.py` | o contrato de quem grava (`Repositorio`) e a versão em JSON (`RepositorioJson`) |
| `relatorios.py` | conta e formata os números |

A `guilda.py` não sabe que o JSON existe: quem traduz objeto para dicionário e de volta é o
`repositorio.py`. Se essa separação se perder, o teste é um `grep` por `json` dentro da
`guilda.py` — não pode haver nenhum.

O `codice.py` é o programa do Ato 1, de um arquivo só, guardado como história. Ele ainda usa
o `armazenamento.py`, que por isso continua no projeto.

### A medida

`python baseline.py` roda 17 comandos em dois cenários e grava as respostas em
`baseline.txt`. Depois de qualquer mudança, `git diff baseline.txt` deve sair vazio — é assim
que se prova que o programa responde o mesmo de antes.

Obs: eu escolhi fazer o repositório em português porque todo o programa está nessa língua.
