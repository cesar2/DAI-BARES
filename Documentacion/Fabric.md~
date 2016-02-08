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

def install_run():
	run('sudo apt-get update')
	run('sudo apt-get install -y docker.io')
	run('sudo docker pull cesar2/dai-bares:dai-bares')
	run('sudo docker run -i -t cesar2/dai-bares:dai-bares /bin/bash')
```

Se actualizaría el sistema base, se instalaría docker, se descargaría la imagen y se arrancaría dicho contenedor. 
El comando a usar es el siguiente (el archivo fabfile se encuentra en nuestra máquina y solo sirve para indicar 
al SSH que tiene que hacer):

```
fab -H cesar@cesar-service-jskdg.cloudapp.net install_run
```
Con la opcion [-H] se le indica el host, puede usarse la opcion -p para pasarle la password sino se desea más tarde:

```
fab -p **contraseña** -H cesar2@cesar-service-jskdg.cloudapp.net install_run
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



