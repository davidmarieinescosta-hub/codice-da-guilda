# relatorios.py — a sala que conta e veste os números.


def mostrar_numeros(herois: list) -> dict:
    """Devolve o total, a média de nível e o mais forte da guilda."""
    if len(herois) == 0:                       # o guarda da porta — decisão A
        return {"quantos": 0, "media": 0, "mais_forte": None}
    total = 0                                  # o seu cofre do Dia 6, intacto
    # None = "ainda não vi nenhum herói". Nenhum nível válido é None, então
    # ele não colide com dado de verdade — com 0, o herói mais forte de nível
    # 0 (ou negativo) nunca entrava na disputa.
    mais_forte = None
    nome_mais_forte = ""
    for heroi in herois:
        total = total + heroi.nivel
        if mais_forte is None or heroi.nivel > mais_forte:
            mais_forte = heroi.nivel
            nome_mais_forte = heroi.nome
    return {"quantos": len(herois), "media": total / len(herois), "mais_forte": nome_mais_forte}


def formatar_lista(herois: list) -> list:
    """Devolve a listagem da guilda pronta para exibição."""
    linhas = []
    for heroi in herois:
        linhas.append(f"{heroi.nome}, {heroi.classe}, nível: {heroi.nivel}")
    return linhas
