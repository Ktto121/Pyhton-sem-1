print("Ingresar los 3 lados de un triagulo para saber si es equilatero, isoceles o escaleno")
lado1=int(input("Ingrese su primer lado: "))
lado2=int(input("Ingrese su segundo lado: "))
lado3=int(input("Ingrese su tercer lado: "))

triangulo1=lado1 and lado2 and lado3

if lado1==lado2==lado3:
 print("El triangulo es un equilatero")
elif lado1==lado2  or lado2==lado3 or lado3==lado1:
 print("El triangulo es un isosceles")
elif lado1!=lado2!=lado3:
 print("El triangulo es un escaleno")

###Sacar area###
p=lado1+lado2+lado3/2
area=p*(p-lado1)*(p-lado2)*(p-lado3)
print("Y el area del triangulo es: ",area)