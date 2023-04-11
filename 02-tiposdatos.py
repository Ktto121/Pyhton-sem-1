#01 datos de tipo númerico
estatura = 1.65
peso = 68
complejo = 1 +4j
print ("Impresion del numero completjo:", complejo)

#operacion arimetica basica
inc= peso/estatura**2

#los ** Significa elevado
#print("Mi INC es de {:.2f}".format(inc), "\n")

print("Mi INC es de:",inc)
#Ahora con menos decimales
print("MI INC es de {:.2f}".format(inc), "\n")
#02 Datos de tipo cadena de caracteres
asignatura = "Programacion"
carrera = "Ingieneria civil en informatica"

print ("Mi carrera es", str(carrera), "Y me encuentro en la asignatura de", str(asignatura))

#03 valores de booleanos
ampolleta = False
interruptor = True

#con type sabemos el tipo de datos que estamos tratando
print(type(ampolleta))
print("la variable del interruptor es", type(interruptor))

#04 Datos tipo array (objeto de tipo colección)
estudiante = ["Jose", "Alfonso", "Diego", "Joaquin"]
num = [1,2,3,4,5,6]
print(estudiante) 
print(num)

#delcarando e inicializando una lista
nueva_lista = list()
print("Esta es una lista vacia:",nueva_lista)
otra_lista = []
print("Esta es otra lista vacia:",otra_lista)
print(type(otra_lista))

#¿Se puede realizar una una lista de datos compuesto?
compra_de_super =["Papa","Lechuga","Tomate","Papa"]
print("Esta es la lista de lo que debemos comprar en el super", compra_de_super)
print("En total son",len(compra_de_super),"\n""productos por comprar")

print(compra_de_super.count("Papa"))

lenguaje = ("JacaScript")
print("Nuevo valor del Arreglo de un elemnto:", lenguaje)

#¿Como accedo a un elemento especifico de la lista?
print(estudiante[0])
print(estudiante[1])
print(estudiante[2])
print(estudiante[-3])
#Los numeros negativo hace que la lista sea del final hacia el inicio, Pero solo en Pyhton

#Inicializando  otra lista de datos mistos 
data_asig = [10023,"Programación",1(True)]

 
 
 #¿Se pueden sumar listas?
 print("Suma de listas",estudiante[3], num)