# Arquitetura da Guilda — Ato II

Documento de decisão de arquitetura do Ato II (Dia 10, 23/09/2026).

## As quatro salas

| Sala | Arquivo | Responsabilidade |
|---|---|---|
| Portaria | `cli.py` | fala com o usuário: menu, input, print |
| Conselho | `regras.py` | decide: montar o herói, buscar, filtrar |
| Relatórios | `relatorios.py` | conta: os números da guilda |
| Pergaminho | `armazenamento.py` | lembra: salvar e carregar do arquivo |

## O ciclo do dia do baú

1. **Abre** — o armazenamento lê o pergaminho (arquivo) e entrega o baú à portaria.
2. **Roda** — a cada pedido do usuário, a portaria empresta o baú (por parâmetro) ao conselho ou aos relatórios.
3. **Fecha** — a portaria devolve o baú ao armazenamento, que grava no pergaminho.

## Decisões e porquês

- **Fala e decisão separadas.** Nenhum `print` fora da interface (critério 2 do Ato). As funções atuais misturam os dois empregos — cada uma será partida: o pedaço que fala vai para a portaria, o pedaço que decide vai para o conselho.
- **O baú não tem dono.** Ele passa por todo o castelo e volta para o armazenamento. As salas recebem o baú de presente, pelo parâmetro (função pura), e devolvem o resultado — nunca vão buscar o baú sozinhas.
- **Só o armazenamento toca no pergaminho.** Ler no início, gravar no fim. Ninguém mais mexe no arquivo.

## O caminho de um herói (Ato III — 27/11/2026)

O Ato III mudou esta fotografia: o `regras.py` foi apagado e o `armazenamento.py` não é
mais o caminho — hoje o dono do arquivo é o `RepositorioJson`.

`main.py` é o maestro: lê o comando e monta `Guilda(RepositorioJson())`. A `Guilda` nasce
chamando `carregar()`, e o `__init__` guarda os heróis **e** o aviso (se o pergaminho não
existia ou estava estragado).

No cadastro, a portaria lê três `str` (nome, classe, nível), cria um `Heroi` e entrega à
`Guilda`. Ela faz duas coisas, nesta ordem: **guarda na memória** (`herois.append`) e
**manda gravar** (`repositorio.salvar`). A `Guilda` nunca toca no arquivo — entre ela e o
`herois.json` não existe seta direta: existe `Guilda → RepositorioJson → arquivo`.

As quatro trocas de forma do dado:

| quando | troca | onde |
|---|---|---|
| ao carregar | `dict → Heroi` | `RepositorioJson._para_heroi` |
| ao cadastrar | `str → Heroi` | `cli.menu` → `Heroi(...)` |
| ao gravar | `Heroi → dict` | `RepositorioJson._para_dicionario` |
| ao gravar | `dict → texto` | `json.dump` |

