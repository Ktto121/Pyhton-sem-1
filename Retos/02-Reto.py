estudiante = input("Ingresar el nombre del estudiante: ")
asignatura = input("Ingresar el nombre de la asignatura: ")
nota1 = float(input("Ingresar la nota del primer laboratorio: "))
nota2 = float(input("Ingresar la nota del segundo laboratorio: "))

promedio = (nota1 * 0.3) + (nota2 * 0.7)

dic = {
    "Nombre_estudiante": estudiante,
    "Nombre_asignatura": asignatura,
    "nota_1": nota1,
    "nota_2": nota2,
    "promedio": round(promedio, 1)
}

print(dic)