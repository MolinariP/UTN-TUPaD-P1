# TRABAJO PRACTICO 3: ESTRUCTURAS CONDICIONALES
# MOLINARI, PABLO


# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”. 

# Se solicita al usuario ingresar la edad
edad = int(input("Ingrese su edad: "))
# Si se cumple la condicion anterior se muestra el mensaje "Es mayor de edad".
if edad > 18:
    print("Es mayor de edad")

# Se podria agregar un condicional para evitar que se ingresen números negativo.


# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá 
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el 
# mensaje “Desaprobado”.

# Se solicita al usuario que ingrese su nota
nota = int(input("Ingrese su nota: "))
# Si se cumple la condicion se muestra el mensaje "Aprobado".
if nota >= 6:
    print("Aprobado")
# Si no se cumple se muestra el mensaje "Desaprobado".
else:
    print("Desaprobado")

# Se podria agregar un condicional para evitar que se ingresen notas negativas o mayores a 10.


# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un 
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso 
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del 
# operador de módulo (%) en Python para evaluar si un número es par o impar. 

# Se solicita al usuario que ingrese un número
num = int(input("Ingrese un número: "))
# Si se cumple la condicion se muestra el mensaje "Ha ingresado un número par"
if num % 2 == 0:
    print("Ha ingresado un número par")
# Si no se cumple se muestra el mensaje "Por favor, ingrese un número par".
else:
    print("Por favor, ingrese un número par")   


# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las 
# siguientes categorías pertenece: 
# ● Niño/a: menor de 12 años. 
# ● Adolescente: mayor o igual que 12 años y menor que 18 años. 
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
# ● Adulto/a: mayor o igual que 30 años. 

# Se solicita ingresar su edad
edad = int(input("Ingrese su edad: "))
# Si la variable edad es menor al numero 12, se muestra "Usted pertence a la categoría Niño/a"
if edad < 12:
    print("Usted pertence a la categoría Niño/a")
# Si edad es mayor o igual que 12 y menor que 18, se muestra "Usted pertence a la categoría Adolecente"
elif edad >= 12 and edad < 18:
    print("Usted pertence a la categoría Adolecente")
# Si edad es mayor o igual que 18 y menor que 30, se muestra "Usted pertence a la categoría Adulto/a joven"
elif edad >= 18 and edad < 30:
    print("Usted pertence a la categoría Adulto/a joven")
# Si no se cumplen las condiciones anteriores se muestra el mensaje "Usted pertence a la categoría Adulto/a"
else:
    print("Usted pertence a la categoría Adulto/a")

# Se podria agregar un condicional para evitar que se ingresen números negativo.


# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso 
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal 
# como una lista o un string.

# Se solicita al usuario ingresar una contraseña
contrasena = input("Ingrese una contraseña que contenga entre 8 y 14 caracteres: ")
largo_contrasena = len(contrasena)         
# Si se cumple la condicion se muestra el mensaje "Ha ingresado una contraseña correcta"
if largo_contrasena >= 8 and largo_contrasena <= 14:
    print("Ha ingresado una contraseña correcta")  
# Si no se cumple se muestra el mensaje "Por favor, ingrese una contraseña de entre 8 y 14 caracteres"
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


# 6) El paquete statistics de python contiene funciones que permiten tomar una lista de números 
# y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el 
# siguiente: 
#           from statistics import mode, median, mean 
#           mi_lista = [1,2,5,5,3] 
#           mean(mi_lista) 
# En la documentación oficial se puede encontrar más información sobre este paquete: 
# https://docs.python.org/es/3.8/library/statistics.html.  
# La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se 
# pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio: 
# ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la 
# mediana es mayor que la moda. 
# ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, 
# la mediana es menor que la moda. 
# ● Sin sesgo: cuando la media, la mediana y la moda son iguales. 
# Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista 
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si 
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla. 
# Definir la lista numeros_aleatorios de la siguiente forma: 
#           import random 
#           numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 
# Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de 
# forma aleatoria. 

