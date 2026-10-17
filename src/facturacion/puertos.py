"""Interfaces pequeñas y específicas (ISP + DIP).

El servicio depende de estas abstracciones, no de MySQL ni de SMTP.
"""

from typing import Protocol

from .modelos import Factura


class RepositorioFacturas(Protocol):
    def guardar(self, factura: Factura) -> int: ...


class Notificador(Protocol):
    def enviar(self, destinatario: str, mensaje: str) -> None: ...


class RepositorioEnMemoria:
    """Implementación simple, útil para pruebas y demos."""

    def __init__(self) -> None:
        self.facturas: list[Factura] = []

    def guardar(self, factura: Factura) -> int:
        self.facturas.append(factura)
        return len(self.facturas)


class NotificadorConsola:
    def enviar(self, destinatario: str, mensaje: str) -> None:
        print(f"[correo a {destinatario}] {mensaje}")
