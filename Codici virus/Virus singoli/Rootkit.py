import ctypes

def hide_process():
    # Usa ctypes per chiamare le API di basso livello di Windows e nascondere il processo
    ctypes.windll.kernel32.SetFileAttributesW("malicious_process.exe", 0x02)
