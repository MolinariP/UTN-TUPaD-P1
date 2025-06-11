def suma_digitos(n):
    if n < 10:
        return n
    else:
        return n % 10 + suma_digitos(n // 10)

numero = int(input("Ingrese un número entero positivo: "))
print(f"La suma de los dígitos es: {suma_digitos(numero)}")
