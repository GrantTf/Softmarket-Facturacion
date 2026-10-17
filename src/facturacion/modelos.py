"""Entidades del dominio de facturación (sin lógica de infraestructura)."""

from dataclasses import dataclass, field
from decimal import Decimal


@dataclass(frozen=True)
class Item:
    descripcion: str
    precio: Decimal
    cantidad: int

    @property
    def subtotal(self) -> Decimal:
        return self.precio * self.cantidad


@dataclass(frozen=True)
class Cliente:
    nombre: str
    email: str
    tipo: str = "normal"  # normal | frecuente | vip
    pais: str = "CO"


@dataclass
class Factura:
    cliente: Cliente
    items: list[Item]
    subtotal: Decimal = Decimal("0")
    descuento: Decimal = Decimal("0")
    impuesto: Decimal = Decimal("0")
    total: Decimal = Decimal("0")
    numero: int | None = field(default=None)
