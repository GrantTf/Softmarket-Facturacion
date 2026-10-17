from decimal import Decimal

import pytest

from facturacion.modelos import Cliente, Item
from facturacion.puertos import RepositorioEnMemoria
from facturacion.servicio import ServicioFacturacion


class NotificadorFalso:
    def __init__(self):
        self.enviados = []

    def enviar(self, destinatario, mensaje):
        self.enviados.append((destinatario, mensaje))


@pytest.fixture
def servicio():
    return ServicioFacturacion(RepositorioEnMemoria(), NotificadorFalso())


def items_basicos():
    return [Item("Licencia", Decimal("100.00"), 2)]  # subtotal 200


def test_cliente_normal_en_colombia(servicio):
    f = servicio.generar(Cliente("Ana", "ana@x.com"), items_basicos())
    assert f.descuento == Decimal("0.00")
    assert f.impuesto == Decimal("38.00")
    assert f.total == Decimal("238.00")


def test_cliente_vip_recibe_10_por_ciento(servicio):
    f = servicio.generar(Cliente("Luis", "l@x.com", tipo="vip"), items_basicos())
    assert f.descuento == Decimal("20.00")
    assert f.total == Decimal("214.20")  # (200-20)*1.19


def test_pais_sin_tarifa_no_cobra_iva(servicio):
    f = servicio.generar(Cliente("Eva", "e@x.com", pais="US"), items_basicos())
    assert f.impuesto == Decimal("0.00")


def test_factura_sin_items_lanza_error(servicio):
    with pytest.raises(ValueError):
        servicio.generar(Cliente("Ana", "ana@x.com"), [])


def test_se_guarda_y_se_notifica():
    repo, notif = RepositorioEnMemoria(), NotificadorFalso()
    ServicioFacturacion(repo, notif).generar(
        Cliente("Ana", "ana@x.com"), items_basicos()
    )
    assert len(repo.facturas) == 1
    assert notif.enviados[0][0] == "ana@x.com"
