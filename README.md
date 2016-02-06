### Aplicación de Bares y Tapas
Aplicación realizada para la asignatura de DAI e IV con Django.

# Proyecto-IV. Gestión de Hospitales
## Autor: César Albusac Jorge

[![Build Status](https://travis-ci.org/cesar2/Proyecto-IV.svg?branch=master)](https://travis-ci.org/cesar2/Proyecto-IV)

[![Build Status](https://snap-ci.com/cesar2/Proyecto-IV/branch/master/build_image)](https://snap-ci.com/cesar2/Proyecto-IV/branch/master)

[![Heroku](https://www.herokucdn.com/deploy/button.png)](https://dry-thicket-6813.herokuapp.com/)

Este proyecto lo voy a realizar junto a la aplicación de DAI, aprovechando el trabajo de la otra asignatura con ésta.


#Descripción
A priori, la aplicación consiste en una aplicación web, que, usando un framework de Python y una base de datos MongoDB, será capaz de realizar operaciones con formularios, uso de plantillas con Mako, manejo de sesiones con 
la clase Sessions de web.py, obtención de información mediante RSS, realización de gráficos ( Highcharts ),
operaciones con Google Maps, operaciones con Twitter, entre otros.

Aún no sé con certeza como será a ciencia cierta, por lo que podría cambiar ligeramente respecto al año pasado.

#Componentes de la aplicación

La aplicación está formada, de momento, por un archivo principal llamado [hospital.py](https://github.com/cesar2/Proyecto-IV/blob/master/ej3.py), que es el que realiza las funciones principales.

Se trata de una aplicación que devuelve diferentes htmls e imágenes según la ruta que se le pase en el 
navegador, así como manejador de errores.

En la carpeta [epydoc](https://github.com/cesar2/Proyecto-IV/tree/master/epydoc) se encuentra todo lo 
relacionado con la documentación de la aplicación. [Aquí](https://github.com/cesar2/IV/blob/master/Ejercicios_tema2.md#ejercicio-5) podemos ver como he realizado
la descripción y la instalación del mismo.

La carpeta [static](https://github.com/cesar2/Proyecto-IV/tree/master/static).
En epydoc está todo lo referente a la documentación.
En static se encuentran las imágenes y los archivos que serán estáticos, como los .css.


#Requerimientos:
En el archivo [requirements.txt](https://github.com/cesar2/Proyecto-IV/blob/master/requirements.txt) está especificado cuáles son las versiones de las diferentes herramientas que hemos usado para ejecutar la aplicación.
En el siguiente [enlace](https://github.com/cesar2/IV/blob/master/Ejercicios_tema2.md#ejercicio-4) describo cómo
ha de crearse el archivo requirements.txt. Para ejecutarlo(como veremos en .travis.yml), hay que escribir
$ pip install -r requirements.txt


#Desarrollo basado en pruebas:
En el archivo [test.py](https://github.com/cesar2/Proyecto-IV/blob/master/test.py) se encuentran los test que vamos a ejecutar.

En python , un framework para realizar test es **unittest**. Para poder usarlo, en nuestro código debemos importar unittest:

La documentación referente a los test con unittest se encuentra en el siguiente [enlace](https://docs.python.org/2/library/unittest.html).

He creado test.py que contendrá los test que quiero probar. Tenemos que importar unittest, así como HTMLparser.
Luego creamos una clase que contendrá los test, llamada  TestMethods:

![test_1](http://i1175.photobucket.com/albums/r629/Cesar_Albusac_Jorge/PracticayEjercicios2/test_zpsifti2npc.png)

![test_2](http://i1175.photobucket.com/albums/r629/Cesar_Albusac_Jorge/PracticayEjercicios2/test_2_zpsljdz4o0n.png)

Ahora, vamos al terminal y ejecutamos python test.py, lo que nos devuelve lo siguiente:

![test_terminal](http://i1175.photobucket.com/albums/r629/Cesar_Albusac_Jorge/PracticayEjercicios2/test_terminal_zpsupgkggag.png)

Y si quitásemos la imagen de /bicis , para comprobar si nos saldría el error: 

![test_terminal_error](http://i1175.photobucket.com/albums/r629/Cesar_Albusac_Jorge/PracticayEjercicios2/test_fallo_zpsxv0pi6a7.png)

Así , con la orde **python test.py** podemos ejectuar todos los test que queramos automáticamente, siempre que estén en su formato correcto dentro del archivo test.py( o como queramos llamarlo), como hemos visto anteriormente.

# Herramienta de construcción
Los tests que he realizado los he integrado dentro de las herramientas de construcción, incluyendo un objetivo make test en el achivo [makefile](https://github.com/cesar2/Proyecto-IV/blob/master/makefile).

Ahora pasamos a la configuración de la integración continua.

#Integración continua: [travis](https://travis-ci.org/)

Ahora tenemos que escoger un sistema de integración contínua para que cada vez
que se realice alguna modificación en nuestro repositorio, se vuelvan a ejecutar
de nuevo los test y nos muestre que todo ha funcionado correctamente.


He escogido [travis](https://travis-ci.org/) para realizar esta tarea, ya que me ha parecido sencillo y completo.

[Más información](https://github.com/cesar2/Proyecto-IV/blob/master/Documentacion/Integracion.md)


### Despliegue en un PaaS: [Heroku](https://www.heroku.com/)

Me he decantado por Heroku, ya que es sencillo y funciona muy bien. Se puede empezar desde 0 sin muchas
complicaciones. Debemos añadir los siguientes archicos a nuestro directorio donde está nuestra aplicación:

Aquí está el enlace a mi [aplicación en Heroku](https://dry-thicket-6813.herokuapp.com/).

[Más información](https://github.com/cesar2/Proyecto-IV/blob/master/Documentacion/Heroku.md)



### Entorno de pruebas: [Docker](https://www.docker.com/)

El entorno de pruebas que vamos a utilizar es Docker. Con esta plataforma podemos automatizar el despliege de las aplicaciones
en un contenedor software para poder probarla de manera aislada y poder desplegarla más rápidamente después.

La imagen de la app en Docker es [esta](https://hub.docker.com/r/cesar2/proyecto-iv/)

Para crear el entorno de pruebas, se debe ejecutar el comando:

`make docker`

[Más información](https://github.com/cesar2/Proyecto-IV/blob/master/Documentacion/Docker.md)

Inscripción al certamen:

![Inscripción al certamen:](http://i1175.photobucket.com/albums/r629/Cesar_Albusac_Jorge/Captura%20de%20pantalla%20de%202015-10-14%20130628_zpsxwzmjc7b.png)



