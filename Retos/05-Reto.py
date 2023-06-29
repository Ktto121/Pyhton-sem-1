num = int(input("Ingrese un número: "))
i = num + 1

if num % 2 == 0:
    print ("- Es número par")
else:
    print ("- Es número impar")

if num % 2 == 1:
    print ("- Es un número primo")
elif num == 2:
    print("- Es un número primo")
else:
    print ("- No es un número primo")
    
if num > 50:
    print ("- Es mayor a 50")
elif num == 50:
    print ("- Es el mismo número")
else:
    print ("- Es menor a 50")