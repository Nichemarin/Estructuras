class Perro:
    def sonido(self):
        print('Guauuu!')

class Gato:
    def sonido(self):
        print('Miauuu!')

class Vaca:
    def sonido(self):
        print('Muuuuu!')

def oir_sonido(animales):
    for animal in animales:
        animal.sonido()

granja = [Perro(), Gato(), Vaca()]

oir_sonido(granja)