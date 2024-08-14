# Solicitar una cadena de texto al usuario
texto = input("Ingresa una cadena de texto: ")

# Solicitar la letra a buscar
letra = input("Ingresa la letra a buscar: ")

# Verificar que se haya ingresado solo una letra
if len(letra) != 1:
    print("Por favor, ingresa solo una letra.")
else:
    # Contar cuántas veces aparece la letra en el texto
    conteo = texto.count(letra)

    # Mostrar el resultado
    print(f"La letra '{letra}' aparece {conteo} veces en la cadena de texto.")
albert
