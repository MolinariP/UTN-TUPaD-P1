def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

niveles = int(input("Ingrese la cantidad de bloques que desea colocar en la base: "))
print(f"El total de bloques necesarios para construir la pirámide es de: {contar_bloques(niveles)} bloques")
