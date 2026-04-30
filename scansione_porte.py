import socket

print("=" * 50)
print("        PORT SCANNER TCP")
print("=" * 50)
print("Questo programma controlla quali porte")
print("sono APERTE o CHIUSE su un host.")
print("=" * 50)

host = input("Inserire un indirizzo ip: ")

porte = [20, 21, 22, 23, 25, 53, 80, 110, 143,
         445, 3306, 3389, 5432, 5900, 8080, 8443, 27017]


print(f"Scansione porte su {host}...\n")

for porta in porte:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    risultato = sock.connect_ex((host, porta))

    if risultato == 0:
        print(f"[APERTA] Porta {porta}")
    else:
        print(f"[CHIUSA] Porta {porta}")

    sock.close()