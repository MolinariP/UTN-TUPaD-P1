# 1. Crear una función llamada imprimir_hola_mundo que imprima por
#  pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
#  programa principal.

# Definicion de funciones
def imprimir_hola_mundo():
    print("Hola Mundo!")

# Programa principal
imprimir_hola_mundo()


#  2. Crear una función llamada saludar_usuario(nombre) que reciba
#  como parámetro un nombre y devuelva un saludo personalizado.
#  Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de
# volver: “Hola Marcos!”. Llamar a esta función desde el programa
#  principal solicitando el nombre al usuario.

# Definicion de funciones
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

# Programa principal
saludar_usuario("Marcos")


#  3. Crear una función llamada informacion_personal(nombre, apellido,
#  edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#  [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe
# dir los datos al usuario y llamar a esta función con los valores in
# gresados.

# Definicion de funciones
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Programa principal
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su residencia: ")
informacion_personal(nombre, apellido, edad, residencia)


#  4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra
# dio como parámetro y devuelva el área del círculo. calcular_peri
# metro_circulo(radio) que reciba el radio como parámetro y devuel
# va el perímetro del círculo. Solicitar el radio al usuario y llamar am
# bas funciones para mostrar los resultados.

import math
# Definicion de funciones
def calcular_area_circulo(radio):
    area =  math.pi * radio ** 2
    print("El área del círculo es:", area)

def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    print("El perímetro del círculo es:", perimetro)


# Programa principal
radio = float(input("Ingrese el radio de un círculo: "))
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)


#  5. Crear una función llamada segundos_a_horas(segundos) que reciba
#  una cantidad de segundos como parámetro y devuelva la cantidad
#  de horas correspondientes. Solicitar al usuario los segundos y mos
# trar el resultado usando esta función.

# Definicion de funciones
def segundos_a_horas(segundos):
    horas = segundos / 3600
    print(f"La cantidad de segundos ingresados equivalen a {horas} horas.")

# Programa principal
segundos = int(input("Ingrese los segundos: "))
segundos_a_horas(segundos)


#  6. Crear una función llamada tabla_multiplicar(numero) que reciba un
#  número como parámetro y imprima la tabla de multiplicar de ese
#  número del 1 al 10. Pedir al usuario el número y llamar a la fun
# ción.

# Definicion de funciones
def tabla_multiplicar(numero):
    print(f"La tabla de multiplicar del número {numero} es:")
    for i in range(1, 11):
        print(f"{numero} por {i} = {numero * i}")

# Programa principal
numero = int(input("Ingrese un número entero: "))
tabla_multiplicar(numero)


#  7. Crear una función llamada operaciones_basicas(a, b) que reciba
#  dos números como parámetros y devuelva una tupla con el resulta
# do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re
# sultados de forma clara.

# Definicion de funciones
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicarcion = a * b
    division = a / b if b != 0 else "No se puede dividir por cero"

    print(f"El resultado de {a} + {b} es = {suma}")
    print(f"El resultado de {a} - {b} es = {resta}")
    print(f"El resultado de {a} * {b} es = {multiplicarcion}")
    print(f"El resultado de {a} / {b} es = {division}")

    return (suma, resta, multiplicarcion, division)

# Programa principal
a = float(input("Ingrese un número: "))
b = float(input("Ingrese otro número: "))
operaciones_basicas(a, b)


#  8. Crear una función llamada calcular_imc(peso, altura) que reciba el
#  peso en kilogramos y la altura en metros, y devuelva el índice de
#  masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun
# ción para mostrar el resultado con dos decimales.

# Definicion de funciones
def calcular_imc(peso, altura):
    imc = peso / (altura) ** 2
    print(f"Su IMC es: {imc:.2f}")

# Programa principal
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kilogramos: "))
calcular_imc(peso, altura)


#  9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#  una temperatura en grados Celsius y devuelva su equivalente en
#  Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#  resultado usando la función.

# Definicion de funciones
def celsius_a_fahrenheit(celsius):
    fahrenheit = (9 / 5) * celsius + 32
    print(f"El equivalente a {celsius} grados Celsius es de {fahrenheit} grados Fahrenheit")

# Programa principal
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
celsius_a_fahrenheit(celsius)


#  10.Crear una función llamada calcular_promedio(a, b, c) que reciba
#  tres números como parámetros y devuelva el promedio de ellos.
#  Solicitar los números al usuario y mostrar el resultado usando esta
#  función.

# Definicion de funciones
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    print(f"El promedio de los tres números es {promedio}")

# Programa principal
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))
calcular_promedio(a, b, c)
