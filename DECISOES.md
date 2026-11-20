# Decisões da Forja (Ato III)

Cinco decisões escritas na forma que o ato pede: **decidi X, porque Y, descartei Z**.
As frases de "porque" são do autor — se alguma não disser o que ele pensou, a frase
está errada e o documento também.

## A regra que segura tudo

O `baseline.txt` congelou 17 respostas. A Forja pode reescrever o código inteiro; não
pode mudar **nenhuma linha** do que o programa responde. Toda decisão abaixo passa
por esse teste.

---

## 1. O `Heroi`: dados à mostra, comparação por método

**Decidi** que o `Heroi` guarda `nome`, `classe` e `nivel` como atributos públicos, e
que só a **comparação** vira método: `atende_por(nome)` e `e_da_classe(classe)`.

```python
heroi.atende_por(nome_procurado)     # em vez de  heroi["nome"] == nome_procurado
heroi.e_da_classe(classe_procurada)  # em vez de  heroi["classe"] == classe_procurada
```

**Porque** comparar é uma regra, e regra mora em quem é dono do dado: se amanhã a
busca tiver que ignorar acento ou caixa, muda dentro do `Heroi` e mais nada. Ler o
dado (`heroi.nivel`) pode continuar aberto — o `relatorios.py` só lê e formata, e
esconder isso seria cerimônia sem ganho.

**Descartei** manter o dicionário com as buscas no `regras.py`: funciona hoje, mas a
chave `"nome"` é um contrato invisível — o editor não avisa, o erro só aparece quando
aquela linha roda, e a mesma regra fica espalhada por quem usa o herói.

### Regra conhecida e adiada

**Decidi** registrar "nível não pode ser negativo" sem aplicá-la.

**Porque** aplicá-la agora faria o programa recusar `--nivel -5`, que hoje grava — e
o ato exige respostas idênticas.

**Descartei** validar já (quebra o baseline) e descartei não registrar (a regra se
perde e alguém a reinventa diferente). Endereço marcado: `Heroi.__init__`, no dia em
que o ato permitir mudar comportamento — e nesse dia ela vai precisar de `raise`.

---

## 2. A `Missao`, que existe sem comando

**Decidi** que existe a classe `Missao`, com `nome` e `dificuldade` (1 a 5), e que o
`Heroi` guarda uma lista delas — vazia por padrão. O programa nunca cria uma missão.

**Porque** o ato exige uma composição justificada, e "um herói tem missões" é verdade
do domínio mesmo sem comando. Uma classe que nunca aparece na tela não muda nenhuma
resposta do `baseline`: é modelagem, não funcionalidade nova.

**Descartei** inventar um comando de missão (seria funcionalidade nova, proibida pelo
ato) e descartei deixar a `Missao` de fora até existir comando (o ato a nomeia como
entregável). Descartei também a versão completa, com `concluida` e `recompensa`: cada
campo é uma decisão a mais num programa que não os usa.

**Sobre o arquivo:** o `herois.json` passa a ter o campo `missoes`. **Decidi** gravá-lo
sempre, mesmo vazio.

**Porque** um arquivo com uma forma só é mais fácil de ler do que um com duas: quem lê
nunca precisa perguntar "será que o campo está aí?".

**Descartei** gravar só quando houvesse missão — criaria duas formas do mesmo registro.
Heróis antigos não têm o campo; **essa diferença é problema do `RepositorioJson`**, que
resolve na entrada e entrega tudo igual para dentro.

---

## 3. A herança: `Repositorio` abstrato → `RepositorioJson`

**Decidi** que `Repositorio` é uma **ABC** (`abc.ABC`, com `@abstractmethod` em
`carregar` e `salvar`), e que `RepositorioJson` herda dela.

**Porque** um filho incompleto falha **no nascimento** — `TypeError: Can't instantiate
abstract class ...` — no começo do programa, antes de o usuário digitar uma letra.

**Descartei** a classe vazia (`class Repositorio: pass`): o objeto incompleto nasce
feliz e o `AttributeError` só aparece no meio de uma operação real. Descartei também
`raise NotImplementedError` dentro dos métodos — mesmo problema, só que mais tarde: o
erro espera o método ser chamado.

A herança é justificada por **substituição**: o filho serve em qualquer lugar onde o
pai serviria. É isso que permite um `RepositorioCsv` amanhã sem tocar na `Guilda`.

---

## 4. A composição: a `Guilda` tem um repositório, e ele vem de fora

