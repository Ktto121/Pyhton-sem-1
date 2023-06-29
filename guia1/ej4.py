print("A continuacion se le pedira escribir 2 nombres")
nombre1=input("Escriba el primer nombre: ")
nombre2=input("Escriba el segundo nombre: ")

letra_inicial1=nombre1[0]
#print(letra_inicial1)
letra_inicial2=nombre2[0]
#print(letra_inicial2)

letra_final1=nombre1[-1]
#print(letra_final1)
letra_final2=nombre2[-1]
#print(letra_final2)
print("")
if letra_inicial1==letra_inicial2:
    print("Las letras iniciales son iguales en los dos nombres")

elif letra_inicial1!=letra_inicial2:
     print("Las letras iniciales no son iguales en los dos nombres")

if letra_final1==letra_final2:
    print("Las letras finales son iguales en los dos nombres")
     
elif letra_final1!=letra_final2:
     print("Las letras finales no son iguales en los dos nombres")