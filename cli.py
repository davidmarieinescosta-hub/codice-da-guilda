# cli.py — a portaria: fala com o usuário.
import regras
import relatorios


def exibir_aviso(aviso: str | None) -> None:
    """Imprime o aviso de carregamento, se houver algum."""
    if aviso is not None:
        print(aviso)


def exibir_lista(herois: list) -> None:
    """Imprime a lista da guilda, um herói por linha."""
    if len(herois) == 0:
        print("Nenhum herói na guilda.")
        return
    for linha in relatorios.formatar_lista(herois):
        print(linha)


def exibir_busca(herois: list, nome: str) -> None:
    """Imprime o herói achado, ou avisa que ele não existe."""
    resultado = regras.buscar_heroi(herois, nome)
    if resultado is None:
        print("Herói não encontrado.")
    else:
        print(resultado['nome'])


def exibir_filtro(herois: list, classe: str) -> None:
    """Imprime os heróis da classe pedida."""
    aprovados = regras.filtrar_herois_por_classe(herois, classe)
    if len(aprovados) == 0:
        print(f"Nenhum herói na guilda com a classe de {classe}.")
        return
    for linha in relatorios.formatar_lista(aprovados):
        print(linha)


def exibir_numeros(herois: list) -> None:
    """Imprime o total, a média e o mais forte da guilda."""
    numeros = relatorios.mostrar_numeros(herois)
    print(f"{numeros['quantos']} heróis na guilda")
    print(f"{numeros['media']}, é a média do nível da guilda")
    if numeros['mais_forte'] is None:
        print("Nenhum herói na guilda.")
    else:
        print(f"{numeros['mais_forte']}, é o mais forte")


def cadastrar_heroi(herois: list, nome: str, classe: str, nivel: int) -> None:
    """Cria o herói, guarda no baú e avisa que ele entrou."""
    heroi = regras.criar_heroi(nome, classe, nivel)
    herois.append(heroi)
    print(f"{nome} entrou para a guilda!")


def menu(herois: list, aviso: str | None) -> None:
    """Roda o menu da guilda até o usuário escolher sair."""
    exibir_aviso(aviso)
    opções = input("o que vc deseja fazer? cadastrar, listar, buscar, filtrar, números ou sair? ")
    while opções != "sair":
        if opções == "cadastrar":
            nome = input("Nome do herói: ")
            classe = input("Classe: ")
            nivel = int(input("Nível: "))
            cadastrar_heroi(herois, nome, classe, nivel)
        elif opções == "listar":
            exibir_lista(herois)
        elif opções == "buscar":
            nome = input("Qual nome quer buscar? ")
            exibir_busca(herois, nome)
        elif opções == "filtrar":
            classe = input("Qual classe quer filtrar? ")
            exibir_filtro(herois, classe)
        elif opções == "números":
            exibir_numeros(herois)
        opções = input("o que vc deseja fazer? cadastrar, listar, buscar, filtrar, números ou sair? ")
    print("agora você conhece a guilda")
