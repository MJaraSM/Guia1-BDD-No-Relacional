import pymongo
from bson.objectid import ObjectId

HOST="localhost"
PUERTO="27017"
TIME_OUT=1000

URL="mongodb://"+HOST+":"+PUERTO+"/"

database="Pokedex"
collection="Pokemon"
cliente = pymongo.MongoClient(URL, serverSelectionTimeoutMS=TIME_OUT)
BaseDatos = cliente[database]
Collection = BaseDatos[collection]

def VerDatos():
    try:
        cliente.server_info()
        print("Conexion Exitosa")
        for pokemones in Collection.find():
            print(pokemones)
        print(" ")
        for pokemones in Collection.find():
            print(str(pokemones["Numero"])+" "+pokemones["Nombre"]+" "+pokemones["Tipo1"]+" "+pokemones["Tipo2"])
        cliente.close()
    except pymongo.errors.serverSelectionTimeoutError as errorTiempo:
        print("Tiempo exedido "+ errorTiempo)
    except pymongo.errors.ConnectionFailure as errorConexion:
        print("Error de conexion"+errorConexion)

def InsertarDatos():
    Numero=1
    Nombre="Bulbasaur"
    Tipo1="Planta"
    Tipo2="Ninguno"
    try:
        pokemon={"Numero":Numero,
                "Nombre":Nombre,
                "Tipo1":Tipo1,
                "Tipo2":Tipo2}
        Collection.insert_one(pokemon)
    except pymongo.errors.ConnectionFailure as error:
        print(error)

def ModificarDatos():
    #Recordatorio = Mantener la id actualizada si lo borra mas adelante
    ID = "660e14fb39d5807fddffcf38"
    pokemon= Collection.find({"_id": ObjectId(ID)})[0]
    print(pokemon)
    #Seleccione los datos a cambiar
    nuevos_datos = {
            "Numero": 9,
            "Nombre": "Blastoise",
        }
    Collection.update_one({"_id": ObjectId(ID)}, {"$set": nuevos_datos})
    print("Pokemon modificado exitosamente.")
    pokemon= Collection.find({"_id": ObjectId(ID)})[0]
    print(pokemon)

def EliminarDatos():
    ID = "660e14fb39d5807fddffcf38"
    # Buscar el Pokémon por su ID
    pokemon = Collection.find_one({"_id": ObjectId(ID)})
    if pokemon:
        print("Pokemon encontrado:")
        print(pokemon)
        # Confirmar si se desea eliminar
        confirmacion = input("¿Está seguro de que desea eliminar este Pokémon? (s/n): ")
        if confirmacion.lower() == "s":
            # Eliminar el documento de la colección
            Collection.delete_one({"_id": ObjectId(ID)})
            print("Pokemon eliminado exitosamente.")
        else:
            print("Operación cancelada.")
    else:
        print("Pokemon no encontrado.")

#Seleccione la parte del crud que quiere probar
#VerDatos()
#InsertarDatos()
#ModificarDatos()
#EliminarDatos()
