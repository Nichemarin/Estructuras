import random

"""
print ("Hola mundo")

lista = [1,2,3]
lista2 = [4,5,6]
lista3 = lista

print(1 in lista)
print(4 in lista)
print(lista is lista3)
print(lista is not lista3)

print("hola mundo")

yandel = input("¿Cuál es tu nombre? ")
print(f"¡Hola, {yandel}!")
wisin = int(input("¿Cuántos años tienes? "))
print(f"Tienes {wisin} años.")

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))

if num1 and num2 > 0:
    print("Ambos números son positivos.")
elif num1 and num2 < 0:
    print("Ambos números son negativos.")

nota = float(input("escribe tu nota: "))
match nota:
    case nota if nota < 5 and nota >= 0:
        print("Suspenso")
    case nota if nota >= 5 and nota < 7:
        print("Aprobado")
    case nota if nota >= 7 and nota < 8.5:
        print("Notable")
    case nota if nota >= 8.5 and nota <= 10:
        print("Sobresaliente")
    case _ if nota < 0 or nota > 10:
        print("Nota no valida")

temperatura = float(input("Ingrese la temperatura actual: "))
if 18 <= temperatura <= 27:
    print("Temperatura optima")
elif temperatura < 18:
    print("ALERTA FRÍO")
else:
    print("ALERTA CALOR")


userName = input("Ingrese su nombre de usuario: ")
postalCode = input("Ingrese su código postal: ")

userName = userName.strip().lower()
postalCode = postalCode.strip()

if not userName:
    print("El nombre esta vacío")
elif not postalCode:
    print("El código postal esta vacío")
elif not postalCode.isdigit():
    print("El codigo postal solo puede contener numeros")
else:
    print(f"Registro valido. \nUsuario: {userName}\nCódigo postal: {postalCode}")


product1 = input("Ingrese el nombre del producto: ")
product2 = input("Ingrese el nombre del segundo producto: ")

if product1 == product2:
    print("Son el mismo producto")
elif product1 < product2:
    print(product1)
    print(product2)
else:
    print(product2)
    print(product1)

product1 = product1.strip().lower()
product2 = product2.strip().lower()

if product1 == product2:
    print("Son el mismo producto")
elif product1 < product2:
    print(product1)
    print(product2)
else:
    print(product2)
    print(product1)


estado = int(input("Ingrese el estado: "))

match estado:
    case 200 | 201:
        print("Respuesta exitosa")
    case 400 | 401 | 403 | 404:
        print("Error de cliente")
    case 500 | 503:
        print("Error de servidor")
    case _:
        print("Código de estado desconocido")


mi_lista = ["manzana", "pera", "uva", "banana"]
for fruta in mi_lista:
    print(fruta)

for letter in "Hipopotomonstrosesquipedialofobia":
    print(letter)

prices = [100, 250, 75, 500, 150]
discounted_prices = []
discount_rate = 0.20

for price in prices:
    discounted = price * (1-discount_rate)
    discounted_prices.append(discounted)
    print(f"Precio origina: {price} -> Con descuento: {discounted}")

for number in range(0,11,2):
    print(f"Numero: {number}")

for number in range (10,0,-1):
    print(number)
print("Despegue")

numero = 6
print(f"Tabla del {numero}")
for number in range(1,11):
    print(f"{numero} x {number} = {numero*number}")
tasks = [
    "No hacer nada",
    "Seguir sin hacer nada",
    "Pensar en hacer algo pero no hacer nada",
]
for index, task in enumerate(tasks, start=1):
    print(f"{index}. {task}")

    
lista = [15.50, 20.0, 35.75, 10.0]
suma = 0
for precio in lista:
    suma += precio
print(suma)

palabra = input("Escribe algo: ")
contador = 0
for letra in palabra.lower():
    if letra in "aeiou":
        contador += 1
print(contador)

numero = 8
print(f"Tabla del {numero}")
for number in range(1,11):
    print(f"{numero} x {number} = {numero*number}")

for number in range(20,-1,-2):
    print(number)

lista = ["Comprar leche", "Llamar al medico", "Estudiar Python"]
for index, tarea in enumerate(lista, start=1):
    print(f"{index}. {tarea}")

for i in range(1,4):
    print(f"Tabla del {i}")
    for j in range(1,6):
        result = i*j
        print(f"\t{i} * {j} = {result}")

cuadrados = [numero**2 for numero in range(1,6)]
print(cuadrados)

for i in range(1,6):
    for j in range(i,6):
        print("* ", end="")
    print(" ")


for i in range(1,6):
    for j in range(i):
        aleatorio = (random.randint(0, 9))
        if(aleatorio % 2 == 0):
            print("P", end=" ")
        else:
            print(aleatorio, end=" ")
    print(" ")


numbers = [1, 2, 3, 7, 14]

index = 0
found = None
while index < len(numbers) and found is None:
    if numbers[index] % 7 == 0:
        found = numbers[index]
    index+=1
print(f"Encontrado con while: {found}")

talla = ["M", "L"]
colores = ["Rojo", "Azul", "Negro"]

for i in range (len(talla)):
    for j in range(len(colores)):
        print(f"{talla[i]} {colores[j]}")

        
numeros = [1, 2, 3, 4, 5]
cuadrados = [numero**2 for numero in range(1, len(numeros) + 1)]
print(cuadrados)


palabras = ["sol", "murcielago", "mar", "elefante", "luz"]
largas = [p for p in palabras if len(p) > 3]
print(largas)

password = "python123"
while True:
    userPassword = input("Escribe la contraseña: ")
    if password != userPassword:
        print("Contraseña incorrecta vuelva a intentarlo...")
    else:
        print("Contraseña correcta")
        break

suma = 0
contador = 0;
while suma <= 50:
    numero = int(input("Escriba un numero: "))
    suma += numero
    contador += 1
print(f"Se ingresaron {contador} numeros")

intentos_maximos = 3
intentos_hechos = 0
contraseña = 1234
while intentos_hechos < 3:
    usuario_contraseña = int(input("Digite su pin: "))
    if usuario_contraseña != contraseña:
        intentos_hechos += 1
        print("Pin incorrecto, vuelvalo a intentar")
    else:
        print("Ingresando al cajero...")
        break

inventario = {"Manzanas" : 50, "peras":30, "naranjas":100}
frutas = []
for fruta,cantidad in inventario.items():
    print(f"{fruta} {cantidad}")
    frutas.append(fruta)
print(frutas)

def sumar(p1, p2):
    return (p1+p2)

print(sumar(3,4))

def factorial(n):
    if n <= 1:
        return 1
    return n*factorial(n-1)

numeros = [1,2,3,4,5]
cuadrado = list (map(lambda x: x**2, numeros))

print(cuadrado)
print(factorial(500))

def crear_perfil_usuario(**kwargs):
    for clave,valor in kwargs.items():
        print(f"{clave.capitalize()}: {valor}")

crear_perfil_usuario(nombre ="luis", edad = 19, Ciudad = "Madrid", pais = "España")
"""

def crear_perfil_usuario(nombre, apellido,**kwargs):
    perfil = {"nombre": nombre, "apellido": apellido}
    perfil.update(kwargs)
    return perfil

print(crear_perfil_usuario("Luis", "Taba", edad = 19, ciudad = "Torremolinos", País = "Panchitolandia"))