from fabric.api import run, local, hosts, cd
from fabric.contrib import django


#Descarga y arranca docker
def install_run():
	run('sudo apt-get update')
	run('sudo apt-get install -y docker.io')
	run('sudo docker pull cesar2/dai-bares:dai-bares')
	run('sudo docker run -i -t cesar2/dai-bares:dai-bares /bin/bash')

#Ejecucion de la aplicacion en modo desarrollo
def runApp():
	run('cd DAI && sudo python manage.py runserver 0.0.0.0:80')

#Actualizar la aplicacion
def actApp():
	run('cd DAI && sudo git pull')
