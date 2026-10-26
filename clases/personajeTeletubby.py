class personajeTeletubby:
    saludo_oficial = "¡Tubby abrazo!"

    def __init__(
        self, nombre, color, antena, objeto_favorito, nivel_hambre, nivel_felicidad
    ):
        self.nombre = nombre
        self.color = color
        self.antena = antena
        self.objeto_favorito = objeto_favorito
        self.__nivel_hambre = nivel_hambre
        self.__nivel_felicidad = nivel_felicidad

    def __str__(self):
        return f"Nombre: {self.nombre}\nColor: {self.color}\nAntena: {self.antena}\nObjeto favorito: {self.objeto_favorito}\nNivel de hambre: {self.__nivel_hambre}\nNivel de felicidad: {self.__nivel_felicidad}"

    def saludar(self):
        return f"Hola! Soy {self.nombre}, mi color es {self.color} y mi antena es {self.antena}"

    def jugar(self):
        self.__nivel_hambre += 20
        self.__nivel_felicidad += 10
        return f"{self.nombre} esta jugando con su objeto favorito"

    def comer_tuby_papilla(self):
        self.__nivel_hambre = 0
        self.__nivel_felicidad += 20
        return f"{self.nombre} ha comido una deliciosa tuby papilla"

    def ver_estado(self):
        return f"Nombre: {self.nombre} \nColor: {self.color} \nAntena: {self.antena} \nObjeto favorito: {self.objeto_favorito} \nNivel de hambre: {self.__nivel_hambre} \nNivel de felicidad: {self.__nivel_felicidad}"


if __name__ == "__main__":
    tinky_winky = personajeTeletubby(
        "Tinky Winky", "morado", "triángulo", "bolso", 5, 8
    )
    dipsy = personajeTeletubby("Dipsy", "verde", "antena recta", "sombrero", 4, 9)
    laa_laa = personajeTeletubby(
        "Laa-Laa", "amarillo", "antena rizada", "pelota", 3, 10
    )
    po = personajeTeletubby("Po", "rojo", "círculo", "patinete", 6, 9)
    # 1. Saludar y mostrar el saludo oficial
    print(personajeTeletubby.saludo_oficial)
    print(tinky_winky.saludar())
    print(po.saludar())

    # 2. Jugar
    print(tinky_winky.jugar())
    print(po.jugar())

    # 3. Mostrar el estado inicial después de jugar
    print("\n--- Estado de Tinky Winky ---")
    print(tinky_winky.ver_estado())

    print("\n--- Estado de Po ---")
    print(po.ver_estado())

    # 4. Solo Tinky Winky come
    print("\n" + tinky_winky.comer_tuby_papilla())

    # 5. Mostrar el estado final de ambos
    print("\n--- Estado final de Tinky Winky ---")
    print(tinky_winky.ver_estado())

    print("\n--- Estado final de Po ---")
    print(po.ver_estado())
