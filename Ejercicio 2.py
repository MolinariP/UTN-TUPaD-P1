def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


posicion = int(input("Ingrese la posición hasta donde desea ver la serie de Fibonacci: "))
for i in range(posicion + 1):
    print(fibonacci(i), end=" ")
