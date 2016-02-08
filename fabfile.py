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
