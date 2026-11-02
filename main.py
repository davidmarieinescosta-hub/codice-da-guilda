# main.py — o maestro: orquestra o ciclo do dia.
import argparse

import cli
from guilda import Guilda
from repositorio import RepositorioJson


def montar_parser() -> argparse.ArgumentParser:
    """Monta o parser com os comandos da guilda."""
    parser = argparse.ArgumentParser(description="A guilda dos heróis.")
    sub = parser.add_subparsers(dest="comando")

    sub.add_parser("listar", help="lista os heróis da guilda")

    buscar = sub.add_parser("buscar", help="busca um herói pelo nome")
    buscar.add_argument("--nome", required=True, help="o nome do herói")

    filtrar = sub.add_parser("filtrar", help="filtra os heróis por classe")
    filtrar.add_argument("--classe", required=True, help="a classe desejada")

    sub.add_parser("numeros", help="mostra os números da guilda")

    cadastrar = sub.add_parser("cadastrar", help="cadastra um herói novo")
    cadastrar.add_argument("--nome", required=True, help="o nome do herói")
    cadastrar.add_argument("--classe", required=True, help="a classe do herói")
    cadastrar.add_argument("--nivel", type=int, required=True, help="o nível do herói")

    return parser


def executar(guilda: Guilda, args: argparse.Namespace) -> None:
    """Roda o comando escolhido na linha de comando."""
    if args.comando == "listar":
        cli.exibir_lista(guilda)
    elif args.comando == "buscar":
        cli.exibir_busca(guilda, args.nome)
    elif args.comando == "filtrar":
        cli.exibir_filtro(guilda, args.classe)
    elif args.comando == "numeros":
        cli.exibir_numeros(guilda)
    elif args.comando == "cadastrar":
        cli.cadastrar_heroi(guilda, args.nome, args.classe, args.nivel)


def main() -> None:
    """Abre a guilda, atende o comando (ou o menu) — ela grava a cada mudança."""
    parser = montar_parser()
    args = parser.parse_args()

    guilda = Guilda(RepositorioJson())

    if args.comando is None:
        cli.menu(guilda)
    else:
        cli.exibir_aviso(guilda.aviso)
        executar(guilda, args)


if __name__ == "__main__":
    main()
