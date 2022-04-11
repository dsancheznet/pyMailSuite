from email.message import EmailMessage

myMessage = EmailMessage()

myMessage['From']="test@gmail.com"
myMessage['To']='test2@gmail.com'
myMessage['Subject']="Hola"
myMessage.set_content( "Cuerpo del Mensaje ")
print( myMessage.as_string())
