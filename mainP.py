#Mario Sarmientos 17055


from proyecto import *
from random import *
print("Musical Recomendations")

#loop de programa
cond = False
while (cond == False):
    print("")
    print("1. Ingresar una cancion!")
    print("2. Buscar por genero")
    print("3. Buscar por estado de animo")
    print("4. Buscar por artista")
    print("5. Buscar cancion especifica")
    print("6. Salir")
    opc = (input("elija que desea hacer: "))

#acciones a ejecutar de acorde al usario
    if opc == "1":
        nombre = input("nombre de la cancion:")
        artista = input("nombre del artista: ")
        genero  = input("genero musical: ")
        estado = input("estado de animo: ")
        nuevaCancion(nombre,artista,genero,estado)
        
    if opc == "2":
        genero = input("De que genero desea encontrar canciones :")
        genero = str(genero)
        encontrarGenero(genero)
        
    if opc == "3":
        state = input("De que estado de animo te sientes? :")
        state = str(state)
        encontrarEstado(state)
    if opc == "4":
        artist = input("De que artista desea escuchar musica? :")
        artist = str(artist)
        encontrarArtista(artist)
    if opc == "5":
        song = input("Que cancion te gustaria escuchar? :")
        song = str(song)
        encontrarCancion(song)
        recomendacion = randint(1, 3)
        print("\n Estas canciones tambien te pueden gustar!!!\n")
        
        #recomendacion de canciones por genero
        if recomendacion == 1:
            encontrarGenero(str(ExtraerGenero(song)))
        #recomendacion de canciones por artista
        if recomendacion == 2:
            
            encontrarArtista(str(ExtraerArtista(song)))
        #recomendacion de canciones por estado    
        if recomendacion == 3:
            
            encontrarEstado(str(ExtraerEstado(song)))


    respuesta = input("Desea seguir? S/N ")
    while (respuesta != "S" and respuesta != "N"):
        print ("Por favor ingrese uno de los siguientes(S o N)")
        respuesta = input("Desea realizar otra accion? S/N")

    if (respuesta == "S"):
        cond == False
    else:
        Salir();
        cond = True
        print ("Gracias por usar el programa, esperamos verlo pronto.")
        
        


