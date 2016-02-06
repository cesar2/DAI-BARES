### Despliegue en un PaaS: [Heroku](https://www.heroku.com/)

Me he decantado por Heroku, ya que es sencillo y funciona muy bien. Se puede empezar desde 0 sin muchas
complicaciones. Debemos añadir los siguientes archicos a nuestro directorio donde está nuestra aplicación:

[Procfile](https://github.com/cesar2/Proyecto-IV/blob/master/Procfile):

```
web: python ej3.py
```

[requirements.txt](https://github.com/cesar2/Proyecto-IV/blob/master/requirements.txt):

```
Flask==0.10.1
gunicorn==19.3.0
html5lib==0.999
itsdangerous==0.24
Jinja2==2.8
MarkupSafe==0.23
requests==2.2.1
six==1.5.2
ssh-import-id==3.21
urllib3==1.7.1
virtualenv==13.1.2
Werkzeug==0.10.4
WTForms==2.0.2
wheel==0.24.0
yolk==0.4.3
```

Tenemos que hacer los mismos pasos que hicimos en la app básica del [Ejercicio5](https://github.com/cesar2/IV/blob/master/Ejercicios_tema3.md#ejercicio-5) , 
pero ahora con nuestro repositorio y nuestros archivos.

![heroku1](http://i1175.photobucket.com/albums/r629/Cesar_Albusac_Jorge/Ejercicios3/heroku_zpsvogggkv9.png)
![heroku2](http://i1175.photobucket.com/albums/r629/Cesar_Albusac_Jorge/Ejercicios3/heroku3_zps9vauwcii.png)
![heroku3](http://i1175.photobucket.com/albums/r629/Cesar_Albusac_Jorge/Ejercicios3/heroku2_zpszfwwrm0t.png)

Esta es la aplicación ya desplegada en Heroku: [https://dry-thicket-6813.herokuapp.com/](https://dry-thicket-6813.herokuapp.com/)

Ahora añadimos un proceso de integración contínua junto al despliegue automático mediante, que se puede hacer desde el mismo Heroku o con [Snap CI](https://snap-ci.com/).

Con HEROKU:

Conectamos la app de Heroku con GitHub con la siguiente configuración:
Para configurar el despliegue automático utilizo Travis CI, diciéndole a Heroku que no despliegue hasta pasar los test:
![ej7_1](http://i1175.photobucket.com/albums/r629/Cesar_Albusac_Jorge/Ejercicios3/ej6_zpst9n0fbx7.png)
![ej7_2](http://i1175.photobucket.com/albums/r629/Cesar_Albusac_Jorge/Ejercicios3/ej7_zpszhtkczyg.png)

Y aquí con Snap CI:
![ej7_3](http://i1175.photobucket.com/albums/r629/Cesar_Albusac_Jorge/Ejercicios3/ej7_3_zpssdl6by1e.png)

Aquí está el enlace a mi [aplicación en Heroku](https://dry-thicket-6813.herokuapp.com/).




