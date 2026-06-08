import random

# =========================
# CLASE BASE (HERENCIA)
# =========================
class Personaje:
    def __init__(self, nombre):
        self._nombre = nombre

    def mostrar_tipo(self):
        print("Soy un personaje del juego.")


# =========================
# CLASE JUGADOR
# =========================
class Jugador(Personaje):

    def mostrar_tipo(self):
        print(f"{self._nombre} es un jugador.")  # Polimorfismo


# =========================
# CLASE COMPUTADORA
# =========================
class Computadora(Personaje):

    def mostrar_tipo(self):
        print("Soy la computadora.")  # Polimorfismo


# =========================
# CLASE PRINCIPAL DEL JUEGO
# =========================
class JuegoAhorcado:

    def __init__(self):
        self.__palabras = [
            "python",
            "computadora",
            "programacion",
            "videojuego",
            "algoritmo"
        ]

        self.__puntaje = 0

    # Getter
    def get_puntaje(self):
        return self.__puntaje

    # Setter
    def set_puntaje(self, valor):
        self.__puntaje = valor

    def jugar(self):

        palabra = random.choice(self.__palabras)

        letras_adivinadas = []
        intentos = 6

        print("\n=== ADIVINA LA PALABRA ===")

        while intentos > 0:

            palabra_oculta = ""

            for letra in palabra:
                if letra in letras_adivinadas:
                    palabra_oculta += letra + " "
                else:
                    palabra_oculta += "_ "

            print("\nPalabra:", palabra_oculta)

            if "_" not in palabra_oculta:
                print("\n¡Ganaste!")
                self.__puntaje += 10
                return True

            try:
                letra = input("Ingresa una letra: ").lower()

                if len(letra) != 1:
                    raise ValueError

            except ValueError:
                print("Debes ingresar una sola letra.")
                continue

            if letra in letras_adivinadas:
                print("Ya intentaste con esa letra.")
                continue

            letras_adivinadas.append(letra)

            if letra not in palabra:
                intentos -= 1
                print("Incorrecto.")
                print("Intentos restantes:", intentos)

        print("\nPerdiste.")
        print("La palabra era:", palabra)
        return False

    def guardar_puntaje(self, nombre):

        with open("puntajes.txt", "a", encoding="utf-8") as archivo:
            archivo.write(f"{nombre}: {self.__puntaje} puntos\n")

    def mostrar_historial(self):

        try:
            with open("puntajes.txt", "r", encoding="utf-8") as archivo:
                print("\n=== HISTORIAL DE PUNTAJES ===")
                print(archivo.read())

        except FileNotFoundError:
            print("Aún no existen puntajes registrados.")


# =========================
# PROGRAMA PRINCIPAL
# =========================

print("=== SUITE DE MINIJUEGO ===")

nombre = input("Ingresa tu nombre: ")

jugador = Jugador(nombre)
pc = Computadora("CPU")

# Polimorfismo
jugador.mostrar_tipo()
pc.mostrar_tipo()

juego = JuegoAhorcado()

juego.jugar()

print("\nPuntaje obtenido:", juego.get_puntaje())

juego.guardar_puntaje(nombre)

juego.mostrar_historial()