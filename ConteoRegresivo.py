# Solicitar un número inicial al usuario
numero_inicial = int(input("Ingresa un número inicial: "))

# Imprimir los números en orden descendente hasta llegar a cero
for numero in range(numero_inicial, -1, -1):
    print(numero)
