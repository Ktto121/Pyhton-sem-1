#01 datos de tipo númerico
estatura = 1.65
peso = 68
complejo = 1 +4j
print ("Impresion del numero complejo:", complejo)

#operacion arimetica basica
imc= peso/estatura**2

#los ** Significa elevado
#print("Mi IMC es de {:.2f}".format(inc), "\n")

print("Mi IMC es de:",imc)
#Ahora con menos decimales
print("MI IMC es de {:.2f}".format(imc), "\n")
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

lenguaje = ("JavaScript")
print("Nuevo valor del Arreglo de un elemnto:", lenguaje)

#¿Como accedo a un elemento especifico de la lista?
print(estudiante[0])
print(estudiante[1])
print(estudiante[2])
print(estudiante[-3])
#Los numeros negativo hace que la lista sea del final hacia el inicio, Pero solo en Pyhton

#Inicializando  otra lista de datos mistos 
data_asig = [10023,"Programación",1,True]

 #¿Se pueden sumar listas? como suar lista de estudiante con los numeros

#tupla (NO MUTABLE)
grupo1 = ("Daniel","Cristian","Felipe",200,100,"Daniel")
print("###### 05-Tuplas ######")
print(type(grupo1))
#accediendo al primer elemnto de la tupla
print(grupo1[0])
#Consultando el elemento daniel cuantas veces se encuentra en la tupla. Count es cuantas veces se repite el elemento
print("El elemento se repite:",grupo1.count("Daniel"))
#Muestra el indice del primer elemento buscado. INDEX es posicion
print("Indice del elemento:", grupo1.index ("Cristian"))
#Reasignando el primer elemento de la tupla. (TUPLA NO MUTABLE) No se puede modificar

#grupo1[0] = "Constanza"
#print(grupo1)

#¿Se podran sumar Tuplas?

#Obteniendo un trozo de la tupla
grupo2 = ("Pedro",100,"Felipe","Diego",2020,"Alejandro")
print("Trozo de la tupla",grupo2[0:3])

#¿Entonces como no puedo modificar una tupla, que puedo hacer?

grupo1 = list(grupo1)
print("La tupla ahora es de tipo:",type(grupo1),"\n")
print("\n")
#Forma de inicializar un Set
conjunto_vacio = set()
conjunto_vacio1 = {}
print(type(conjunto_vacio))
conjunto_colores = set({"Azul","Rojo","Verda"})
conjunto_animales = {"Gato","Perro","Loro"}

print(type(conjunto_colores))
print(type(conjunto_animales))
print("El primer set contiene los siguientes colores:", conjunto_colores)
print("El segundo set contiene los siguientes animales:", conjunto_animales)


#print(conjunto_animales[2])
#No dejara acceder a la posicion con los SETS

conjunto_colores.add("Celeste")
print("El set de colores lo conforman:", conjunto_colores)
conjunto_animales.add("Lagarto")
print("El set de animales lo conforman:", conjunto_animales,)