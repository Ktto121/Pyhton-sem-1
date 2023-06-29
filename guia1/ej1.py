print("Realizar un algoritmo que indique el numero menor y el numero mayor entre tres")
print("enteros leidos por consola. Solo se deben ingresar numeros enteros.")
print("")
print("Ingrese 3 numeros enteros")
n1=int(input("Ingrese el primer numero: "))
n2=int(input("Ingrese el segundo numero: "))
n3=int(input("Ingrese el terdcer numero: "))

#######Numero mayor#####
if n1>n2 and n1>n3:
    numero_mayor=n1
if n2>n1 and n2>n3:
    numero_mayor=n2
if n3>n1 and n3>n2:
    numero_mayor=n3

#######Numero menor#####
if n1<n2 and n1<n3:
    numero_menor=n1
if n2<n1 and n2<n3:
    numero_menor=n2
if n3<n1 and n3<n2:
    numero_menor=n3

print("El numero mayor es", numero_mayor)
print("El numero menor es", numero_menor)