# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea. 

for num in range(101):
    print(num)


# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
# dígitos que contiene. 

num = int(input("Ingrese un número entero: "))

num = abs(num)

if num == 0:
    digitos = 1
else:
    digitos = 0
    while num > 0:
        num //= 10
        digitos += 1

if digitos == 1:
    print("El número ingresado tiene", digitos, "dígito.")
else:
    print("El número ingresado tiene", digitos, "dígitos.")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
# dados por el usuario, excluyendo esos dos valores. 

num1 = int(input("Ingrese un número entero: "))
num2 = int(input("Ingrese otro número entero: "))
suma_enteros = 0

if num1 > num2:
    aux = num1
    num1 = num2
    num2 = aux

for i in range(num1+1, num2):
    suma_enteros += i

print("La suma de todos los números enteros comprendidos entre ", num1, " y ", num2, " (excluyendo los valores ingresados) es: ", suma_enteros)


# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
# un 0. 

num = int(input("Ingrese un número entero. Cuando quiera finalizar ingrese 0 (Cero) "))
suma_enteros = 0
 
while num != 0:
    suma_enteros += num
    num = int(input("Ingrese otro número entero. Cuando quiera finalizar ingrese 0 (Cero) "))

print("La suma de los número enteros ingresados es: ", suma_enteros)

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 

import random

numero_aleatorio = random.randint(0, 9) 

num = int(input("En el siguiente juego debe acertar un número del 0 al 9. Ingrese un número: "))
intento = 1

while num != numero_aleatorio:
    intento += 1
    num = int(input("No acertó. Ingrese otro número: "))

print("Acertó en el intento ", intento)

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
# entre 0 y 100, en orden decreciente. 

for num in range(100, -1, -1):
    print(num)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
# número entero positivo indicado por el usuario. 

num = int(input("Ingrese un número entero positivo: "))
suma_num = 0

if num >= 0:
    for i in range(0, num+1):
        suma_num += i
    
    print("La suma de los números entre 0 y", num, "es:", suma_num)
else:
    print("Debió ingresar un número entero positivo.")

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
# menor, pero debe estar preparado para procesar 100 números con un solo cambio). 

num_pares = 0
num_impares = 0
num_positivos = 0
num_negativos = 0

for i in range(100):
    num = int(input("Ingrese un número entero: "))
    if num >= 0:
        num_positivos += 1
    else:
        num_negativos += 1
    
    if num % 2 == 0:
        num_pares += 1
    else:
        num_impares += 1

print("De los números ingresados hay", num_pares, "números pares,", num_impares, "números impares,", num_negativos, "números negativos y", num_positivos, "números positivos.")


# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
# poder procesar 100 números cambiando solo un valor). 

suma_enteros = 0

for i in range(100):
    num = int(input("Ingrese un número entero: "))
    suma_enteros += num

media = suma_enteros / 100

print("La media de los números ingresados es:", media)

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num = int(input("Ingrese un número: "))
num_negativo = num < 0
num = abs(num)

num_invertido = 0
while num > 0:
    digito = num % 10
    num_invertido = num_invertido * 10 + digito
    num //= 10

if num_negativo:
    num_invertido *= -1

print("El número invertido es:", num_invertido)

