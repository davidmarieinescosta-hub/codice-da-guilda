# Relatório do Ato III — A Forja

**Para:** o mestre da Guilda
**De:** David Angelo Soares da Costa
**Data:** 2 de novembro de 2026 — Dia 24 de 90
**Entrega:** PR #41 — https://github.com/davidmarieinescosta-hub/codice-da-guilda/pull/41

---

## Sobre o Ato II

O senhor encerrou o Ato II e disse que não voltaria a ele. Tomo isso como ponto de partida e não reabro o assunto.

Registro uma coisa só, para o histórico ficar correto: o critério do Ato II falava em *um PR com
correções pedidas pelo mestre*, e a revisão do senhor aprovou sem pedir nenhuma. Eu decidi não
fabricar uma correção para fechar o critério. Fica escrito como o que foi — uma revisão externa que
aprovou. Não peço nada sobre isso; é só para o registro não mentir depois.

---

## O que o Ato III pedia, e como ficou

| Critério | Situação |
|---|---|
| Quatro classes | **feito** — `Heroi`, `Missao`, `Guilda`, `RepositorioJson` |
| Nenhuma funcionalidade nova | **feito** — nenhum comando nasceu |
| "Mesmos comandos, mesmas respostas" | **feito** — 17 comandos congelados e reconferidos |
| A `Guilda` não pode saber que JSON existe | **feito** — nenhum `open(`, `json.` ou `RepositorioJson` nela |
| Uma herança justificada | **feito** — `Repositorio` (ABC) → `RepositorioJson` |
| Uma composição justificada | **feito** — a `Guilda` recebe o repositório |
| Cinco decisões registradas | **feito** — seis, cada uma com a alternativa descartada e o custo |
| PR mostrando antes e depois | **feito** — #41, com a baseline como prova |
| Revisão do mestre e merge | **pendente** — é o que este relatório pede |

---

## O que foi entregue

**`Heroi`** — guarda nome, classe, nível e as missões. Sabe responder duas perguntas sobre si:
`atende_por(nome)` e `e_da_classe(classe)`.

**`Missao`** — nome e dificuldade. Nasceu no ato como o dado que faltava para o `Heroi` não ficar
só com três campos.

**`Guilda`** — o baú. Guarda os heróis, responde `listar`, `buscar` e `filtrar`, e manda gravar a
cada mudança.

**`Repositorio`** — o contrato, uma *ABC*: diz que quem guarda heróis precisa saber `carregar` e
`salvar`, sem dizer como.

**`RepositorioJson`** — a implementação. É a única sala que abre arquivo e a única que traduz
objeto para dicionário e de volta.

A seta de dependência aponta num sentido só, sem import circular:

```
main.py → cli.py → guilda.py → repositorio.py → heroi.py / missao.py
```

Antes, um dicionário atravessava o programa inteiro e todos sabiam de cor as chaves `"nome"`,
`"classe"` e `"nivel"`, sem que ninguém fosse dono delas. Agora cada pergunta vai para a sala que
sabe responder.

---

## A prova

No Dia 20, antes de tocar em qualquer classe, congelei a saída de **17 comandos** em dois cenários
— guilda com heróis e guilda vazia — gravando stdout, stderr e o código de saída de cada um.
Depois de *cada* commit do ato:

```
$ python baseline.py
$ git diff baseline.txt
(nada)
```

A segunda linha vazia é a prova. Se qualquer mensagem, qualquer espaço ou qualquer código de saída
tivesse mudado, apareceria ali.

**O que a baseline também revelou:** com a guilda vazia, o comando `numeros` imprime *"0, é a média
do nível da guilda"*. É um defeito antigo, achado no Dia 20 e **não corrigido** — corrigir mudaria o
comportamento, e o ato proíbe função nova. Fica registrado para o Ato IV.

---

## As seis decisões

1. **Atributos públicos para ler; métodos para comparar.** Descartei tudo privado com `get_nome()`,
   e também tudo público sem método nenhum.
2. **`Missao` com nome e dificuldade, gravada mesmo vazia.** Descartei gravar a chave só quando
   houver missão.
3. **`Repositorio` como ABC de verdade.** Descartei a classe comum com `raise NotImplementedError`.
4. **A `Guilda` recebe o repositório de fora e grava a cada mudança.** Descartei a `Guilda`
   fabricar o próprio repositório, e também gravar só no fim.
