#Tipos de variables#

#Print#
print("Hola, me llamo miguel")
print("")
#print("01-Declarando variable")
nombre="Miguel" #a la variable nombre se le da el valor "Miguel"
nombre2="Pepe" #a la variable nombre2 se le da el valor "Pepe"
edad=44 #a la variable edad se le da el valor "44"
print("")
print("02-Impresion de una variable")
print(nombre)
print(nombre2)
print(edad)
print("Hola soy", nombre)
print("Tengo",edad,"años de edad")
print("")
print("03-Concadenacion") #Imprimir 2 variables en una misma concadenacion 
print("Hola me llamo",nombre2,"Y tengo",edad,"años")#Se usa la coma para cada separación
print(f"Hola me llamo {nombre} y tengo {edad} años")#Se utiliza "F-String (Cadena de formato)", Esto permite  incrustar variables en una cadena de caracteres de manera más sencilla
print("")
print("04-Actualizacion de una variable")
nombre2="Gonzalo" #La variable "nombre2" (Pepe) pasa a tener el valor de "Gonzalo"
print(f"Ahora me llamo {nombre2}")
print("")
print("05-Intruccion input")
name=input("¿Cual es tu nombre?\n") #Aca el INPUT se utiliza para rellenar la variable vacia escribiendola 
print(f"Tu nombre es {name}")