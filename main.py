# main.py — o maestro: orquestra o ciclo do dia.
import argparse

import armazenamento
import cli


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


def executar(herois: list, args: argparse.Namespace) -> None:
    """Roda o comando escolhido na linha de comando."""
    if args.comando == "listar":
        cli.exibir_lista(herois)
    elif args.comando == "buscar":
        cli.exibir_busca(herois, args.nome)
    elif args.comando == "filtrar":
        cli.exibir_filtro(herois, args.classe)
    elif args.comando == "numeros":
        cli.exibir_numeros(herois)
    elif args.comando == "cadastrar":
        cli.cadastrar_heroi(herois, args.nome, args.classe, args.nivel)


def main() -> None:
    """Carrega a guilda, atende o comando (ou abre o menu) e salva no fim."""
    parser = montar_parser()
    args = parser.parse_args()

    herois, aviso = armazenamento.carregar_herois()

    if args.comando is None:
        cli.menu(herois, aviso)
    else:
        cli.exibir_aviso(aviso)
        executar(herois, args)

    armazenamento.salvar_herois(herois)


if __name__ == "__main__":
    main()
