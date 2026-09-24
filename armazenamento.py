import json



def salvar_herois(herois):
    with open("herois.json", "w", encoding="utf-8") as arquivo:
        json.dump(herois, arquivo, indent=2, ensure_ascii=False)


