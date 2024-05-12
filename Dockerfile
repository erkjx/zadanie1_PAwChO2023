# Ustawienie obrazu bazowego, który zawiera pytz
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
