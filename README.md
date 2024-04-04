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
la database se llamo Pokedex y la collection Pokemon

Para que el programa entrege alguna de las funciones del CRUD, se debe de descomentar al final del codigo la 
funcion que se desea realizar.
