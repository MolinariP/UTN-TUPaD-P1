frase = input("Ingrese una frase: ")

palabras = frase.split()

palabras_unicas = set(palabras)

print("\nPalabras únicas:", palabras_unicas)

recuento = {}
for palabra in palabras:
    recuento[palabra] = recuento.get(palabra, 0) + 1

print("Recuento:", recuento)