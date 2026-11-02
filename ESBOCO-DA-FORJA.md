# Esboço da Forja — Ato III

> **Rascunho.** Nada aqui está decidido. Este arquivo é material para o repasse do
> Dia 22: cada seção termina numa pergunta que o autor responde, não numa resposta
> que a IA deu. Quando estiver fechado, ele vira o `DECISOES.md`.

## A regra que segura tudo

O `baseline.txt` congelou 17 respostas. A Forja pode mudar o **código** inteiro; não
pode mudar **nenhuma linha** do que o programa responde. Toda decisão abaixo passa
por esse teste.

## Os nove acessos — o que eles ensinaram

`Select-String -Path regras.py, relatorios.py -Pattern 'heroi\['` devolveu 9 acessos a
3 chaves: `nome`, `classe`, `nivel`.

- **Todos são leitura.** Ninguém escreve no herói. O herói de hoje é um saco de dados
  que os outros abrem quando querem.
- **Nenhuma chave tem comportamento.** `nome`, `classe` e `nivel` são valores. Isso
  significa que o `Heroi` do Ato III **não** vai nascer cheio de métodos: ele nasce
  com dados e ganha método só onde há uma **regra** que o dono do dado deveria saber
  responder.

## As quatro salas

| Sala | Emprego | O que ela pode saber |
|---|---|---|
| `Heroi` | um herói: o que ele é e o que ele responde sobre si | os próprios campos |
| `Missao` | uma missão de um herói | os próprios campos |
| `Guilda` | o baú de heróis e as perguntas que se fazem a ele | heróis; **nunca** JSON |
| `RepositorioJson` | guardar e carregar | arquivos e a forma do JSON |

## Decisão 1 — o que o `Heroi` é

```python
class Heroi:
    def __init__(self, nome, classe, nivel, missoes=None): ...
    def atende_por(self, nome_procurado) -> bool: ...   # regras.py:9
    def e_da_classe(self, classe_procurada) -> bool: ... # regras.py:18
```

Os três campos continuam **atributos públicos** (`heroi.nome`, `heroi.nivel`): o
`relatorios.py` lê e formata, e isso não é segredo. O que vira método é só a
**comparação** — porque comparar é uma regra, e amanhã a comparação pode ficar
esperta (sem acento, sem caixa) sem ninguém de fora mudar.

- **Decidi:** atributos para leitura, métodos para comparação.
- **Porque:** a gaveta aberta de fora (`heroi["nome"]`) é um contrato invisível; o
  método é um contrato que o editor mostra e o erro denuncia na hora.
- **Descartei:** `Heroi` só com dados e as buscas em `regras.py` — funciona hoje, mas
  espalha a regra do herói por quem o usa.

> **Pergunta para amanhã:** `nivel` pode ser 0? 100? Negativo? Se houver regra, ela
> é do `Heroi` e **muda a resposta** — logo, é outro PR, não este.

## Decisão 2 — a `Missao`, que não tem comando

O programa não tem comando de missão. Ela existe no Ato III mesmo assim, porque é a
**composição** exigida: um herói **tem** missões.

- **Decidi:** `Heroi` guarda `missoes: list[Missao]`, vazia por padrão, e o programa
  nunca a preenche.
- **Porque:** o Ato III pede uma composição justificada, e "um herói tem missões" é a
  verdade do domínio mesmo sem comando. O contrário — inventar um comando novo — seria
  funcionalidade nova, proibida pelo ato e capaz de mexer no baseline.
- **Descartei:** deixar a `Missao` de fora até existir comando. Mais honesto com
  "nada de novo", mas o ato nomeia a classe como entregável.
- **Cuidado registrado:** se `missoes` for gravada no JSON, o formato do `herois.json`
  muda. Decisão adiada para o repasse: gravar `missoes` (e aceitar o campo novo) ou
  não gravar enquanto estiver vazia.

> **Pergunta para amanhã:** uma missão tem nome e **dificuldade**? O que mais? Quem
> inventa uma missão?

## Decisão 3 — a herança: `Repositorio` → `RepositorioJson`

```python
class Repositorio:                  # o contrato
    def carregar(self) -> tuple[list, str | None]: ...
    def salvar(self, herois) -> None: ...

class RepositorioJson(Repositorio): # o que sabe JSON
    ...
```

- **Decidi:** herdar de um `Repositorio` abstrato.
- **Porque:** a `Guilda` só conhece o **contrato** (carregar/salvar). Amanhã um
  `RepositorioCsv` entra sem tocar em uma linha da `Guilda` — e a herança é
  justificada por **substituição**: o filho serve em qualquer lugar onde o pai serve.
- **Descartei:** `RepositorioJson` sem pai, com a `Guilda` pedindo essa classe direto.
  Menos código, mas prende a `Guilda` a uma implementação — o que é exatamente o
  pecado que o ato proíbe.

> **Pergunta para amanhã:** o contrato deveria ser uma classe vazia (`class
> Repositorio: pass`) ou uma `ABC` que **impede** o filho de esquecer um método?

## Decisão 4 — a composição: a `Guilda` tem um repositório

```python
class Guilda:
    def __init__(self, repositorio):      # recebe, não fabrica
        self.repositorio = repositorio
        self.herois = repositorio.carregar()[0]
```

- **Decidi:** a `Guilda` **recebe** o repositório de fora, em vez de criar
  `RepositorioJson()` por dentro.
- **Porque:** é o que torna a regra do ato verificável — dentro do `guilda.py` não pode
  existir `open(` nem `json.`; e no teste dá para passar um repositório de mentira.
- **Descartei:** a `Guilda` criar o seu próprio repositório. Constrói rápido, mas cola
  as duas salas e torna o "não sabe JSON" uma promessa em vez de um fato.

> **Pergunta para amanhã:** a `Guilda` guarda a lista em memória e salva a cada
> mudança, ou devolve os heróis e deixa o `main.py` decidir quando salvar? A resposta
> muda o `main.py` e deve aparecer no `DECISOES.md`.

## Decisão 5 — onde ficam as buscas e as contas

- Buscar e filtrar viram métodos da `Guilda` (perguntas ao baú), que delegam a
  comparação ao `Heroi`.
- As contas (`mostrar_numeros`) e a formatação (`formatar_lista`) **ficam** em
  `relatorios.py` — continuam sendo a sala que conta e veste números, agora lendo
  `heroi.nivel` em vez de `heroi["nivel"]`.
- A portaria (`cli.py`) continua falando. A regra continua devolvendo dados.

> **Pergunta para amanhã:** `relatorios.py` some e vira método da `Guilda`? A
> alternativa tem nome próprio: **objeto de relatório**. Escolher agora é escolher
> quantas salas o Ato III terá.

## O que fica de fora, de propósito

- Corrigir a média 0 na guilda vazia (achado do Dia 20) — mudaria o baseline.
- Qualquer comando novo, inclusive de missão.
- `requirements.txt`, CSV, pasta de módulos: continuam sem casa, e nada aqui os pede.

## Lista do repasse (Dia 22)

- [ ] explicar, sem olhar, por que `heroi["nome"]` é pior que `heroi.atende_por(nome)`
- [ ] dizer de quem é a `Missao` e por que ela existe sem comando
- [ ] desenhar as quatro salas e as setas (tem / é um)
- [ ] responder as cinco perguntas marcadas acima
- [ ] escrever o `DECISOES.md` na forma "decidi X, porque Y, descartei Z"
- [ ] só então: escrever a primeira classe, explicar em voz alta, commitar
