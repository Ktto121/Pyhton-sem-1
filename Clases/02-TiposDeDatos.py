
print("# Tipo de datos #")


print("01-Datos de tipos numerico")

#() Son paréntesis
#[] Son corchetes
#{} Son llaves

estatura = 1.65 #Tipo "Float". Aquellos que pueden contener una parte decimal.
peso = 72 #Tipo "Int". Son los numeros enteros sin parte decimal.
edad = 24
complejo = 1 + 4j #Tipo complejo

#Tipo "Complex". Son numeros complejos Se declaran usando la "j" para la parte imaginaria.
#La variable "complejo" tendra el valor "1 + 4i". Tambien se declaran: z = complex(2, 3)
complejo = 1 + 4j

print(f"Mi estatura es de {estatura} m y mi peso es de {peso} Kg") #Impresion de la variable "estatura" y "peso" en un f-string.
print("Impresion del numero complejo",complejo) #Impresion de un numero complejo.
print("")
imc=peso / estatura**2 #los "**" es un elevado, y el "/" es una division, aca estamos haciando que una variables sea una operacion
print(f"Mi masa corporal es de {imc}")
print("Mi masa corporal(IMC) es de: {:.2f}".format(imc)) #Con el {:.2f} lo que hacemos es que indicamos que solo se vizualize hasta 2 decimales, y el ".format" se le pone un parentesis donde ira la variable

#Para transformar un numero real a uno entero se usaria el INT
print("Transformando un valor a entero:",int(estatura))
#Para transformar un numero entero a uno real se usaria el FLOAT
print("Transformando un valor a real:",float(edad))
print("")
print("Datos de tipo cadena de caracteres")
asignatura="Programación"
carrera="Ingenieria civil en informatica"
print(f"La agisnatura de {asignatura} corresponde de la carrera de {carrera}")
#Utilizando LEN
#Lo que hace LEN es que cuenta los caracteres de las variables
print("La cantidad de caracteres de la palabra",asignatura,"es de :",len(asignatura))
print("La cantidad de caracteres de la palabra",carrera,"es de :",len(carrera)) #El LEN tambien cuenta los espacios
print("")
print("03-Datos de tipos booleanos")
ampolleta=True #La variable esta encendida
interruptor=False #La varible esta apagada

print("La variable \"ampolleta\" es de tipo:", type(ampolleta)) #Type para saber el tipo de variable.
print("La variable \"estatura\" es de tipo:", type(estatura)) #Type para saber el tipo de variable.
print("La variable \"peso\" es de tipo:", type(peso)) #Type para saber el tipo de variable.
print("La variable \"complejo\" es de tipo:", type(complejo))  #Type para saber el tipo de variable.
print("La variable \"carrera\" es de tipo:", type(carrera))  #Type para saber el tipo de variable.
print("")
print(bool(0))
print(bool("")) #Las 2 comillas se conocen como "vacío"
print(bool(None))
print(bool("False"))#Da true ya que lo toma como una palabra en sí, no como un dato
print(bool(1))
print("")
print("04-Datos de tipos listas")
estudiantes=["Matias","Marcos","Cristobal","Sebastian"]#una variable como una lista de elementos STR
num=[1,2,3,4,5,6]#una variable como lista de elementos INT
print(f"Los estudiantes son {estudiantes}")
print(f"Los numeros que contiene un dado son {num}")
nueva_lista=list() #Esta es una forma de hacer una list, esta vacia
print(f"la nueva lista es {nueva_lista}")
otra_lista=[]#Esta es una formamas sencilla de hacer una lista
print(f"Esta es la otra lista {otra_lista}")
print("")
print("La variable \"nueva_lista\" es de tipo:", type(nueva_lista))
print("La variable \"otra_lista\" es de tipo:", type(otra_lista))
print("")
#Otras listas
grupo = ["Benjamín", "Raul", "Miguel", "Augusto", "Raul"]
numeros = [1,2,3,4,5,6]
lenguaje = ["Phyton"]

#Las comas para separar palabras son demasiado importantes

