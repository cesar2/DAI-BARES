### Despliegue en un PaaS: [Heroku](https://www.heroku.com/)


[![Heroku](https://www.herokucdn.com/deploy/button.png)](http://app-bares-cesar.herokuapp.com/rango/)

[![Build Status](https://snap-ci.com/cesar2/DAI-BARES/branch/master/build_image)](https://snap-ci.com/cesar2/DAI-BARES/branch/master)

También tengo la aplicación en Azure:

[![Azure](http://azuredeploy.net/deploybutton.png)](http://cesar-service-hxtco.cloudapp.net/rango/)


Me he decantado por Heroku, ya que es sencillo y funciona muy bien. Se puede empezar desde 0 sin muchas
complicaciones. Debemos añadir los siguientes archicos a nuestro directorio donde está nuestra aplicación:

[Procfile](https://github.com/cesar2/DAI-BARES/blob/master/Procfile):

```
web: gunicorn ejemeplo.wsgi --log-file -
```

[requirements.txt](https://github.com/cesar2/DAI-BARES/blob/master/requirements.txt):

```
Django==1.7
argparse==1.2.1
django-appconf==1.0.1
django-classy-tags==0.6.2
django-bootstrap-toolkit==2.15.0
django-registration-redux==1.3
django-easy-maps==0.9.2
Pillow==2.9.0
geopy==1.11.0
six==1.10.0
wsgiref==0.1.2
dj-database-url==0.3.0
dj-static==0.0.6
django-toolbelt==0.0.1
djangorestframework==3.3.1
foreman==0.9.7
futures==3.0.3
gunicorn==19.3.0
psycopg2==2.4.5
requests==2.8.1
requests-futures==0.9.5
static3==0.6.1
wheel==0.26.0
whitenoise==2.0.4
```

Tenemos que hacer los siguientes pasos:
1. Clonamos el repositorio que deseamos desplegar:

![heroku1](http://i1155.photobucket.com/albums/p543/cesypozo/Ejercicios%20tema%206/Captura%20de%20pantalla%20de%202016-01-19%20183648_zpsnfauslmv.png)

2. Ahora, creamos en heroku la aplicación , con ```heroku create <nombre_de_la_aplicacion>```:
![heroku3](http://i1155.photobucket.com/albums/p543/cesypozo/Ejercicios%20tema%206/Captura%20de%20pantalla%20de%202016-01-19%20183712_zpsodc8qli1.png)

3. A continuación, ejecutamos ```git push heroku master``` para subir la aplicación:
![heroku2](http://i1155.photobucket.com/albums/p543/cesypozo/Ejercicios%20tema%206/Captura%20de%20pantalla%20de%202016-01-19%20183728_zpshph7w1fu.png)

4. Abrimos la aplicación con ```heroku open```:
![heroku4](http://i1155.photobucket.com/albums/p543/cesypozo/Ejercicios%20tema%206/Captura%20de%20pantalla%20de%202016-01-19%20183812_zpsz46gaou6.png)

Esta es la aplicación ya desplegada en Heroku: [http://app-bares-cesar.herokuapp.com/rango/](http://app-bares-cesar.herokuapp.com/rango/)

Ahora añadimos un proceso de integración contínua junto al despliegue automático mediante, que se puede hacer desde el mismo Heroku o con [Snap CI](https://snap-ci.com/).

Con HEROKU:

Conectamos la app de Heroku con GitHub con la siguiente configuración:
Para configurar el despliegue automático utilizo Travis CI, diciéndole a Heroku que no despliegue hasta pasar los test:
![ej7_1](http://i1175.photobucket.com/albums/r629/Cesar_Albusac_Jorge/Ejercicios3/ej6_zpst9n0fbx7.png)
![ej7_2](http://i1175.photobucket.com/albums/r629/Cesar_Albusac_Jorge/Ejercicios3/ej7_zpszhtkczyg.png)

Y aquí con Snap CI:
![ej7_3](http://i1175.photobucket.com/albums/r629/Cesar_Albusac_Jorge/Ejercicios3/ej7_3_zpssdl6by1e.png)

Aquí está el enlace a mi [aplicación en Heroku](http://app-bares-cesar.herokuapp.com/rango/).

