# Solicitar un número al usuario
numero = int(input("Ingresa un número: "))

# Verificar si el número es divisible por 3 y 5
if numero % 3 == 0 and numero % 5 == 0:
    print(f"El número {numero} es divisible por 3 y 5 al mismo tiempo.")
else:
    print(f"El número {numero} no es divisible por 3 y 5 al mismo tiempo.")
