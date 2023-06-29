def frase(i):
    palabra = i.split()   
    largo = len(i)
    diccionario = {
        "Palabras" : palabra,
        "Longitud" : largo,
        }

    print (diccionario)
    
    
frase(input("Introduzca una frase: "))
