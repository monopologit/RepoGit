# Solicitar un número al usuario
numero = int(input("Ingresa un número entre 1 y 100: "))

# Verificar si el número está dentro del rango
if 1 <= numero <= 100:
    print(f"El número {numero} está dentro del rango permitido.")
else:
    print(f"El número {
          numero} está fuera del rango permitido. Por favor, ingresa un número entre 1 y 100.")
