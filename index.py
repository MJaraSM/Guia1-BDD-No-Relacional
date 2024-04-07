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
seleccion = 0

def VerDatos():
    try:
        for pokemones in Collection.find():
            print(pokemones)
    except:
        print("A ocurrido un error")

def InsertarDatos():
    print("Vamos a añadir un nuevo pokemon")
    Numero = input("Primero, ingrese el numero de pokedex: ")
    Nombre = input("Ahora, ingrese el nombre del pokemon: ")
    Tipo1 = input("Ingrese el primer tipo del pokemon: ")
    Tipo2 = input("Para terminar, ingrese el segundo tipo, si no tiene, escriba ninguno: ")
    try:
        pokemon={"Numero":Numero,
                "Nombre":Nombre,
                "Tipo1":Tipo1,
                "Tipo2":Tipo2}
        Collection.insert_one(pokemon)
        print
    except pymongo.errors.ConnectionFailure as error:
        print(error)

def ModificarDatos():
    Valido = 0
    while Valido == 0:
        ID = input("Ingrese el ID del Pokemon a modificar: ")
        try:
            pokemon = Collection.find_one({"_id": ObjectId(ID)})
            break
        except:
            print("El id ingresado no es valido")
    print("Este es el pokemon a editar: ")
    print(pokemon)
    print("Ahora vamos a añadir los nuevos datos del pokemon")
    Numero = input("Ingrese el nuevo numero de la pokedex: ")
    Nombre = input("Ingrese el nuevo nombre del pokemon: ")
    Tipo1 = input("Ingrese el primer tipo del pokemon: ")
    Tipo2 = input("Ingrese el segundo tipo, si no tiene, escriba ninguno: ")
    nuevos_datos = {
            "Numero": Numero,
            "Nombre": Nombre,
            "Tipo1": Tipo1,
            "Tipo2": Tipo2
        }
    Collection.update_one({"_id": ObjectId(ID)}, {"$set": nuevos_datos})
    print("Pokemon modificado exitosamente.")

def EliminarDatos():
    Valido = 0
    while Valido == 0:
        ID = input("Ingrese el ID del Pokemon a eliminar: ")
        try:
            pokemon = Collection.find_one({"_id": ObjectId(ID)})
            break
        except:
            print("El id ingresado no es valido")
    if pokemon:
        print("Pokemon encontrado:")
        print(pokemon)
        confirmacion = input("¿Está seguro de que desea eliminar este Pokémon? (s/n): ")
        if confirmacion.lower() == "s":
            Collection.delete_one({"_id": ObjectId(ID)})
            print("Pokemon eliminado exitosamente.")
        else:
            print("Operación cancelada.")
    else:
        print("Pokemon no encontrado.")

try:
    cliente.server_info()
    print("Conexion a la BDD Exitosa")
    while(seleccion ==0):
        print("Seleccione la acción a realizar: ")
        print(" ")
        print("1. Ver")
        print("2. Insertar")
        print("3. Modificar")
        print("4. Eliminar")
        respuesta = input("Respuesta: ")
        if respuesta == "1":
            VerDatos()
        if respuesta == "2":  
            InsertarDatos()
        if respuesta == "3":
            ModificarDatos()
        if respuesta == "4":
            EliminarDatos()
        print(" ")
        print("¿Desea volver al menu inicial?")
        print("1. Si "+"    "+" 2. No")
        respuesta2 = input("Respuesta: ")
        print(" ")
        if respuesta2 == "2":
            break
    cliente.close()
except pymongo.errors.serverSelectionTimeoutError as errorTiempo:
    print("Tiempo exedido "+ errorTiempo)
except pymongo.errors.ConnectionFailure as errorConexion:
    print("Error de conexion"+errorConexion)
