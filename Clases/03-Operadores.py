print("01-Operadores arimeticos")

#Se declaran variables para proceder al uso de operadores
a = 2
b = 6
c= 10
d = 30
print("")
#Operaciones comunes

print("suma entre dos números", a + b) 
print("multiplicación entre dos números", c*a)
print("Números elevados", b**a)
print("Resta de números", d - c)
print("División de números", d/a)
print("")
#Operaciones con flotantes

T= 2
D = 6
print("")
#Por consecuencia

V = T * D

#Declarando variables de tipo compleja

c1 = 4 + 3j
print(type(c1))

#Creando un número complejo con complex

c2 = complex(3, -5)
print("el numero complejo es:" ,c2)

print(c2.real) #Se obtiene la parte real del número complejo
print(c2.imag) #Se obtiene la parte imaginaria del número complejo

#¿Se puede multiplicar un String con un número entero?

print("Cadena de texto " * 3)
print("")

print("02-Operadores de comparación")
#Comparando términos numéricos

a = 1
b = 2
c = 3
d = 4
print("")
print("Comparando números")
#print(a == b) #b igual a
print(a != b) #es distinto a
print(a < b) #b es mayor que a
print(b < a) #a es mayor que b
print(c > d) #c es mayor que d
print(c < d) #d es mayor que c
print("")
#Comparando cadenas de caracteres
animal_doméstico = "perro"
animal_salvaje = "tigre"
print("")
print("Comparando cadenas de carácteres")
print(animal_doméstico == animal_salvaje)
print(animal_doméstico != animal_salvaje)
print(animal_doméstico > animal_salvaje)
print(animal_doméstico < animal_salvaje)
