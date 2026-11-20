import json
from abc import ABC, abstractmethod

from heroi import Heroi
from missao import Missao


class PergaminhoInvalido(Exception):
    """Um herói do pergaminho não tem a forma que o programa espera."""


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
        if not isinstance(dicionarios, list):
            return [], "O pergaminho não é uma lista de heróis — a guilda começa vazia."

        try:
            return [self._para_heroi(d) for d in dicionarios], None
        except PergaminhoInvalido as erro:
            return [], f"O pergaminho tem um herói com defeito ({erro}) — a guilda começa vazia."

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
        if not isinstance(dicionario, dict):
            raise PergaminhoInvalido("um item do pergaminho não é um herói")

        for campo in ("nome", "classe", "nivel"):
            if campo not in dicionario:
                raise PergaminhoInvalido(f"herói sem o campo '{campo}'")

        if not isinstance(dicionario["nivel"], int):
            raise PergaminhoInvalido("o campo 'nivel' não é um número")

        missoes = []
        for uma_missao in dicionario.get("missoes", []):
            if not isinstance(uma_missao, dict):
                raise PergaminhoInvalido("uma missão do herói não é um objeto")
            if "nome" not in uma_missao or "dificuldade" not in uma_missao:
                raise PergaminhoInvalido("uma missão do herói está incompleta")
            missoes.append(Missao(uma_missao["nome"], uma_missao["dificuldade"]))
        return Heroi(
            dicionario["nome"],
            dicionario["classe"],
            dicionario["nivel"],
            missoes,
        )

