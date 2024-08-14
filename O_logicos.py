# Solicitar un número al usuario
numero = float(input("Ingresa un número: "))

# Verificar si el número es par y positivo
if numero > 0 and numero % 2 == 0:
    print(f"El número {numero} es par y positivo.")
else:
    print(f"El número {
          numero} no cumple con ambas condiciones (par y positivo).")
