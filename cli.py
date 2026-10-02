# cli.py — a portaria: fala com o usuário.
import regras
import relatorios


def menu(herois: list, aviso: str | None) -> None:
    """Roda o menu da guilda até o usuário escolher sair."""
    if aviso is not None:
        print(aviso)
    opções = input("o que vc deseja fazer? cadastrar, listar, buscar, filtrar, números ou sair? ")
    while opções != "sair":
        if opções == "cadastrar":
            nome = input("Nome do herói: ")
            classe = input("Classe: ")
            nivel = int(input("Nível: "))
            heroi = regras.criar_heroi(nome, classe, nivel)
            herois.append(heroi)
            print(f"{nome} entrou para a guilda!")
        elif opções == "listar":
            for linha in relatorios.formatar_lista(herois):
                print(linha)
        elif opções == "buscar":
            nome = input("Qual nome quer buscar? ")
            resultado = regras.buscar_heroi(herois, nome)
            if resultado is None:
                print("Herói não encontrado.")
            else:
                print(resultado['nome'])
        elif opções == "filtrar":
            classe = input("Qual classe quer filtrar? ")
            aprovados = regras.filtrar_herois_por_classe(herois, classe)
            for linha in relatorios.formatar_lista(aprovados):
                print(linha)
        elif opções == "números":
            numeros = relatorios.mostrar_numeros(herois)
            print(f"{numeros['quantos']} heróis na guilda")
            print(f"{numeros['media']}, é a média do nível da guilda")
            if numeros['mais_forte'] is None:
                print("Nenhum herói na guilda.")
            else:
                print(f"{numeros['mais_forte']}, é o mais forte")

        opções = input("o que vc deseja fazer? cadastrar, listar, buscar, filtrar, números ou sair? ")
    print("agora você conhece a guilda")
