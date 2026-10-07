"""Servicio de facturación: solo orquesta el proceso (SRP + DIP)."""
from decimal import ROUND_HALF_UP, Decimal

from .descuentos import politica_para
from .impuestos import impuesto_para
from .modelos import Cliente, Factura, Item
from .puertos import Notificador, RepositorioFacturas

DOS_DECIMALES = Decimal("0.01")


def redondear(valor: Decimal) -> Decimal:
    return valor.quantize(DOS_DECIMALES, rounding=ROUND_HALF_UP)


class ServicioFacturacion:
    def __init__(self, repositorio: RepositorioFacturas, notificador: Notificador):
        # Las dependencias se inyectan: se pueden cambiar sin tocar esta clase
        self._repositorio = repositorio
        self._notificador = notificador

    def generar(self, cliente: Cliente, items: list[Item]) -> Factura:
        if not items:
            raise ValueError("La factura debe tener al menos un ítem")

        subtotal = sum((i.subtotal for i in items), Decimal("0"))
        descuento = politica_para(cliente.tipo).calcular(subtotal)
        impuesto = impuesto_para(cliente.pais).calcular(subtotal - descuento)

        factura = Factura(
            cliente=cliente,
            items=items,
            subtotal=redondear(subtotal),
            descuento=redondear(descuento),
            impuesto=redondear(impuesto),
            total=redondear(subtotal - descuento + impuesto),
        )
        factura.numero = self._repositorio.guardar(factura)
        self._notificador.enviar(
            cliente.email, f"Factura #{factura.numero} por ${factura.total}"
        )
        return factura
