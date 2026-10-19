"""Congela o que o programa responde hoje, antes da Forja do Ato III.

Roda todos os comandos com os mesmos dados e grava saída, erro e código de
saída em baseline.txt. No fim do Ato III, roda de novo: se o arquivo não mudou,
o comportamento do programa também não mudou.

Uso (da raiz do repositório): python baseline.py
"""

import json
import os
import subprocess
import sys

# Os dados de teste ficam aqui, e não no herois.json: o baseline precisa ser
# reproduzível — os mesmos heróis em toda execução.
DADOS = [
    {"nome": "Aldric", "classe": "Mago", "nivel": 42},
    {"nome": "Bryn", "classe": "Ladino", "nivel": 17},
    {"nome": "Cedric", "classe": "Mago", "nivel": 60},
    {"nome": "Dara", "classe": "Clérigo", "nivel": 8},
]

COM_HEROIS = [
    (["listar"], None),
    (["buscar", "--nome", "Aldric"], None),
    (["buscar", "--nome", "Ninguem"], None),
    (["filtrar", "--classe", "Mago"], None),
    (["filtrar", "--classe", "Bárbaro"], None),
    (["numeros"], None),
    (["cadastrar", "--nome", "Elga", "--classe", "Clérigo", "--nivel", "5"], None),
    (["listar"], None),
    (["numeros"], None),
    (["buscar"], None),  # falta o --nome: o argparse recusa
    (["cadastrar", "--nome", "X", "--classe", "Mago", "--nivel", "abc"], None),
    (["--help"], None),
    ([], "sair\n"),  # o menu: a entrada "sair" faz ele terminar
]

# A guilda vazia é onde vivem as cláusulas de guarda: cada comando tem que falar.
VAZIA = [
    (["listar"], None),
    (["filtrar", "--classe", "Mago"], None),
    (["numeros"], None),
    (["buscar", "--nome", "Aldric"], None),
]

CENARIOS = [
    ("guilda com heróis", DADOS, COM_HEROIS),
    ("guilda vazia", [], VAZIA),
]


def rodar(comando: list, entrada: str | None) -> subprocess.CompletedProcess:
    """Roda o programa com o comando pedido e devolve o processo terminado."""
    ambiente = {**os.environ, "PYTHONIOENCODING": "utf-8"}
    return subprocess.run(
        [sys.executable, "main.py"] + comando,
        input=entrada,
        capture_output=True,
        text=True,
        encoding="utf-8",
        env=ambiente,
    )


def escrever_herois(herois: list) -> None:
    """Grava a lista no herois.json — o mesmo arquivo que o programa lê."""
    with open("herois.json", "w", encoding="utf-8") as arquivo:
        json.dump(herois, arquivo, ensure_ascii=False, indent=2)


def main() -> None:
    """Grava o baseline e devolve o herois.json do autor ao que era."""
    with open("herois.json", encoding="utf-8") as arquivo:
        original = arquivo.read()
    try:
        with open("baseline.txt", "w", encoding="utf-8") as saida:
            for nome, dados, comandos in CENARIOS:
                escrever_herois(dados)
                saida.write(f"=== {nome} ===\n\n")
                for comando, entrada in comandos:
                    processo = rodar(comando, entrada)
                    saida.write(f"$ python main.py {' '.join(comando)}".rstrip() + "\n")
                    saida.write(processo.stdout)
                    if processo.stderr:
                        saida.write("[erro]\n" + processo.stderr)
                    saida.write(f"[código de saída: {processo.returncode}]\n\n")
    finally:
        with open("herois.json", "w", encoding="utf-8") as arquivo:
            arquivo.write(original)


if __name__ == "__main__":
    main()
