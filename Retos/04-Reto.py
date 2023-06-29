#Rellenar datos de cada paciente
paciente1=input("introduzca el nombre del primer paciente\n")
peso1=input("introduzca el peso del primer paciente\n")
estatura1=input("introduzca la estatura del primer paciente\n")
edad1=input("introduzca la edad del primer paciente\n")

paciente2=input("introduzca el nombre del segundo paciente\n")
peso2=input("introduzca el peso del segundo paciente\n")
estatura2=input("introduzca la estatura del segundo paciente\n")
edad2=input("introduzca la edad del segundo paciente\n")

paciente3=input("introduzca el nombre del tercer paciente\n")
peso3=input("introduzca el peso del tercer   paciente\n")
estatura3=input("introduzca la estatura del tercer paciente\n")
edad3=input("introduzca la edad del tercer paciente\n")

###TUPLAS###
t1=(paciente1,peso1,estatura1,edad1)
t2=(paciente2,peso2,estatura2,edad2)
t3=(paciente3,peso3,estatura3,edad3)

#Muestra todos los datos que han sido rellenado
print("######## Datos del primer paciente ########")
print(t1)

print("######## Datos del segundo paciente ########")
print(t2)

print("######## Datos del tercer paciente ########")
print(t3)