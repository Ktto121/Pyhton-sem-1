print("Escribir un programa que pida al usuario ingresar dos palabras y las guarde en")
print("dos variables diferentes. Luego imprimir cúal palabra tiene más caracteres y cúal")
print("tiene menos caracteres.")
print("")
print("A continuacion escriba 2 palabras diferentes")
p1=(input("ingrese la primera palabra: "))
p2=(input("ingrese la segunda palabra: "))

caracter1=len(p1)
caracter2=len(p2)
if caracter1>caracter2:
    caracter_mayor=p1
    caracter_menor=p2

if caracter1<caracter2:
    caracter_mayor=p2
    caracter_menor=p1
print("la palabra con mayor caracteres es: ", caracter_mayor)
print("la palabra con menor caracteres es: ", caracter_menor)