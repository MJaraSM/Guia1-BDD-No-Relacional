# Guia1-BDD-No-Relacional
# Instalación de requisitos

Primero debemos instalar mongodb y compass
Luego descargamos alguna version de python3

Teniendo ambos instalados debemos ir a la carpeta bin de mongodb, ubicada en archivos del programa
para luego copiar la dirección de esa carpeta (ej:C:\Program Files\MongoDB\Server\7.0\bin) y luego
agregar esa dirección en las variables de entorno de Path.

Luego en consola ejecutamos el comando de mongod, luego en el disco C, creamos la carpeta data, 
dentro creamos la carpeta db y volvemos a ejecutar el comando de mongod y dejamos la terminal abierta.

Ya realizado lo anterior, creamos la base de datos y la colleción y agregamos las variables en el codigo.


# Variables del codigo

Las variables de HOST y PUERTO se deben cambiar segun corresponda
Las variables de database y collection igual se deben cambiar segun el nombre que se le dio, en este caso
la database se llamo Pokedex y la collection Pokemon.

Se llaman asi porque la base de datos que se creo es una pokedex, la cual es donde se almacenan los datos de 
los pokemones, en este caso, se cuenta con el numero del pokemon en la podekex, su nombre, y sus ambos tipos,
si no posee un segundo tipo, se completa con un ninguno.

# Funcionamiento

Para que el programa entrege alguna de las funciones del CRUD, se debe ingresar el numero de la opcion que se 
desea realizar y luego ir respondiendo segun se vayan pidiendo los datos para las variables.

Ejemplos:

Menu de selección
![image](https://github.com/MJaraSM/Guia1-BDD-No-Relacional/assets/145721388/d037fea1-053c-46ea-82b5-1fcde8c9e667)



