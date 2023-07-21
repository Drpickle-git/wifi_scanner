import socket

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
