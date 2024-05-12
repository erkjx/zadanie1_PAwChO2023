# zadanie1_PAwChO2023

#Podpunkt 1: main.py

import socket
import datetime
import logging
from pytz import timezone

author_name = "Eryk Kołodziejczyk"
author_port = 8080

# Konfiguracja loggera
logging.basicConfig(filename='server.log', level=logging.INFO)

# Funkcja zapisująca informacje o logach
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


#Podpunkt 2: Dockerfile
# Ustawienie obrazu bazowego
FROM python:3.9

# Ustawienie katalogu roboczego
WORKDIR /app

# Skopiowanie kodu źródłowego do kontenera
COPY main.py .

# Instalacja zależności
RUN pip install pytz

# Dodanie informacji o autorze
LABEL author="Eryk Kołodziejczyk"

# Ustawienie zmiennej środowiskowej z numerem portu
ENV PORT=8080

# Uruchomienie serwera po uruchomieniu kontenera
CMD ["python", "main.py"]


#Podpunkt 3
  a)
  Polecenie: docker build -t nazwa obrazu .
             docker build -t zad1 .
  ![image](https://github.com/erkjx/zadanie1_PAwChO2023/assets/129630909/49d15878-bea9-41ae-8c7e-1f030328930e)

  b)
  Polecenie: docker run -d -p port_hosta:port_kontenera nazwa_obrazu
             docker run -d -p 8080:8080 zad1
  ![image](https://github.com/erkjx/zadanie1_PAwChO2023/assets/129630909/a0a96ad1-fcbb-48b1-9e6d-4e938c2c7429)

  c) 
  Polecenie: docker logs <ID_kontenera>
             docker logs 5555fb3f61f3

  d)
  Polecenie: docker inspect --format='{{len .RootFS.Layers}}' nazwa_obrazu
             docker inspect --format='{{len .RootFS.Layers}}' zad1
  ![image](https://github.com/erkjx/zadanie1_PAwChO2023/assets/129630909/dae7b907-085e-42bf-a36b-14cbcc812e3b)

  ![image](https://github.com/erkjx/zadanie1_PAwChO2023/assets/129630909/14586b4f-599d-4dfd-bc5d-cc82d41b79b8)



