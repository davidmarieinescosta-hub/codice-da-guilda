from heroi import Heroi
from repositorio import Repositorio


class Guilda:
    """O baú da guilda: guarda os heróis e responde perguntas sobre eles."""

    def __init__(self, repositorio: Repositorio):
        """Guarda o repositório e carrega os heróis que já existiam."""
        self.repositorio = repositorio
        self.herois, self.aviso = repositorio.carregar()

    def cadastrar(self, heroi: Heroi) -> None:
        """Acrescenta o herói ao baú e grava na hora."""
        self.herois.append(heroi)
        self.repositorio.salvar(self.herois)

    def buscar(self, nome: str) -> Heroi | None:
        """Devolve o herói com aquele nome, ou None se não existir."""
        for heroi in self.herois:
            if heroi.atende_por(nome):
                return heroi
        return None

    def listar(self) -> list:
        """Devolve todos os heróis da guilda."""
        return self.herois

    def filtrar(self, classe: str) -> list:
        """Devolve os heróis daquela classe."""
        aprovados = []
        for heroi in self.herois:
            if heroi.e_da_classe(classe):
                aprovados.append(heroi)
        return aprovados

    def _parecido(self, procurado: str, candidatos: list) -> str | None:
        """Devolve o candidato que difere do procurado só por espaço ou maiúscula."""
        alvo = procurado.strip().casefold()
        for candidato in candidatos:
            if candidato.strip().casefold() == alvo:
                return candidato
        return None

    def nome_parecido(self, nome: str) -> str | None:
        """Devolve o nome de um herói parecido com o procurado, se houver."""
        return self._parecido(nome, [heroi.nome for heroi in self.herois])

    def classe_parecida(self, classe: str) -> str | None:
        """Devolve a classe parecida com a procurada, se houver."""
        return self._parecido(classe, [heroi.classe for heroi in self.herois])
