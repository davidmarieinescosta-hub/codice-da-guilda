# main.py — o maestro: orquestra o ciclo do dia.
import armazenamento
import cli


def main() -> None:
    """Carrega a guilda, roda o menu e salva no fim."""
    herois = armazenamento.carregar_herois()
    cli.menu(herois)
    armazenamento.salvar_herois(herois)


if __name__ == "__main__":
    main()
