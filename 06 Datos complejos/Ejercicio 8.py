stock_productos = {
    "sardinas": 5,
    "atún": 7,
    "choclo": 9,
    "lentejas": 11
}

print("Productos actuales:", stock_productos)

producto = input("\nIngrese el nombre del producto a consultar: ").lower()

if producto in stock_productos:
    print(f"Stock actual de {producto}: {stock_productos[producto]} unidades")

    agregar = input("¿Desea agregar unidades al stock? (s/n): ").lower()
    if agregar == "s":
        unidades = int(input("¿Cuántas unidades desea agregar?: "))
        stock_productos[producto] += unidades
        print(f"Nuevo stock de {producto}: {stock_productos[producto]} unidades")
else:
    print(f"{producto} no existe en el stock.")
    agregar_nuevo = input("Desea agregarlo como nuevo producto? (s/n): ").lower()
    if agregar_nuevo == "s":
        unidades = int(input("¿Cuántas unidades desea agregar?: "))
        stock_productos[producto] = unidades
        print(f"{producto} fue agregado con {unidades} unidades.")

print("\nStock actualizado:", stock_productos)
