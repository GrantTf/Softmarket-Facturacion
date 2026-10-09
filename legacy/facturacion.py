"""
Módulo de facturación ORIGINAL de SoftMarket (antes de la refactorización).
Se conserva solo como referencia del diagnóstico: NO usar en producción.

Problemas visibles:
- Una sola clase hace todo: calcula, aplica descuentos, guarda en BD,
  envía correos e imprime (viola SRP).
- Cada nuevo tipo de cliente o impuesto obliga a editar los if/elif (viola OCP).
- Depende directamente de MySQL y de SMTP (viola DIP): imposible de probar.
"""
import os
import smtplib
import mysql.connector  # dependencia concreta "quemada" en el código


class Factura:
    def procesar(self, cliente, items, tipo_cliente, pais):
        subtotal = 0
        for i in items:
            subtotal = subtotal + i["precio"] * i["cantidad"]

        # Descuentos: cada tipo nuevo = otro elif
        if tipo_cliente == "normal":
            descuento = 0
        elif tipo_cliente == "frecuente":
            descuento = subtotal * 0.05
        elif tipo_cliente == "vip":
            descuento = subtotal * 0.10
        else:
            descuento = 0

        # Impuestos: el mismo bloque está copiado en ventas.py y cotizaciones.py
        if pais == "CO":
            iva = (subtotal - descuento) * 0.19
        elif pais == "EC":
            iva = (subtotal - descuento) * 0.15
        else:
            iva = 0

        total = subtotal - descuento + iva

        # Persistencia acoplada (credenciales en el código)
        db = mysql.connector.connect(host="localhost", user="root",
                                     password=os.environ["DB_PASSWORD"], database="softmarket")
        cur = db.cursor()
        cur.execute("INSERT INTO facturas (cliente, total) VALUES ('"
                    + cliente["nombre"] + "', " + str(total) + ")")  # SQL injection
        db.commit()

        # Notificación acoplada
        server = smtplib.SMTP("smtp.softmarket.com")
        server.sendmail("ventas@softmarket.com", cliente["email"],
                        "Su factura es de " + str(total))

        print("Factura generada: " + str(total))
        return total
