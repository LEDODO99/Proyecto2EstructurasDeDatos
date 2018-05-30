#Mario Sarmientos 17055
#Sergio Marchena 16387 
#Mario Sarmientos  

from neo4j.v1 import GraphDatabase, basic_auth

#Establece el driver y la sesion de Neo4J
driver = GraphDatabase.driver("bolt:localhost:7474", auth=basic_auth("neo4j", "123"))#AGREGAR USERNAME Y PASSWORD PARA ACCESAR A NE0EJ.
session = driver.session()

#funcion para agregar canciones a la bd
def nuevaCancion(nombre,artista,genero,estado):
    session.run("CREATE (a:Cancion {nombre: {nombre}, artista: {artista}, genero: {genero},estado: {estado}})",
                {"nombre": nombre, "artista": artista, "genero": genero, "estado":estado})

#funcion para encontrar canciones por genero

def encontrarGenero(genero):
    cancion = session.run("MATCH (song:Cancion) WHERE song.genero = {genero}"
                          "RETURN song.nombre AS nombre, song.artista AS artista",
                          
                          {"genero":genero})
    print("\n")
    print("***estas canciones de acorde al genero podrian gustarte***\n")
    for dato in cancion:
        print(dato["nombre"] + " Artista: " + dato["artista"]+ " Genero: "+ genero )

#funcion automatica que genera los estados en la bd

#def crearEstado():
#    session.run("CREATE (a:Estado {estado:{State}}))",
#                {"State":"Felicidad"})
#    session.run("CREATE (a:Estado {estado:{State}}))",
#                {"State":"Tristesa"})
#    session.run("CREATE (a:Estado {estado:{State}}))",
#                {"State":"Extremo"})
                

#funcion para asociar canciones a estados de animo
#def asociacionGen(cancion,estado):
#    session.run("MATCH (cancion:Cancion),(estado:Estado)"
#                "WHERE cancion.nombre = {cancion} AND  estado.estado = {estado}"
#                "CREATE (cancion)-[:ESTADO] -> (estado)",
#                {"cancion":cancion,"estado":estado})

#funcion para encontrar canciones por estado de animo
def encontrarEstado(state):
    cancion = session.run("MATCH (song:Cancion) WHERE song.estado = {state}"
                "RETURN song.nombre AS nombre, song.artista AS artista, song.genero AS genero",
                {"state":state})
    print("\n")  
    print("***estas canciones de acorde a tu estado de animo podrian gustarte***\n")
    for dato in cancion:
        print ("Nombre: " + dato["nombre"] +" Artista: "+ dato["artista"] + " Genero: " + dato["genero"] + " Estado: " + state)

#funcion para encontrar canciones por artista
def encontrarArtista(artist):
    cancion = session.run("MATCH (song:Cancion) WHERE song.artista = {artist}"
                "RETURN song.nombre AS nombre, song.genero AS genero, song.estado AS estado",
                {"artist":artist})
    for dato in cancion:
        print ("Nombre: " + dato["nombre"] +" Artista: "+ artist + " Genero: " + dato["genero"] + " Estado: " + dato["estado"])
#funcion para encontrar cancion
def encontrarCancion(song):
    cancion = session.run("MATCH (song:Cancion) WHERE song.nombre = {name}"
                          "RETURN song.nombre AS nombre, song.artista AS artista, song.genero AS genero",
                          {"name":song})
    print("resultados para la busqueda: " + song + "\n")
    for dato in cancion:
        print("Nombre: " + song + " Artista: " + dato["artista"] + " Genero: "+dato["genero"]) 
#Extraer genero de cancion
def ExtraerGenero(song):
    cancion = session.run("MATCH (song:Cancion) WHERE song.nombre = {name}"
                          "RETURN song.genero AS genero",{"name":song})
    for info in cancion:
        genere = info["genero"]
    return genere

#Extrae el estado de una cancion
def ExtraerEstado(song):
    cancion = session.run("MATCH (song:Cancion) WHERE song.nombre = {name}"
                          "RETURN song.estado AS estado",{"name":song})
    for info in cancion:
        genere = info["estado"]
    return genere

#Extrae el artista de una cancion
def ExtraerArtista(song):
    cancion = session.run("MATCH (song:Cancion) WHERE song.nombre = {name}"
                          "RETURN song.artista AS artista",{"name":song})
    for info in cancion:
        genere = info["artista"]
    return genere

#Elimina una cancion de la base
def borrarCancion(song):
    cancion = session.run("MATCH (song:Cancion) WHERE song.nombre = {name}"
                          "RETURN song.nombre AS nombre, song.artista As artista",{"name":song})
    print("Se ha eliminado:")
    for dato in cancion:
        print("Nombre: "+dato["nombre"]+" Artista " + dato["artista"] + "\n")

#funcion para terminar conexion con bd
def Salir():
    session.close()
