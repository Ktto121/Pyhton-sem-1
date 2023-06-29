print("A continuacion debera poner 3 notas para los laboratorios del ramo de programación")
print("")
nota1=float(input("Introduzca el numero la primera nota: "))
nota2=float(input("Introduzca el numero la segunda nota: "))
nota3=float(input("Introduzca el numero la tercera nota: "))

promedio_ponderado=nota1*0.3+nota2*0.4+nota3*0.3

print("{:.2f}".format(promedio_ponderado))

if promedio_ponderado<4.0:
 print("El estudiante a reprobado la asignatura")
elif promedio_ponderado>=4.0 and promedio_ponderado<6.0:
 print("El estudiante aprobo la asignatura")
elif promedio_ponderado>=6.0:
 print("El estudiante aprobo con distinción")