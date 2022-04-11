from email.message import EmailMessage

myMessage = EmailMessage()

myMessage['From']="dominik.sanchez@gmail.com"
myMessage['To']='avenchara@gmail.com'
myMessage['Subject']="Hola"
myMessage.set_content( "Cuerpo del Mensaje ")
print( myMessage.as_string())
