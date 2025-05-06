import time

def escribe_hora():
    print("Escribiendo la hora..")
    hora = time.strftime("%H:%M:%S")
    print(f"La hora es: {hora}")

if __name__ == "__main__":
    escribe_hora()
    print("Fin del programa.")