# Solicitar dos números al usuario
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

# Comparar los dos números
if numero1 > numero2:
    print(f"El número {numero1} es mayor que {numero2}.")
elif numero1 < numero2:
    print(f"El número {numero1} es menor que {numero2}.")
else:
    print(f"El número {numero1} es igual a {numero2}.")
