import json
from abc import ABC, abstractmethod

from heroi import Heroi
from missao import Missao


class Repositorio(ABC):
    """O contrato de quem guarda e carrega heróis."""

    @abstractmethod
    def carregar(self) -> tuple[list, str | None]:
        """Devolve (lista de heróis, aviso)."""

    @abstractmethod
    def salvar(self, herois: list) -> None:
        """Grava a lista de heróis."""


class RepositorioJson(Repositorio):
    """Guarda os heróis num arquivo JSON."""

    def salvar(self, herois: list) -> None:
        """Grava a lista de heróis no arquivo."""
        dicionarios = [self._para_dicionario(h) for h in herois]
        with open("herois.json", "w", encoding="utf-8") as arquivo:
            json.dump(dicionarios, arquivo, indent=2, ensure_ascii=False)

    def carregar(self) -> tuple[list, str | None]:
        """Carrega os heróis do pergaminho e devolve (lista, aviso)."""
        try:
            with open("herois.json", "r", encoding="utf-8") as arquivo:
                dicionarios = json.load(arquivo)
        except FileNotFoundError:
            return [], "Nenhum pergaminho encontrado — a guilda começa vazia."
        except json.JSONDecodeError:
            return [], "O pergaminho está rasgado — a guilda começa vazia."
        return [self._para_heroi(d) for d in dicionarios], None

    def _para_dicionario(self, heroi: Heroi) -> dict:
        """Transforma um Heroi no dicionário que vai para o JSON."""
        missoes = []
        for missao in heroi.missoes:
            missoes.append({"nome": missao.nome, "dificuldade": missao.dificuldade})
        return {
            "nome": heroi.nome,
            "classe": heroi.classe,
            "nivel": heroi.nivel,
            "missoes": missoes,
        }

    def _para_heroi(self, dicionario: dict) -> Heroi:
        """Transforma um dicionário do JSON num Heroi."""
        missoes = []
        for uma_missao in dicionario.get("missoes", []):
            missoes.append(Missao(uma_missao["nome"], uma_missao["dificuldade"]))
        return Heroi(
            dicionario["nome"],
            dicionario["classe"],
            dicionario["nivel"],
            missoes,
        )

