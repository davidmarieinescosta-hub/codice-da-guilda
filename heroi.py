class Heroi:
    """Um herói da guilda."""

    def __init__(self, nome: str, classe: str, nivel: int, missoes=None):
        """Guarda os dados de um herói."""
        self.nome = nome
        self.classe = classe
        self.nivel = nivel
        if missoes is None:
            missoes = []
        self.missoes = missoes

    def atende_por(self, nome_procurado: str) -> bool:
        """Diz se este herói é o procurado."""
        return self.nome == nome_procurado

    def e_da_classe(self, classe_procurada: str) -> bool:
        """Diz se este herói é da classe pedida."""
        return self.classe == classe_procurada
