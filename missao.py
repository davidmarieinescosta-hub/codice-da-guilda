class Missao:
    """Uma missão da guilda."""

    def __init__(self, nome: str, dificuldade: int):
        """Guarda os dados de uma missão."""
        self.nome = nome
        self.dificuldade = dificuldade
