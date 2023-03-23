from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP
from os import environ, getcwd, path

def enviar_correo(destinatarios, titulo, cuerpo):
    mensaje = MIMEMultipart()
    email_emisor = environ.get('EMAIL_SENDER')
    password_email_emisor = environ.get('PASSWORD_SENDER')

    mensaje['Subject'] = titulo

    mensaje.attach(MIMEText(cuerpo))

    emisor = SMTP('smtp.gmail.com', 587) 

    emisor.starttls()
    emisor.login(user = email_emisor, password= password_email_emisor)

    emisor.sendmail(from_addr= email_emisor, to_addrs= destinatarios, msg=mensaje.as_string())

    emisor.quit()

def enviar_correo_adjuntos(destinatarios, titulo):
    cuerpo = 'Por favor, revisar los archivos adjuntos'
    mensaje = MIMEMultipart()
    email_emisor = environ.get('EMAIL_SENDER')
    password_email_emisor = environ.get('PASSWORD_SENDER')

    mensaje['Subject'] = titulo

    mensaje.attach(MIMEText(cuerpo))
    ruta = path.join(getcwd(), 'utils', 'maxcold.jpeg')
    with open(ruta, 'rb') as archivo:
        print(archivo)
        archivo = MIMEApplication(archivo.read(), Name = 'maxcold.jpeg')

    archivo['Content-Disposition'] = 'attachment; filename=maxcold.jpeg'
    mensaje.attach(archivo)

    emisor = SMTP('smtp.gmail.com', 587) 

    emisor.starttls()
    emisor.login(user = email_emisor, password= password_email_emisor)

    emisor.sendmail(from_addr= email_emisor, to_addrs= destinatarios, msg=mensaje.as_string())

    emisor.quit()
