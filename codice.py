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
        print(f"{heroi['nome']}, {heroi['classe']}, level: {heroi['nivel']} ")
        


def buscar_heroi(nome_procurado):
    for heroi in herois:
        if heroi["nome"] == nome_procurado:
            print(heroi['nome'])                   
       

def filtrar_herois_por_classe(classe_procurada):
    aprovados = []
    for heroi in herois:
        if heroi["classe"] == classe_procurada:
          aprovados.append(heroi)
    return aprovados



def mostrar_numeros():
    print(f'{len(herois)} heróis na guilda')
    total = 0
    mais_forte = 0
    nome_mais_forte = ""
    for heroi in herois:
        total = total + heroi['nivel']
        if heroi['nivel'] > mais_forte:
            mais_forte = heroi['nivel']
            nome_mais_forte = heroi['nome']
    media = total / len(herois)
    print(f'{media}, é a média do nível da guilda')
    print(f'{nome_mais_forte}, nível {mais_forte}, é o mais forte')




    
  
          
            








    