def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

numero = int(input("Ingrese un número en base decimal: "))
binario = decimal_a_binario(numero)
if binario != "":
    print("El número en binario es:", binario)
else:
    print("El número en binario es: 0")