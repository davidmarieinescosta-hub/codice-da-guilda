import json



def salvar_herois(herois: list) -> None:
    """Grava a lista de heróis no arquivo herois.json."""
    with open("herois.json", "w", encoding="utf-8") as arquivo:
        json.dump(herois, arquivo, indent=2, ensure_ascii=False)


def carregar_herois() -> tuple[list, str | None]:
    """Carrega os heróis do pergaminho e devolve (baú, aviso) — aviso é None quando tudo corre bem."""
    try:
        with open("herois.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo), None
    except FileNotFoundError:
        return [], "Nenhum pergaminho encontrado — a guilda começa vazia."
    except json.JSONDecodeError:
        return [], "O pergaminho está rasgado — a guilda começa vazia."



    


    


