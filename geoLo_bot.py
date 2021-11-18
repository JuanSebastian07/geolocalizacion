import urllib.request
#Importamos json por que la informacion esta en formato json
import json
import requests


lista=[]

def main():
    objetivo='https://ipinfo.io/json'
    contenido=urllib.request.urlopen(objetivo)
    cargajson=json.loads(contenido.read())
    #print(cargajson)
    for dato in cargajson:
        print(dato)
        mensaje=dato + " : " + str(cargajson[dato])
        lista.append(mensaje)
    return lista
        
def mandar_datos(): 
    enviar=json.dumps(main(), indent=2)
    bot_token = 'Tu token'
    bot_chatID = 'chat ID'#Grupo
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + enviar
    requests.get(send_text)

main()
mandar_datos()



















