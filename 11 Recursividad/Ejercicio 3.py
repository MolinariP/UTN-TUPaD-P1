def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)


base = int(input("Ingrese el número base: "))
exponente = int(input("Ingrese el exponente: "))
print(f"El resultado es = {potencia(base, exponente)}")