# Del paquete statistics se importan solo las funciones mode, median, mean
from statistics import mode, median, mean          
import random

# crea una lista con 50 números entre 1 y 100 elegidos de forma aleatoria.
numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 

# Se utilizan las funciones y se guardan en las variables
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

# Si se cumple la condicion se muestra el mensaje "No hay sesgo"
if media == mediana and media == moda:
    print("No hay sesgo")
# Si se cumple la siguiente condicion se muestra el mensaje "Hay sesgo positivo"              
elif media > mediana and mediana > moda:
    print("Hay sesgo positivo")
# Si se cumple la siguiente condicion se muestra el mensaje "Hay sesgo negativo"
elif media < mediana and mediana < moda:
    print("Hay sesgo negativo")

# Se podría agregar un else que ejecute un print para el caso que no se cumplan las condiciones anteriores.


# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por 
# pantalla. 

# Se solicita al usuario que ingrese una frase o una palabra
frase = input("Ingrese una frase o palabra: ")
letraFinal = frase[-1].lower()
# Si se cumple la condicion se muestra la frase agregando el signo de exclamación al final 
if letraFinal == 'a' or letraFinal == 'e' or letraFinal == 'i' or letraFinal == 'o' or letraFinal == 'u':
    print(frase + "!")
# Si no se cumple se muestra la frase original ingresada por el usuario
else:
    print(frase)

# Se podria mejor el codigo inculendo las vocales con tildes o caracteres especiales.


# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
# dependiendo de la opción que desee: 
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.

# Se solicita al usuario ingresar su nombre
nombre = input("Ingrese su nombre: ")

# Se solicita al usuario ingresar una de las opciones
opcion = int(input("""Si quiere su nombre en mayúsculas, ingrese 1.
Si quiere su nombre en minúsculas, ingres 2.
Si quiere su nombre con la primera letra mayúscula, ingrese 3."""))

# Si se cumple la condicion se muestra el texto en mayusculas
if opcion == 1:
    print(nombre.upper())
# Si se cumple la condicion 2, se muestra el texto en minúsculas
elif opcion == 2:
    print(nombre.lower())
# Si se cumple la condicion 3, se muestra la inicial en mayúscula
elif opcion == 3:
    print(nombre.title())

# Se podría agregar un condicional para evitar que se ingresen números negativos o mayores a 3.


# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado 
# por pantalla: 
# ● Menor que 3: "Muy leve" (imperceptible). 
# ● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
# ● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero 
# generalmente no causa daños). 
# ● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras 
# débiles). 
# ● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

# Se solicita al usuario ingresar la magnitud del terremoto
magnitud = float(input("Ingrese la magnitud del terremoto: "))
# Si se muestra el mensaje segun la condición que se cumpla
if magnitud < 3:
    print("La magnitud del terremoto es Muy Leve, imperceptible")
elif magnitud >= 3 and magnitud < 4:
    print("La magnitud del terremoto es Leve, ligeramente perceptible")
elif magnitud >= 4 and magnitud < 5:
    print("La magnitud del terremoto es Moderado, sentido por personas, pero generalmente no causa daños")
elif magnitud >= 5 and magnitud < 6:
    print("La magnitud del terremoto es Fuerte, puede causar daños en estructuras débiles")
elif magnitud >= 6 and magnitud < 7:
    print("La magnitud del terremoto es Muy Fuerte, puede causar daños significativos")
else:
    print("La magnitud del terremoto es Extremo, puede causar graves daños a gran escala")

# Se podria agregar un condicional para evitar los valores negativos.


# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año 

# Periodo del año               Estación en el       Estación en el 
#                                hemisferio norte    hemisferio sur
# Desde el 21 de diciembre            
#  hasta el 20 de                    Invierno           Verano
# marzo (incluidos) 

# Desde el 21 de marzo              
# hasta el 20 de junio               Primavera          Otoño
# (incluidos) 

