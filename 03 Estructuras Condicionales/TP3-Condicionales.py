
# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”. 

edad = int(input("Ingrese su edad: ")) # Con el input se pide la edad al usuario, se convierte en numero entero con int, y se guarda en la variable edad
if edad > 18:                           # El condicional verifica si la variable edad es mayor al numero 18
    print("Es mayor de edad")           # Si se cumple la condicion anterior se ejecuta el print, mostrando el mensaje.


# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá 
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el 
# mensaje “Desaprobado”.

nota = int(input("Ingrese su nota: "))  # En la variable nota se guarda el input solicitado al usuario, convertido en entero por el int 
if nota >= 6:                           # El condicional verifica si la variable edad es mayor o igual al numero 6
    print("Aprobado")                   # Si se cumple la condicion anterior se ejecuta el print, mostrando el mensaje "Aprobado".
else:
    print("Desaprobado")                # Si no se cumple se ejecuta el print, mostrando el mensaje "Desaprobado".


# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un 
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso 
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del 
# operador de módulo (%) en Python para evaluar si un número es par o impar. 

num = int(input("Ingrese un número par: "))     # En la variable num se guarda el input solicitado al usuario, convertido en entero por el int 
if num % 2 == 0:                                # El operador módulo (%) se usa para obtener el resto de la división entre la variable num y 2.
                                                # El condicional verifica si la variable es igual a cero, ya que el resto de los pares siempre es cero
    print("Ha ingresado un número par")         # Si se cumple la condicion se ejecuta el print, mostrando el mensaje "Ha ingresado un número par"
else:
    print("Por favor, ingrese un número par")   # Si no se cumple se ejecuta el print, mostrando el mensaje "Por favor, ingrese un número par".


# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las 
# siguientes categorías pertenece: 
# ● Niño/a: menor de 12 años. 
# ● Adolescente: mayor o igual que 12 años y menor que 18 años. 
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
# ● Adulto/a: mayor o igual que 30 años. 

edad = int(input("Ingrese su edad: "))                  # En la variable edad se guarda el input solicitado al usuario, convertido en entero por el int
if edad < 12:                                            # El condicional verifica si la variable edad es menor al numero 12
    print("Usted pertence a la categoría Niño/a")
elif edad >= 12 and edad < 18:                           # El condicional elfi, si no se cumplio el condicional anterior, verifica si la variable edad 
                                                        # es mayor o igual al numero 12 y edad es menor al numero 18.
    print("Usted pertence a la categoría Adolecente")   # Si se cumple la condicion se ejecuta el print
elif edad >= 18 and edad < 30:                          # Si no se cumple se verifica que la variable edad es mayor o igual a 18 y menor que 30
    print("Usted pertence a la categoría Adulto/a joven")   # Si se cumple la condicion se ejecuta el print
else:
    print("Usted pertence a la categoría Adulto/a")     # Si no se cumple se ejecuta el print


# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso 
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal 
# como una lista o un string.

contrasena = input("Ingrese una contraseña que contenga entre 8 y 14 caracteres: ")     # La variable contrasena guarda el input solicitado al usuario
largo_contrasena = len(contrasena)                                # La funcion len() devuelve la cantidad de caracteres de la variable contrasenta y se guarda en la variable largo_contrasena
if largo_contrasena >= 8 and largo_contrasena <= 14:              # El condicional verifica si la variable largo_contrasena es mayor o igual que 8 y menor o igual que 14
    print("Ha ingresado una contraseña correcta")                 # Si se cumple la condicion se ejecuta el print
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")   # Si no se cumple se ejecuta el print


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

from statistics import mode, median, mean          # del paquete statistics se importan solo las funciones mode, median, mean
# median: Retorna la mediana (valor central) de los datos numéricos, utilizando el método clásico de «media de los dos del medio»
# mean: Retorna la media aritmética, es decir, la suma de los valores dividida entre el número de observaciones. Es comúnmente denominada «promedio»
# mode: Retorna el valor más común del conjunto de datos discretos o nominales data.La moda (cuando existe) es el valor más representativo y sirve como medida de tendencia central.
import random

