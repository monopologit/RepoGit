# Solicitar al usuario que ingrese dos números
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

# Calcular la suma de los dos números
suma = numero1 + numero2

# Mostrar el resultado
print(f"La suma de {numero1} y {numero2} es: {suma}")


edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Eres mayor de edad.")

else:
    print("No eres mayor de edad")

numero3 = int(input("Ingrese un numero: "))
numero4 = int(input("Ingrese otro numero: "))
if numero3 == numero4:
    print("Son iguales")
else:
    print("Son distintos")
