# las llaves{} es como poner set(etc,etc,etc)
grupo1={"Marcos","Gabriela","Benjamin","Matias"}
grupo2={"Marcos","Nicolás","Diego","Matias"}
print("el grupo 1 contiene a :",grupo1)
print("el grupo 2 contiene a :",grupo2)
print("Pero en estos 2 grupos se repiten personas, los cuales son")
#el intersection hace un nuevo set solo con los elementos que estan en ambos sets
repetidos=grupo1.intersection(grupo2)
print(repetidos)
