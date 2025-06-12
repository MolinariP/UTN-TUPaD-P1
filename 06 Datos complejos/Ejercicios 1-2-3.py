precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
1450} 

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500 
precios_frutas['Pera'] = 2300 

print(f"\nEjercicio 1: {precios_frutas}")


precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700 
precios_frutas['Melón'] = 2800 

print(f"\nEjercicio 2: {precios_frutas}")



# lista_frutas = [precios_frutas.keys()]
lista_frutas = list(precios_frutas.keys())

print(f"\nEjercicio 3: {lista_frutas}")
