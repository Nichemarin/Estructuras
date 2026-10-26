class Coche:
    def __init__(self, color, aceleracion):
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 0

    def acelera(self):
        self.velocidad += self.aceleracion

class CocheVolador(Coche):
    ruedas = 6
    def __init__(self, color, aceleracion, esta_volando = False):
        super().__init__(color, aceleracion)
        self.esta_volando = esta_volando

    def vuela(self):
        self.esta_volando = True


cv1 = CocheVolador("Rojo", 60)

cv1.acelera()
print(f"Velocidad coche volador: {cv1.velocidad}")
print(f"Vuela?: {cv1.esta_volando}")
print("¿CocheVolador es subclase de Coche ?: ", issubclass(CocheVolador, Coche))
print("¿Coche es subclase de CocheVolador ?: ", issubclass(Coche, CocheVolador))