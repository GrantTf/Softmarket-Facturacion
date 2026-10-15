"""Notificador por correo (SM-15, en desarrollo). Implementa el protocolo Notificador."""
import smtplib


class NotificadorEmail:
    def __init__(self, servidor: str, remitente: str):
        self._servidor = servidor
        self._remitente = remitente

    def enviar(self, destinatario: str, mensaje: str) -> None:
        with smtplib.SMTP(self._servidor) as smtp:
            smtp.sendmail(self._remitente, destinatario, mensaje)
