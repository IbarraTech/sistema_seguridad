import smtplib


def envio_correos():
    # Configuración
    remitente = " sistemaseguridadvivienda@gmail.com"
    destinatario = ["oscar.marino.ibarra@correounivalle.edu.co",
                    "oscaribarracardona@gmail.com", "adriana.olave@correounivalle.edu.co"]
    asunto = "ALERTA: SENSOR ACTIVO"
    mensaje = "Hola se ha activado la alarma "

    # Configurar el servidor SMTP de Gmail y el puerto
    servidor_smtp = "smtp.gmail.com"
    puerto_smtp = 587

    # Conectar al servidor SMTP
    smtp = smtplib.SMTP(servidor_smtp, puerto_smtp)
    smtp.starttls()

    # Autenticarse en la cuenta de Gmail (Asegúrate de permitir el acceso a aplicaciones menos seguras)
    correo_gmail = "sistemaseguridadvivienda@gmail.com"
    clave_gmail = "rfnqwclsphzbfeov"
    smtp.login(correo_gmail, clave_gmail)

    # Crear el mensaje del correo
    mensaje_correo = f"Subject: {asunto}\n\n{mensaje}"

    # Enviar el correo electrónico
    smtp.sendmail(remitente, destinatario, mensaje_correo)

    # Cerrar la conexión SMTP
    smtp.quit()


# Llamar a la función para enviar el correo
# envio_correos()
