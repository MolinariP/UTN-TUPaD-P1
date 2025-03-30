# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print("Hola Mundo!")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.

nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.

radio = input("Ingrese el radio de un círculo: ")
radio = float(radio)
pi = 3.14159
area = pi * radio * radio
perimetro = 2 * pi * radio
print(f"El area del circulo es {area} y el perimetro es {perimetro}")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.

segundos = input("Ingrese la cantidad de segundos a convertir: ")
segundos = int(segundos)
horas = segundos / 3600 
print(f"{segundos} segundos equivalen a {horas} horas.")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.

numero = input("Ingrese un numero: ")
numero = int(numero)
print(f"La tabla de multiplicar del número {numero} es:")
print(f"{numero} por 1 = {numero * 1}")
print(f"{numero} por 2 = {numero * 2}")
print(f"{numero} por 3 = {numero * 3}")
print(f"{numero} por 4 = {numero * 4}")
print(f"{numero} por 5 = {numero * 5}")
print(f"{numero} por 6 = {numero * 6}")
print(f"{numero} por 7 = {numero * 7}")
print(f"{numero} por 8 = {numero * 8}")
print(f"{numero} por 9 = {numero * 9}")
print(f"{numero} por 10 = {numero * 10}")

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

num1 = input("Ingrese un número entero distinto de 0: ")
num1 = int(num1)
num2 = input("Ingrese otro número entero distinto de 0: ")
num2 = int(num2)
print(f"El resultado de {num1} + {num2} es = {num1 + num2}")
print(f"El resultado de {num1} / {num2} es = {num1 / num2}")
print(f"El resultado de {num1} * {num2} es = {num1 * num2}")
print(f"El resultado de {num1} - {num2} es = {num1 - num2}")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
# modo:
# 𝐼𝑀𝐶 =  𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔 / (𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)2

altura = input("Ingrese su altura en metros: ")
altura = float(altura)
peso = input("Ingrese su peso en kilogramos: ")
peso = float(peso)
imc = peso / (altura) ** 2
print(f"Su IMC es: {imc}")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
# 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9/5 . 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32

celsius = input("Ingrese la temperatura en grados Celsius: ")
celsius = float(celsius)
fahrenheit = (9 / 5) * celsius + 32
print(f"El equivalente a {celsius} grados Celsius es de {fahrenheit} grados Fahrenheit")

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.

num1 = input("Ingrese el primer número: ")
num1 = float(num1)
num2 = input("Ingrese el segundo número: ")
num2 = float(num2)
num3 = input("Ingrese el tercer número: ")
num3 = float(num3)
promedio = (num1 + num2 + num3) / 3
print(f"El promedio de los tres números es {promedio}")
