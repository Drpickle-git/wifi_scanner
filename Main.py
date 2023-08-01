import socket
import os

os.system('cls' if os.name == 'nt' else 'clear')

print("  _    _ ___________ _____             _____ _____  ___  _   _ _   _ ___________  ")
print(" | |  | |_   _|  ___|_   _|           /  ___/  __ \/ _ \| \ | | \ | |  ___| ___ \ ")
print(" | |  | | | | | |_    | |______ ______\ `--.| /  \/ /_\ \  \| |  \| | |__ | |_/ / ")
print(" | |/\| | | | |  _|   | |______|______|`--. \ |   |  _  | . ` | . ` |  __||    /  ")
print(" \  /\  /_| |_| |    _| |_            /\__/ / \__/\ | | | |\  | |\  | |___| |\ \  ")
print("  \/  \/ \___/\_|    \___/            \____/ \____|_| |_|_| \_|_| \_|____/\_| \_|  ")
print(" ")

print("Appuyez sur Entrée pour démarrer le programme...")
input()

os.system('cls' if os.name == 'nt' else 'clear')


print("  _    _ ___________ _____             _____ _____  ___  _   _ _   _ ___________  ")
print(" | |  | |_   _|  ___|_   _|           /  ___/  __ \/ _ \| \ | | \ | |  ___| ___ \ ")
print(" | |  | | | | | |_    | |______ ______\ `--.| /  \/ /_\ \  \| |  \| | |__ | |_/ / ")
print(" | |/\| | | | |  _|   | |______|______|`--. \ |   |  _  | . ` | . ` |  __||    /  ")
print(" \  /\  /_| |_| |    _| |_            /\__/ / \__/\ | | | |\  | |\  | |___| |\ \  ")
print("  \/  \/ \___/\_|    \___/            \____/ \____|_| |_|_| \_|_| \_|____/\_| \_|  ")
print(" ")

def scan_network():
    try:
       
        subnet = "192.168.1."
        start_range = 1
        end_range = 255

        print("Scan du réseau en cours...\n")

        
        for i in range(start_range, end_range + 1):
            ip = subnet + str(i)
            try:
                host_name = socket.gethostbyaddr(ip)[0]
                print(f"IP: {ip}, Nom: {host_name}")
            except socket.herror:
                pass

    except Exception as e:
        print("Une erreur s'est produite lors du scan du réseau.")
        print(" ")
        print("Merci de réesayer.")

if __name__ == "__main__":
    scan_network()


print(" ")
print("Pour acceder aux interfaces web des appareills: http://xxx.xxx.x.xx.")