5. **As contas ficam em `relatorios.py`, como funções.** Descartei virar método da `Guilda` — ela
   viraria Deus.
6. **Apagar só o `regras.py`; manter o `armazenamento.py`.** Descartei apagar os dois — quebraria o
   `codice.py` do Ato I.

Duas eu mudei **depois de ver prova**, não por argumento. Na quarta, eu queria a `Guilda` fabricando
o repositório; a versão que fabrica não aceita um repositório de mentira no construtor e precisaria
nomear `RepositorioJson` dentro dela — o que o critério do ato proíbe. Na sexta, eu tinha decidido
apagar os dois arquivos; um `grep` antes de apagar mostrou o `codice.py` usando o `armazenamento.py`
nas linhas 71 e 75.

**O custo, com nome.** Tirar o `salvar_herois` do fim do `main()` ganhou escrita deliberada e perdeu
a **rede de segurança**: antes, ao sair de qualquer execução, memória e arquivo eram iguais por
garantia. Hoje, um método que esqueça de chamar `salvar` perde a mudança em silêncio. Em troca,
`python main.py listar` não toca no arquivo, e um `herois.json` corrompido não é sobrescrito com
`[]` — provei com o arquivo quebrado antes e depois do comando.

---

## Onde eu errei

Registro os erros porque foi a prova rodada, e não a explicação, que os consertou.

- Descrevi o `self` como "uma gaveta que guarda as informações". A gaveta é o atributo; o `self` é
  o dono dela.
- Disse que o `NameError` vinha do `return`. Vem da busca do nome: ele não é local nem global.
- Escrevi `nome = str` querendo dizer "isto é um texto". Isso faz a classe `str` virar o valor
  padrão.
- Pus o `return` dentro do `for` do `filtrar`: voltou `['Aldric']` onde deviam voltar dois heróis.
- Na conversão de volta do JSON, tratei dicionário como objeto e objeto como dicionário, três vezes
  na mesma função.
- No `cli.py`, troquei o corpo de três funções sem trocar os cabeçalhos — os parâmetros ainda se
  chamavam `herois`.
- Achei que a resposta sobre onde a gravação passou a acontecer dependia de um ato futuro. Estava no
  comportamento do programa de hoje.

Em todos os casos o erro foi de **modelo mental**, não de sintaxe. É o sinal nº 4 do programa —
entender lendo e travar escrevendo — e é o critério que eu ainda não consegui treinar sozinho.

---

## O que ainda não está pronto

- **O merge do PR #41.** Aberto e não mergeado, de propósito: o ato pede revisão, e eu não quero
  mergear o que não revisei.
- **A prova dos 15 minutos.** Digitei o `heroi.py` e o `missao.py` e mexi no `relatorios.py` e no
  `cli.py`, mas sempre com a IA por perto. Alterar uma classe sozinho, cronometrado, ainda não
  aconteceu.
- **Um arquivo solto na raiz**, `teste_subcomandos.py`, de antes do ato, sem destino decidido.
- **Conceitos sem casa no código:** `raise`, `requirements.txt`, CSV e módulos dentro de uma pasta.

---

## Os três pedidos

1. **A revisão do PR #41.** O que eu mais quero não é elogio: é o apontamento do que está errado. O
   `DECISOES.md` está no PR com as seis decisões e as alternativas descartadas, para facilitar a
   discordância.
2. **A Issue da Sabotagem I.** Ficou combinada no fim do Ato II e ainda não chegou. É o exercício de
   ler código alheio em busca de defeito — e eu não consigo inventar isso sozinho.
3. **A data do Rito de Passagem II.** Trinta minutos, tela compartilhada, quatro critérios:
   Explicar, Modificar, Decidir e Rastro. Preciso de uma data para treinar o que está fraco em vez
   de descobrir no dia.

---

## Onde estou na conta

Dia de trabalho **24 de 90**, com três atos fechados. O programa orçava até o Dia 45 para o Ato III;
fechei no 24. Medido no repositório: **116 commits em 23 dias diferentes**.

A folga não é sobra. Ela existe porque no Dia 10 desenhei a arquitetura no papel antes de escrever
código, e no Dia 20 congelei a baseline antes de mexer — e é o que vai pagar os atos pesados que vêm.

---

*David Angelo Soares da Costa · codice-da-guilda · 2 de novembro de 2026*

🤖 Generated with [Claude Code](https://claude.com/claude-code)
