# cli.py — a portaria: fala com o usuário.
from guilda import Guilda
from heroi import Heroi
import relatorios


def exibir_aviso(aviso: str | None) -> None:
    """Imprime o aviso de carregamento, se houver algum."""
    if aviso is not None:
        print(aviso)


def exibir_lista(guilda: Guilda) -> None:
    """Imprime a lista da guilda, um herói por linha."""
    herois = guilda.listar()
    if len(herois) == 0:
        print("Nenhum herói na guilda.")
        return
    for linha in relatorios.formatar_lista(herois):
        print(linha)


def exibir_busca(guilda: Guilda, nome: str) -> None:
    """Imprime o herói achado, ou avisa que ele não existe."""
    resultado = guilda.buscar(nome)
    if resultado is None:
        print("Herói não encontrado.")
    else:
        print(resultado.nome)


def exibir_filtro(guilda: Guilda, classe: str) -> None:
    """Imprime os heróis da classe pedida."""
    aprovados = guilda.filtrar(classe)
    if len(aprovados) == 0:
        print(f"Nenhum herói na guilda com a classe de {classe}.")
        return
    for linha in relatorios.formatar_lista(aprovados):
        print(linha)


def exibir_numeros(guilda: Guilda) -> None:
    """Imprime o total, a média e o mais forte da guilda."""
    numeros = relatorios.mostrar_numeros(guilda.listar())
    print(f"{numeros['quantos']} heróis na guilda")
    print(f"{numeros['media']}, é a média do nível da guilda")
    if numeros['mais_forte'] is None:
        print("Nenhum herói na guilda.")
    else:
        print(f"{numeros['mais_forte']}, é o mais forte")


def cadastrar_heroi(guilda: Guilda, nome: str, classe: str, nivel: int) -> None:
    """Cria o herói, guarda no baú e avisa que ele entrou."""
    heroi = Heroi(nome, classe, nivel)
    guilda.cadastrar(heroi)
    print(f"{nome} entrou para a guilda!")


def menu(guilda: Guilda) -> None:
    """Roda o menu da guilda até o usuário escolher sair."""
    exibir_aviso(guilda.aviso)
    opções = input("o que vc deseja fazer? cadastrar, listar, buscar, filtrar, números ou sair? ")
    while opções != "sair":
        if opções == "cadastrar":
            nome = input("Nome do herói: ")
            classe = input("Classe: ")
            # O nível vem do teclado: pode vir letra. Enquanto não vier
            # número, pergunta de novo — sem perder nome e classe já lidos.
            while True:
                entrada = input("Nível: ")
                try:
                    nivel = int(entrada)
                    break
                except ValueError:
                    print("Isso não é um número. Tente de novo.")
            cadastrar_heroi(guilda, nome, classe, nivel)
        elif opções == "listar":
            exibir_lista(guilda)
        elif opções == "buscar":
            nome = input("Qual nome quer buscar? ")
            exibir_busca(guilda, nome)
        elif opções == "filtrar":
            classe = input("Qual classe quer filtrar? ")
            exibir_filtro(guilda, classe)
        elif opções == "números":
            exibir_numeros(guilda)
        else:
            # Sem este else, uma opção desconhecida volta ao menu em silêncio.
            print(f'A opção "{opções}" não existe.')
        opções = input("o que vc deseja fazer? cadastrar, listar, buscar, filtrar, números ou sair? ")
    print("agora você conhece a guilda")
