import socket
import datetime
import logging
from pytz import timezone

author_name = "Eryk Kołodziejczyk"
author_port = 8080
# Konfiguracja loggera
logging.basicConfig(filename='server.log', level=logging.INFO)

# Funkcja zapisująca informacji o logach
def log_startup():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logging.info(f"Start serwera: {timestamp}, autor: {author_name}, port: {author_port}\n")


# Funkcja zwracająca informacje o kliencie na podstawie jego adresu IP
def get_client_info(client_ip):
    client_time = datetime.datetime.now(timezone('UTC')).astimezone(timezone('Europe/Warsaw'))
    client_info = f"Adres IP klienta: {client_ip}\n"
    client_info += f"Czas lokalny klienta: {client_time.strftime('%Y-%m-%d %H:%M:%S')}"
    return client_info

# Funkcja obsługująca połączenie z klientem
def handle_client_connection(client_socket):
    client_address = client_socket.getpeername()[0]
    print(f"Połączono z klientem o adresie IP: {client_address}")

    # Generowanie strony informacyjnej
    client_info = get_client_info(client_address)
    response = (f"HTTP/1.1 200 OK\nContent-Type: text/html\n\n"
                f"<html>"
                    f"<body>"
                        f"<p>{client_info}</p>"
                    f"</body>"
                f"</html>")

    # Wysłanie odpowiedzi do klienta
    client_socket.sendall(response.encode())
    client_socket.close()

 # Funkcja tworząca działanie serwera na zdefiniowanym porcie
def main():
    server_port = 8080
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', server_port))
    server_socket.listen(5)
    print(f"Serwer nasłuchuje na porcie {server_port}")

    log_startup()

    try:
        while True:
            client_socket, address = server_socket.accept()
            handle_client_connection(client_socket)
    finally:
        server_socket.close()


if __name__ == "__main__":
    main()
