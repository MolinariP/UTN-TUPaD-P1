# Diccionario original: país → capital
paises_capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Paraguay": "Asunción"
}

capitales_paises = {}
for pais, capital in paises_capitales.items():
    capitales_paises[capital] = pais

print("Original:", paises_capitales)
print("Invertido:", capitales_paises)

