agenda = {}

print("A continuación podrá guardar 5 contactos:")
for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto #{i + 1}: ")
    telefono = input("Ingrese el número de teléfono: ")
    agenda[nombre] = telefono


consultar = input("\nIngresá el nombre del contacto que querés buscar: ")

# Mostrar resultado
if consultar in agenda:
    print(f"El número de {consultar} es: {agenda[consultar]}")
else:
    print(f"{consultar} no está en la agenda.")