lista_compuesta = ["Matias", 28, True, 25.6]
data = ["Osorno", {"UV": "nivel bajo" ,"temp °C": 18}, (-40.7464, -70.8383)]#Esto es un Diccionario
print("Esta es la lista compuesta: ", lista_compuesta)
print("Esta es la otra lista compuesta: ", data)
print("Esta es una lista de cadenas de caracteres:", estudiantes)
print("Esta es una lista de numeros:", num)
print("Esta es una lista de un elemento:", lenguaje)
print("Esto igual es una lista:", data)
print("")
print("El numero de elementos en la lista DATA es de: ",len(data))#Si usamos LEN para una lista este contara los elementos que se encuentras en la lista
print("¿Cuantas veces se repite Raul en la lista GRUPO?: ", grupo.count("Raul"))#Con el COUNT se cuenta cuantas veces esta el elemento en la lista
print("")
lenguaje = ["Javascript"] #Cambiamos el elemento que se encontraba en la lista(Antes el elemento era Python)
print("Nuevo valor del arreglo de un elemento:" ,lenguaje, "\n")

#¿Como se accede a un elemento especifico de una lista?
print("Posicion 1 de la lista ESTUDIANTES es: ",estudiantes[0])#De esta forma podemos acceder a la una posicion, El primer elemento siempre el 0
print("Posicion 2 de la lista ESTUDIANTES es: ",estudiantes[1])
print("Posicion -2 de la lista ESTUDIANTES es: ",estudiantes[-2])#Si ponemos un numero negativo, la lista empezara del final, entonces el -1 seria el ultimo elemento y el -2 el penultimo

#Reasignando el valor de un elemento de la lista.
estudiantes[3] = "Gabriela" 
print("El arreglo de estudiantes es:" ,estudiantes)

#Asigna valores de una lista a variables #Desempaqueta elementos 
data_asig = [10023, "Programacion", 1, True]
cod,ramo,semestre,estado = data_asig
print(ramo)

#¿Se pueden sumar listas?
print("Suma de listas:" ,estudiantes + num)

#¿Que hace estas funciones?
print(list("Phyton")) #Transforma el str "Phyton" en una lista.
print(list(range(10))) #Imprime una lista de rango 10 (0-9)
print("\n") #Salto de linea
print("")
print("05-dato de tipo tuplas") #las tuplas no son mutables

grupo1 = ("Daniel", "Roberto", "Vicente", 200, 100, "Daniel")
print("La variable \"grupo1\" es de tipo:", type(grupo1))

grupo2 = ("Diego", "Matias", "2020", "Alberto", "100", "Pepe")

#Accediendo al primer elemento de la tupla.
print(grupo1[0])

#Consultando el elemento Daniel cuantas veces se encuentra en la tupla
print("El elemento \"Daniel\" se repite:", grupo1.count("Daniel"), "veces")

#Muestra el indice del primer elemento buscado
print("El indice del elemento \"Daniel\" es:", grupo1.index("Daniel"))

#Se pueden sumar las tuplas
print("Suma de tuplas:", grupo1 + grupo2)

#Obteniedo un trozo de la tupla
print("Trozo de la tupla:", grupo2[0:3])

#¿Entonces como puedo modificar una tupla?
grupo1 = list(grupo1)
print("La tupla ahora es de tipo:", type(grupo1))
print("")

print("06-Datos de tipo sets")

#Tanto diccionario como "set" utiliza las llaves

conjunto_vacio = set()
conjunto_vacio1 = {}
conjunto_colores = set({"Azul", "Rojo", "Verde"})
conjunto_animales = {"Gato", "Perro", "Loro"}

print("\"conjuto_colores\" es de tipo:", type(conjunto_colores))
print("\"conjuto_vacio1\" es de tipo:", type(conjunto_vacio1))
print("\"conjuto_colores\" es de tipo:", type(conjunto_colores))
print("\"conjuto_animales\" es de tipo:", type(conjunto_animales))
print("")

#print(conjunto_animales[0]) #Accediendo al primer elemento del set
conjunto_colores.add("Celeste")
print("El set de colores lo conforman:", conjunto_colores)

conjunto_animales.add("Gato")
print("El set de animales lo conforman:", conjunto_animales)
print("")
print("07-Diccionario")
#Estas son las 2 formas de hacer un diccionario
diccionario = dict()
diccionario2 = {}

datos_personales = {
    "Nombre":"Miguel",
    "Institución":"ulagos",
    "Edad":"19",
    "Asignaturas":{"Quimica","Programación"}
    }
print("Diccionario inicial:",datos_personales)

#Las claves son únicas para cada valor // No se puede utilizar posiciones como el 0,1,2,3 para print

print(datos_personales["Institución"])

#Agregando un nuevo valor a una clave del diccionario

datos_personales["Institución"] = "Hollward"

#Agregando una nueva clave al diccionario

datos_personales ["Ciudad"] = "Rio Bueno"
print("Diccionario con el nuevo campo: ",datos_personales)

#Eliminando una clave del diccionario
                 
del datos_personales["Ciudad"]
print(datos_personales)