**Decidi** que a `Guilda` **recebe** o repositório no construtor:

```python
guilda = Guilda(RepositorioJson())
```

**Porque** é o que torna verificável o critério do ato — "a `Guilda` não pode saber que
existe JSON". Dentro do `guilda.py` não pode haver `open(`, `json.` nem o nome
`RepositorioJson`. Com o repositório de fora, a mesma `Guilda` aceita um repositório de
mentira e pode ser testada sem tocar em disco.

**Descartei** a `Guilda` fabricar o seu (`self.repositorio = RepositorioJson()`):
constrói mais rápido, mas o arquivo passa a **nomear** o JSON — a promessa deixa de ser
fato.

**Sobre quando gravar:** **decidi** que a `Guilda` grava **a cada mudança** (o
`cadastrar` chama o repositório na hora).

**Porque** cada ação do programa cadastra um herói só — é atômica —, e gravar na hora
protege o trabalho do usuário.

**O custo, que tem nome:** o `main()` deixou de ter o `salvar_herois(herois)` no fim, e com
ele foi embora a **rede de segurança** que garantia "o que está em memória é o que está no
arquivo" ao sair de toda execução. Hoje, uma mudança feita por um método que esqueça de
chamar `salvar` morre em silêncio no fim do programa. Em troca, nenhuma escrita acontece
por acidente: `python main.py listar` não toca no arquivo, e um `herois.json` corrompido
não é sobrescrito com `[]` — prova rodada em 02/11, com o arquivo quebrado antes e depois
do `listar`.

**Descartei** gravar só no fim, como o programa faz hoje: uma falha no meio do menu
apagaria tudo o que foi feito na sessão.

---

## 5. As contas continuam no `relatorios.py`

**Decidi** que o `relatorios.py` continua existindo como módulo de funções
(`mostrar_numeros`, `formatar_lista`), recebendo lista de heróis.

**Porque** o ato pede quatro classes, e já há trabalho suficiente nelas; a mudança no
`relatorios.py` é de duas linhas (`heroi["nivel"]` vira `heroi.nivel`). A `Guilda`
responde perguntas sobre os heróis (buscar, filtrar); as contas ficam na sala que já
sabe contar — e a lei do Ato II continua valendo: **a regra devolve dados, a portaria
fala**.

**Descartei** transformar as contas em métodos da `Guilda`: ela acumularia emprego
(guardar, buscar, contar e formatar) até virar Deus. Descartei também a classe
`Relatorio`: justificável, mas é uma quinta sala num ato que nomeou quatro.

---

## 6. Apagar só o `regras.py` e manter o `armazenamento.py` pelo `codice.py`

**Decidi** apagar o `regras.py` — ninguém mais o importa depois da religação — e **manter**
o `armazenamento.py`, com um comentário no topo dizendo de quem ele é empregado: o
`codice.py` do Ato I.

**Porque** a primeira versão desta decisão era apagar os dois, e ela estava errada por
informação incompleta: o `codice.py` usa `armazenamento.carregar_herois()` e
`salvar_herois()` nas linhas 71 e 75. Apagar teria deixado um arquivo do repositório que
não abre — e o `codice.py` é a história do Ato I, a comparação que este ato quer mostrar
no PR. Reescrever o `codice.py` com as classes novas seria pior: a "história" passaria a
mostrar o programa de hoje.

**Descartei** apagar os dois (quebraria o `codice.py`) e reescrever o `codice.py`
(apagaria a comparação antes/depois). O custo aceito é um arquivo a mais.

---

## O que fica de fora, de propósito

- Corrigir a média 0 na guilda vazia (achado do Dia 20) — mudaria o baseline.
- Qualquer comando novo, inclusive de missão.
- Validar nível negativo — registrado acima, com endereço.
- `requirements.txt`, CSV e pasta de módulos: seguem sem casa, e nada aqui os pede.



## Onde fica a linha entre dado ruim e programa errado?

- Um dado ruim pode ser classificado quando, por exemplo, alguem editou o arquivo herois.json na mão, ou se o arquivo foi truncado no meio da gravação, se o JSON veio de um outro programa. Pode acontecer com qualquer um, porém o programa tem que sobreviver da mesmo forma.
- Programa errado: o código tem uma suposição falsa. Isso não se trata — se grita, porque esconder o bug é pior que o bug.



### Decisão 1 — Caso 1