# Desde el 21 de junio
#  hasta el 20 de                      Verano           Invierno
# septiembre (incluidos) 

# Desde el 21 de septiembre 
# hasta el 20 de                       Otoño             Primavera
# diciembre (incluidos) 

# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
# del año es y qué día es.  El programa deberá utilizar esa información para imprimir por pantalla 
# si el usuario se encuentra en otoño, invierno, primavera o verano.

# La variable hemisferio guarda el input solicitado y .upper() convierte el input en mayúsculas.
hemisferio = input("Ingrese el hemisferio en el que se encuentra, indique N para Norte, S para Sur): ").upper()
# La variable mes guarda el input solicitado e int lo convierte en un entero
mes = int(input("Ingrese el mes del año, en el formato 1-12: "))
# La variable dia guarda el input solicitado e int lo convierte en un entero
dia = int(input("Ingrese el día, en el formato 1-31: "))


# El condicional verifica si la variable hemisferio es igual a "N", sino pasa al elif donde se verifica si es igual a "S", sino finaliza la ejecucion
if hemisferio == "N":
# Si se cumple la condicion anterior, se verifica si las varibles mes y dia se encuentran dentro de los rangos de cada estación. Si se cumple se muestra por pantalla
    if (mes == 12 and (dia >= 21 and dia <= 31)) or ( mes == 1 and (dia >= 1 and dia <= 31)) or (mes == 2 and (dia >=1 and dia <= 29)) or (mes == 3 and (dia >= 1 and dia <= 20)):
        print("La estación del año en la que se encuentra es invierno")
    elif (mes == 3 and (dia >= 21 and dia <= 31)) or ( mes == 4 and (dia >= 1 and dia <= 30)) or (mes == 5 and (dia >=1 and dia <= 31)) or (mes == 6 and (dia >= 1 and dia <= 20)):
        print("La estación del año en la que se encuentra es primavera")
    elif (mes == 6 and (dia >= 21 and dia <= 30)) or ( mes == 7 and (dia >= 1 and dia <= 31)) or (mes == 8 and (dia >=1 and dia <= 31)) or (mes == 9 and (dia >= 1 and dia <= 20)):
        print("La estación del año en la que se encuentra es verano")
    elif (mes == 9 and (dia >= 21 and dia <= 30)) or ( mes == 10 and (dia >= 1 and dia <= 31)) or (mes == 11 and (dia >=1 and dia <= 30)) or (mes == 12 and (dia >= 1 and dia <= 20)):
        print("La estación del año en la que se encuentra es otoño")
elif hemisferio == "S":
    if (mes == 12 and (dia >= 21 and dia <= 31)) or ( mes == 1 and (dia >= 1 and dia <= 31)) or (mes == 2 and (dia >=1 and dia <= 29)) or (mes == 3 and (dia >= 1 and dia <= 20)):
        print("La estación del año en la que se encuentra es verano")
    elif (mes == 3 and (dia >= 21 and dia <= 31)) or ( mes == 4 and (dia >= 1 and dia <= 30)) or (mes == 5 and (dia >=1 and dia <= 31)) or (mes == 6 and (dia >= 1 and dia <= 20)):
        print("La estación del año en la que se encuentra es otoño")
    elif (mes == 6 and (dia >= 21 and dia <= 30)) or ( mes == 7 and (dia >= 1 and dia <= 31)) or (mes == 8 and (dia >=1 and dia <= 31)) or (mes == 9 and (dia >= 1 and dia <= 20)):
        print("La estación del año en la que se encuentra es invierno")
    elif (mes == 9 and (dia >= 21 and dia <= 30)) or ( mes == 10 and (dia >= 1 and dia <= 31)) or (mes == 11 and (dia >=1 and dia <= 30)) or (mes == 12 and (dia >= 1 and dia <= 20)):
        print("La estación del año en la que se encuentra es primavera")

