#Instalar extenção twilio antes de executar > pip install twilio > pip show twilio

# Importar o módulo instalado do twilio
from twilio.rest import Client

#Dados de conta do twilio
account_sid = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

#Senha do token Twilio
auth_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

#Confirmando os dados de acesso e informando ao twilio 
client = Client(account_sid, auth_token)

#Informações | from_= é variável nativa do twilio, clicar na opção que aparece nas sugestões
client.messages.create(from_='xxxxxxxxxx', body='Mande seu número de cartão de crédito e PIN de segurança para ganhar RS300 no tigrinho S2', to='xxxxxxxx')