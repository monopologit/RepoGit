# Solicitar el puntaje del examen al estudiante
puntaje = float(input("Ingresa el puntaje del examen (0-100): "))

# Determinar la calificación final según el puntaje
if puntaje >= 90:
    calificacion = "A"
elif puntaje >= 80:
    calificacion = "B"
elif puntaje >= 70:
    calificacion = "C"
elif puntaje >= 60:
    calificacion = "D"
else:
    calificacion = "F"

# Mostrar la calificación final
print(f"La calificación final es: {calificacion}")
