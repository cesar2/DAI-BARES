## Entorno de pruebas: [Docker](https://www.docker.com/)

Para crear la imagen, Docker usa un fichero dentro del código de la aplicación llamado [Dockerfile](https://github.com/cesar2/Proyecto-IV/blob/master/Dockerfile) 
para la construcción de la imagen, que en mi caso contiene lo siguiente:

```
FROM ubuntu:latest

#Autor
MAINTAINER Cesar Albusac Jorge <cesypozo@gmail.com>

#Actualizar Sistema Base
RUN sudo apt-get -y update

#Descargar aplicacion 
RUN sudo apt-get install -y git
RUN sudo git clone https://github.com/cesar2/Proyecto-IV.git

#Instalar Python y PostgreSQL
RUN sudo apt-get install -y python-setuptools
RUN sudo apt-get -y install python-dev
RUN sudo apt-get -y install build-essential
RUN sudo apt-get -y install python-psycopg2
RUN sudo apt-get -y install libpq-dev
RUN sudo easy_install pip
RUN sudo pip install --upgrade pip

#Instalar la app
RUN cd Proyecto-IV && make install
```

Ahora, en la web de Docker Hub, creamos un "Automated Build" sobre el repositorio de nuestro proyecto, lo cual comenzará a crear la imagen.

En el directorio del proyecto, tenemos que crear la imagen con ``` sudo  docker build -f Dockerfile -t iv_cesar .``` 

Podemos ver que se ha creado ejecutando el comando ```sudo docker images``` :

Imagen en local: 

![ej10_1](http://i1175.photobucket.com/albums/r629/Cesar_Albusac_Jorge/ej10_2_zpsfhgygypd.png)
Como podemos ver en la imagen anterior, la imagen se ha creado correctamente.
Ahora, arrancamos la imagen con ```sudo docker run -t -i iv_cesar /bin/bash```
Una vez dentro de la imagen, comprobamos la ip que tiene con **ifconfig** para después utilizarla:
![ej10_2](http://i1175.photobucket.com/albums/r629/Cesar_Albusac_Jorge/ej10_zps7lll6oxi.png)

Y ejecutamos y vamos al navegador, a la direccion  **172.17.0.21:2222** y como podemos ver funciona correctamente:

![ej10_3](http://i1175.photobucket.com/albums/r629/Cesar_Albusac_Jorge/Captura%20de%20pantalla%20de%202015-12-10%20112715_zpsjt00fi6f.png)


Imagen en [docker](https://www.docker.com/):

Los comandos que he utilizado han sido: 
```
sudo docker build -f Dockerfile -t proyecto-iv --no-cache=true ./
```
```
sudo docker push cesar2/proyecto-iv
```

Y automáticamente, tras registrarnos en  [docker](https://www.docker.com/), dar permisos para usar nuestro repositorio
del proyecto de Github,se nos habrá creado nuestra imagen, como podemos ver en las siguientes imágenes:


![ej10_4](http://i1175.photobucket.com/albums/r629/Cesar_Albusac_Jorge/docker_1_zpsqb8ls5wf.png)
![ej10_5](http://i1175.photobucket.com/albums/r629/Cesar_Albusac_Jorge/docker_5_zpseufyxakm.png)

Puedes ver el enlace a mi imagen den docker en el siguiente [enlace](https://hub.docker.com/r/cesar2/proyecto-iv/)

