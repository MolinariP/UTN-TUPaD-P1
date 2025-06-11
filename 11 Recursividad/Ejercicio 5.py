def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])

palabra = input("Ingrese una palabra sin espacios ni tildes: ").lower()

if es_palindromo(palabra):
    print("Es palíndromo.")
else:
    print("No es palíndromo.")