#Integración continua: [travis](https://travis-ci.org/) 

He escogido [travis](https://travis-ci.org/) para realizar esta tarea.
En primer lugar, tenemos que darnos darnos de alta con nuestro usuario de GitHub, y autorizar la aplicación:
![Autorizar](http://i1175.photobucket.com/albums/r629/Cesar_Albusac_Jorge/ejercicio7_zpsotpqhn1p.png)

Después, debemos activar el repositorio en el que queremos activar la integración continua:
![activar](http://i1175.photobucket.com/albums/r629/Cesar_Albusac_Jorge/travis_aceptar_zpsu1wthpo4.png)

El archivo [.travis.yml](https://github.com/cesar2/Proyecto-IV/blob/master/.travis.yml) es el que vamos a usar para la integración continua.

Al crear el archivo de configuración de la integración continua, en este caso es un archivo .yml, indicamos entre
otras cosas, el lenguaje que usamos, la versión, cómo instalar dependencias y ejecutar los tests:
![arhivo_travis](http://i1175.photobucket.com/albums/r629/Cesar_Albusac_Jorge/PracticayEjercicios2/archivo_travis_zpsbncg84el.png)


Añadimos en nuestro repositorio el fichero **.travis.yml**  y automáticamente, en la página de travis se ejecutarán la integración:
![integracion](http://i1175.photobucket.com/albums/r629/Cesar_Albusac_Jorge/travis4_zpsnqeocjvs.png)

![test_travis](http://i1175.photobucket.com/albums/r629/Cesar_Albusac_Jorge/travis2_zpsift8yffn.png)

