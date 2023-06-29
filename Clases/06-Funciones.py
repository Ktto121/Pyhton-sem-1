print("########################### 01.Declarando una funcion simple ###########################")
# aca nombre de la funcion
def mi_primera_funcion():
    print("Mi primera funcion")
mi_primera_funcion()

print("########################### 02.Declarando una funcion y utilizacion ###########################")
#El concatenar junta listas
def concatenar(lista1,lista2):
    return lista1 + lista2
lista1=[1,2,3]
lista2=[4,5,6]
#aca se muestra el uso del concatenar
print(concatenar(lista1,lista2));

print("########################### 03.Declarando una funcion multiplicatiba ###########################")

def multiplicacion (num1,num2):
    return num1*num2
#dentro del parectesi de la multiplicacion son los num1 y num2
print(multiplicacion(10,5))
print("########################### 04.Funciones suma y resta (por telcado) ###########################")
def suma(a,b):
    return a + b
def resta(a,b):
    return a - b

#Aca es donde preguntamos al usuario que ingrese los 2 numeros
#Simpre que sean numeros definir como enteros antes(INT)
a=int(input("Ingrese el primer numero: "))
b=int(input("Ingrese el segundo numero: "))

resultado = suma(a,b)
print("El resultado de la suma es :",resultado)
resultado2 = resta(a,b)
print("El resultado de la resta es :",resultado2)