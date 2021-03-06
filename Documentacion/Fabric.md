##Fabric

Para instalar fabric:
```
$ pip install fabric
```
![fabric1](http://i1155.photobucket.com/albums/p543/cesypozo/Ejercicios%20tema%206/fabric_zpsgvssvd4x.png)

El archivo contiene:

```
from fabric.api import run, local, hosts, cd
from fabric.contrib import django

#Descarga la aplicacion del repositorio git
def descargar():
	run('sudo apt-get update')
	run('sudo apt-get install -y git')
	run('sudo git clone https://github.com/cesar2/DAI-BARES.git')

#Instalacion con las dependencias necesarias
def instalar():
	run('cd DAI-BARES && make install')

#Sincronizacion de la aplicacion
def actualizar():
	run('cd DAI-BARES && sudo git pull')

#Ejecucion de test
def test():
	run('cd DAI-BARES && make test')

#Ejecucion de la aplicacion
def ejecutar():
	run('cd DAI-BARES && make run')

#Instalacion de docker, descarga de la imagen y ejecucion
def montar_docker():
	run('sudo apt-get update')
	run('sudo apt-get install -y docker.io')
	run('sudo docker pull cesar2/bares')
	run('sudo docker run -p 8000:8000 -t -i cesar2/bares sh -c "cd DAI-BARES && make run"')
```

De manera que, en primer lugar, nos descargamos nuesta aplicación.
Después, instalamos las dependencias necesarrias.
Sincronizamos la aplicación.
Ejecutamos los test que hayan sido definidos para la aplicación.
Ejecutamos la aplicación.
Y finalmente, se actualizaría el sistema base, se instalaría docker, se descargaría la imagen y se arrancaría dicho contenedor. 
El comando a usar es el siguiente (el archivo fabfile se encuentra en nuestra máquina y solo sirve para indicar 
al SSH que tiene que hacer):

```
fab -H cesar@cesar-service-jskdg.cloudapp.net install_run
```

![fabric2](http://i1155.photobucket.com/albums/p543/cesypozo/Ejercicios%20tema%206/fabric2_zpshp1kahx9.png)
Con la opcion [-H] se le indica el host, puede usarse la opcion -p para pasarle la password sino se desea más tarde:

```
fab -p **contraseña** -H cesar2@cesar-service-jskdg.cloudapp.net install_run
```

Con estas funciones hago distintas cosas como explica el comentario que precede a cada una de ellas, una vez definido este archivo podremos llevar a cabo cualquiera de estas funciones mediante la herramienta de línea de comandos de Fabric:

```
fab -p contraseña -H cesar2@cesar-service-jskdg.cloudapp.net funcionAejecutar
```

En mi caso por ejemplo si ejecuto el siguiente comando:

```
dab -p myPassword -H cesar2@cesar-service-jskdg.cloudapp.net test
```


### Despligue Docker en Azure


Primero, usamos fabfile para realizar el despliegue del contenedor dentro de Azure:
```
fab -H cesar2@cesar-service-jskdg.cloudapp.net install_run
```

Depués ejecutamos el script **run_app.sh** el cual arranca la aplicación.
 
Por último, hay que realizar un simple NAT para que las peticiones a la máquina virtual de Azure sean respondidas por el contenedor, esto se hace de la siguiente manera:
```
sudo iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j DNAT --to-destination 172.17.0.1:8000
```



