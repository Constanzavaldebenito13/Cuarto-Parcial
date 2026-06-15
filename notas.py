nombre= input("Ingrese nombre:")

notas = []

for i in range(3):
    nota = float(input(f"Introduce la nota {i + 1}: "))
    notas.append(nota)

suma= 0

for nota in notas:
    suma = suma+nota

promedio = suma / len(notas)

estudiante = {"Nombre" : nombre,
              "Notas" : notas, 
              "Promedio" : promedio
}

print("\nResumen")
print("____________________________________________")
print("Nombre:", estudiante ["Nombre"])
print("Nota:", estudiante ["Notas"])
print("Notas", estudiante ["Promedio"])