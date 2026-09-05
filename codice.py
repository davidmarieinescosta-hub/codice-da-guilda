def cadastrar_heroi():
    herois = []
    nome = input("Nome do herói: ")
    classe = input("Classe: ")
    nivel = int(input("Nível: "))
    heroi = {"nome": nome, "classe": classe, "nivel": nivel}
    herois.append(heroi)
    print(f"{nome} entrou para a guilda!")


def listar_herois():
    for heroi in herois:
        print(f"{heroi}, é um dos membros da guilda!")