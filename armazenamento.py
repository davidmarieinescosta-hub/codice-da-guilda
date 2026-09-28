import json



def salvar_herois(herois: list) -> None:
    """Grava a lista de heróis no arquivo herois.json."""
    with open("herois.json", "w", encoding="utf-8") as arquivo:
        json.dump(herois, arquivo, indent=2, ensure_ascii=False)


def carregar_herois() -> list:
    """Carrega os heróis do pergaminho; baú vazio se ele não existir ou estiver rasgado."""
    try:
        with open("herois.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print("Nenhum pergaminho encontrado — a guilda começa vazia.")
        return []
    except json.JSONDecodeError:
        print("O pergaminho está rasgado — a guilda começa vazia.")
        return []



    


    


