"""Crear una agenda telefonica que contenga un solo contacto. Esta agenda se debe
guardar en un diccionario. Este diccionario debe contar con las siguientes claves:
Nombre
Direccion
Ciudad
Numero telefonico
A continuacion, agrega una nueva clave llamada “Redes Sociales” que contenga al
menos tres nombres de perfil de diferentes redes sociales (por ejemplo, Facebook,
Instagram y Twitter). Por ultimo, se solicita imprimir solamente el Facebook del
contacto y luego la agenda completa actualizada."""

agenda={
    "Nombre":"Vicente",
    "Direccion":"2198 Ejército Libertador",
    "Ciudad":"Rio Bueno",
    "Numero telefonico":"+569****3803"
}

redes_sociales={
    "Facebook":"Vicente Inostroza",
    "Instagram":"_vicho255",
    "Twitter":"Vicho25"
}

agenda.update({"Redes Sociales":redes_sociales})

print("El Facebook es: ",redes_sociales["Facebook"])
print(agenda)