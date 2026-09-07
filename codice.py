herois = []
def cadastrar_heroi():
    nome = input("Nome do herói: ")
    classe = input("Classe: ")
    nivel = int(input("Nível: "))
    heroi = {"nome": nome, "classe": classe, "nivel": nivel}
    herois.append(heroi)
    print(f"{nome} entrou para a guilda!")


def listar_herois():
    for heroi in herois:
        print(f"{heroi['nome']}, {heroi['classe']}, {heroi['nivel']}, aqui estão as caracteristicas de um membro da guilda.")