**Decidi:** Deixar funcionando como está, está de acordo com o que foi decido.
**Porque:** porque foi decidido antes que o programa deveria agir dessa forma caso o pergaminho tivesse zero bytes.
**Descartei:** não queria fazer de outra forma, já que desse jeito já está dando certo, sescartei deixar sem except, para o arquivo vazio dar traceback.
**Prova:** `Set-Content herois.json '' -Encoding ascii -NoNewline` e depois `python main.py listar`

```
O pergaminho está rasgado — a guilda começa vazia.
Nenhum herói na guilda.
[código de saída: 0]
```

### Decisão 2 — Caso 2 

**Decidi:** Deixar do jeito que está. 
**Porque:** porque literalmente esá funcionandon, não a nada pra mudar.
**Descartei:** porque não vou mudar algo que já está dando certo,descartei exigir que o pergaminho tenha pelo menos um herói.
**Prova:** `Set-Content herois.json '[]' -Encoding ascii -NoNewline` e depois `python main.py listar`

```
Nenhum herói na guilda.
[código de saída: 0]
```

Sem linha de aviso: lista vazia é pergaminho válido, não pergaminho com defeito.



### Decisão 3 — a raiz do pergaminho tem que ser uma lista (casos 3, 4 e 5)

**Decidi:** Conferir a forma na entrada, e isso é uma condição para os três `null`, `{}`, `{"Aldric": 42}`.

**Porque:** A conferência mora num lugar só (no carregador), a mensagem se diz o que esperava, e isso impede do program "mentir" e esconder um erro que pode acabar explodindo no final. Esta validação também pode esconder um defeito meu: se o salvar gravar o arquivo errado, o carregar do dia seguinte vai dizer 'o pergaminho é inválido', e eu vou investigar o arquivo em vez do meu código.

**Descartei:**
- deixar como está — o mesmo defeito dá respostas opostas conforme o dicionário esteja vazio ou não o que não pode ser mantido.
- tratar caso a caso no _para_heroi — três remendos para um defeito só.
- aceitar o dicionário e adivinhar o 42 — inventa um segundo formato que o salvar nunca escreve, e não tem como adivinhar um dado, a resposta vira um jogo de adivinha.
**Prova:** as três execuções, cada uma com `Set-Content herois.json '<conteúdo>' -Encoding ascii -NoNewline` e depois `python main.py listar`

`null`
```
O pergaminho não é uma lista de heróis — a guilda começa vazia.
Nenhum herói na guilda.
[código de saída: 0]
```

`{}`
```
O pergaminho não é uma lista de heróis — a guilda começa vazia.
Nenhum herói na guilda.
[código de saída: 0]
```

`{"Aldric": 42}`
```
O pergaminho não é uma lista de heróis — a guilda começa vazia.
Nenhum herói na guilda.
[código de saída: 0]
```







### Decisão 4 — Caso 6 e 7 

**Decidi:** Tudo ou nada, o arquivo vai ficar intacto no disco. Se Abrib o Notepad, ainda tem chançe de consertá-lo. O programa não toca no que não entendeu. 
**Porque:** Porque se salvar o que der, o programa vai estar carregando um dado que sabe estar incompleto. UM heroi com defeito invalida o pergaminho inteiro, o arquivo não é tocado, para poder ser consertado.
**Descartei:** salvar o que der — carregar os heróis válidos e avisar quantos caíram. Recusei porque o programa regrava o arquivo inteiro a cada cadastro (guilda.py:16), então o primeiro salvar depois de uma carga parcial apagaria para sempre os heróis descartados. A evidência some junto com o dado.
**Prova:** as três execuções, cada uma com `Set-Content herois.json '<conteúdo>' -Encoding ascii -NoNewline` e depois `python main.py listar`

herói sem `nivel` (o Bryn), com um herói válido na mesma lista (o Aldric)
```
O pergaminho tem um herói com defeito (herói sem o campo 'nivel') — a guilda começa vazia.
Nenhum herói na guilda.
[código de saída: 0]
```

`nivel` como texto
```
O pergaminho tem um herói com defeito (o campo 'nivel' não é um número) — a guilda começa vazia.
Nenhum herói na guilda.
[código de saída: 0]
```

missão incompleta dentro de um herói válido
```
O pergaminho tem um herói com defeito (uma missão do herói está incompleta) — a guilda começa vazia.
Nenhum herói na guilda.
[código de saída: 0]
```

Vale em qualquer profundidade: um herói malformado, ou uma missão incompleta
dentro dele, recusa o pergaminho inteiro — o arquivo no disco não é tocado.
