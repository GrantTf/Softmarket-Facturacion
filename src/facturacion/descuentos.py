"""Estrategias de descuento (OCP + LSP).

Para agregar un nuevo tipo de cliente se crea una clase nueva y se registra;
no se modifica el código existente.
"""

from abc import ABC, abstractmethod
from decimal import Decimal


class PoliticaDescuento(ABC):
    @abstractmethod
    def calcular(self, subtotal: Decimal) -> Decimal:
        """Devuelve el valor del descuento (nunca negativo ni mayor al subtotal)."""


class SinDescuento(PoliticaDescuento):
    def calcular(self, subtotal: Decimal) -> Decimal:
        return Decimal("0")


class DescuentoPorcentual(PoliticaDescuento):
    def __init__(self, porcentaje: Decimal):
        if not Decimal("0") <= porcentaje <= Decimal("1"):
            raise ValueError("El porcentaje debe estar entre 0 y 1")
        self._porcentaje = porcentaje

    def calcular(self, subtotal: Decimal) -> Decimal:
        return subtotal * self._porcentaje


POLITICAS_POR_TIPO: dict[str, PoliticaDescuento] = {
    "normal": SinDescuento(),
    "frecuente": DescuentoPorcentual(Decimal("0.05")),
    "vip": DescuentoPorcentual(Decimal("0.10")),
}


def politica_para(tipo_cliente: str) -> PoliticaDescuento:
    return POLITICAS_POR_TIPO.get(tipo_cliente, SinDescuento())
