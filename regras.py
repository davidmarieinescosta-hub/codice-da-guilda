def criar_heroi(nome: str, classe: str, nivel: int) -> dict:
    """Monta o dicionário de um herói novo."""
    return {"nome": nome, "classe": classe, "nivel": nivel}


def buscar_heroi(herois: list, nome_procurado: str) -> dict | None:
    """Devolve o herói com o nome procurado, ou None se não existir."""
    for heroi in herois:
        if heroi["nome"] == nome_procurado:
            return heroi
    return None


def filtrar_herois_por_classe(herois: list, classe_procurada: str) -> list:
    """Devolve a lista dos heróis da classe procurada."""
    aprovados = []
    for heroi in herois:
        if heroi["classe"] == classe_procurada:
            aprovados.append(heroi)
    return aprovados
