import socket
import os
import colorama


os.system('cls' if os.name == 'nt' else 'clear')

colorama.init(autoreset=True)

print(colorama.Fore.RED + "  _    _ ___________ _____             _____ _____  ___  _   _ _   _ ___________   ")
print(colorama.Fore.RED + " | |  | |_   _|  ___|_   _|           /  ___/  __ \/ _ \| \ | | \ | |  ___| ___ \  ")
print(colorama.Fore.RED + " | |  | | | | | |_    | |______ ______\ `--.| /  \/ /_\ \  \| |  \| | |__ | |_/ /  ")
print(colorama.Fore.RED + " | |/\| | | | |  _|   | |______|______|`--. \ |   |  _  | . ` | . ` |  __||    /   ")
print(colorama.Fore.RED + " \  /\  /_| |_| |    _| |_            /\__/ / \__/\ | | | |\  | |\  | |___| |\ \   ")
print(colorama.Fore.RED + "  \/  \/ \___/\_|    \___/            \____/ \____|_| |_|_| \_|_| \_|____/\_| \_|  ")
print(colorama.Fore.RESET + " ")


print("Appuyez sur Entrée pour démarrer le programme...")
input()

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
