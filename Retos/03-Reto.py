ciudades = ["Santiago", "Temuco", "Osorno", "Punta arena"]
ica = [134, 99, 245, 50]

minimo=ica.index(min(ica))
print(f"La ciudad con el indice más bajo es {ciudades[minimo]} con un indice de {ica[minimo]} ICA")
maximo=ica.index(max(ica))

print(f"La ciudad con el indice más alto es {ciudades[maximo]} con un indice de {ica[maximo]} ICA")