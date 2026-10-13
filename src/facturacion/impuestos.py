"""Cálculo de impuestos por país (SRP + OCP).

Antes este bloque estaba copiado en 3 módulos; ahora vive en un solo lugar.
"""
from abc import ABC, abstractmethod
from decimal import Decimal


class CalculadoraImpuesto(ABC):
    @abstractmethod
    def calcular(self, base: Decimal) -> Decimal: ...


class IVA(CalculadoraImpuesto):
    def __init__(self, tarifa: Decimal):
        self._tarifa = tarifa

    def calcular(self, base: Decimal) -> Decimal:
        return base * self._tarifa


TARIFAS_POR_PAIS: dict[str, CalculadoraImpuesto] = {
    "CO": IVA(Decimal("0.19")),
    "EC": IVA(Decimal("0.15")),
}


def impuesto_para(pais: str) -> CalculadoraImpuesto:
    return TARIFAS_POR_PAIS.get(pais, IVA(Decimal("0")))