numeros_aleatorios = [random.randint(1, 100) for i in range(50)] #crea una lista con 50 números entre 1 y 100 elegidos de forma aleatoria.
moda = mode(numeros_aleatorios)         # La variable moda guarda el valor de la funcion mode, la que retorna el valor de la variable numeros_aleatorios.
mediana = median(numeros_aleatorios)    # La variable mediana guarda el valor de la funcion median, la que retorna los datos de la variable numeros_aleatorios.
media = mean(numeros_aleatorios)         # La variable media guarda el valor de la funcion mean, la que retorna el promedio de la variable numeros_aleatorios.

if media == mediana and media == moda:   # El condicional verifica si la variable media, mediana y moda son iguales
    print("No hay sesgo")               # Si se cumple esa condicion se ejecuta el print
elif media > mediana and mediana > moda:    # Si no se cumple se verifica si media es mayor a mediana y si mediana es mayor a moda
    print("Hay sesgo positivo")             # Si se cumple esa condicion se ejecuta el print
elif media < mediana and mediana < moda:    # Si no se cumple se verifica si media es menor a mediana y si mediana es menor a moda
    print("Hay sesgo negativo")             # Si se cumple esa condicion se ejecuta el print

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por 
# pantalla. 

frase = input("Ingrese una frase o palabra: ")      # La variable frase guarda el input solicitado al usuario
letraFinal = frase[-1].lower()                      # frase[-1] es el ultimo caracter de la variable frase, lower pasa el caracter a minuscula y se guarda en la variable letraFinal
if letraFinal == 'a' or letraFinal == 'e' or letraFinal == 'i' or letraFinal == 'o' or letraFinal == 'u':       # El condicional verifica que la variable letraFinal sea una vocal
    print(frase + "!")                               # Si se cumple la condicion se ejecuta el print, agregando el signo de exclamación
else:
    print(frase)                                    # Si no se cumple se ejecuta el print


# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
# dependiendo de la opción que desee: 
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.

# La variable nombre guarda el input solicitado al usuario
nombre = input("Ingrese su nombre: ")
# La variable opcion guarda el input solicitado, y el int lo transforma en un numero entero
opcion = int(input("""Si quiere su nombre en mayúsculas, ingrese 1.
Si quiere su nombre en minúsculas, ingres 2.
Si quiere su nombre con la primera letra mayúscula, ingrese 3."""))
# El condicional verifica si la variable opcion es igual a 1
if opcion == 1:
# Si se cumple la condicion se ejecuta el print.
# .upper() Convierte todos los caracteres a mayúsculas.
    print(nombre.upper())
# Si no se cumple se verifica la variable opcion es igual a 2
elif opcion == 2:
# Si se cumple la condicion se ejecuta el print.
# .lower() Convierte toda la frase a minúsculas
    print(nombre.lower())
# Si no se cumple se verifica la variable opcion es igual a 3
elif opcion == 3:
# Si se cumple la condicion se ejecuta el print.
# .title() Convierte la primera letra de cada palabra en mayúscula
    print(nombre.title())


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

# La variable magnitud guarda el input, float convierte el valor en un numero decimal
magnitud = float(input("Ingrese la magnitud del terremoto: "))
# El condicional verifica si la variable magnitud es menor a 3
if magnitud < 3:
# Si se cumple la condicion se ejecuta el print.
    print("La magnitud del terremoto es Muy Leve, imperceptible")
# Si no se cumple se verifica la variable sea mayor o igual que 3 y menor que 4
elif magnitud >= 3 and magnitud < 4:
# Si se cumple la condicion se ejecuta el print.
    print("La magnitud del terremoto es Leve, ligeramente perceptible")
# Si no se cumple se verifica la variable sea mayor o igual que 4 y menor que 5
elif magnitud >= 4 and magnitud < 5:
# Si se cumple la condicion se ejecuta el print.
    print("La magnitud del terremoto es Moderado, sentido por personas, pero generalmente no causa daños")
# Si no se cumple se verifica la variable sea mayor o igual que 5 y menor que 6
elif magnitud >= 5 and magnitud < 6:
# Si se cumple la condicion se ejecuta el print.
    print("La magnitud del terremoto es Fuerte, puede causar daños en estructuras débiles")
# Si no se cumple se verifica la variable sea mayor o igual que 6 y menor que 7
elif magnitud >= 6 and magnitud < 7:
# Si se cumple la condicion se ejecuta el print.
    print("La magnitud del terremoto es Muy Fuerte, puede causar daños significativos")
# Si no se cumple, se ejecuta el print
else:
    print("La magnitud del terremoto es Extremo, puede causar graves daños a gran escala")


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

