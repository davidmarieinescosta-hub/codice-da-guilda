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

## O que fica de fora, de propósito

- Corrigir a média 0 na guilda vazia (achado do Dia 20) — mudaria o baseline.
- Qualquer comando novo, inclusive de missão.
- Validar nível negativo — registrado acima, com endereço.
- `requirements.txt`, CSV e pasta de módulos: seguem sem casa, e nada aqui os pede.
