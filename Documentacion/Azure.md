He configurado una máquina en Azure con Vagrant y también con ansible.

En primer lugar, he actualizado la versión de vagrant, ya que con la 1.4.3 he tenido algunos problemas.
La he actualizado a la 1.8.1:

![Ej8](http://i1155.photobucket.com/albums/p543/cesypozo/Ejercicios%20tema%206/ejercicio8b_zpsutkodcmx.png)

Ahora, tenemos que instalar el provisionador de azure para vagrant.
Tenemos que ejecutar ```vagrant plugin install vagrant-azure```:

![Ej8_1](http://i1155.photobucket.com/albums/p543/cesypozo/Ejercicios%20tema%206/ej8_1_zpsidwkvlzs.png)

Podemos comprobar los box que tenemos instalados con ```vagrant box list```.
Si necesitamos eliminar alguna, lo haremos con ```vagrant box remove nombre_box```.

Iniciamos sesión en Azure, como en anteriores ocasiones, con ```azure login```. Después, tenemos que descargar
el archivo de Configuración con ```azure account download```:

![Ej8_2](http://i1155.photobucket.com/albums/p543/cesypozo/Ejercicios%20tema%206/ej8_2_zps6jnktmo5.png)

Tenemos que pinchar en la dirección que nos indica en la consola y se descargará automáticamente:

![Ej_download](http://i1155.photobucket.com/albums/p543/cesypozo/Ejercicios%20tema%206/ejercicio8b_4_zpshisryeu3.png)

Una vez que se haya descargado, lo tenemos que importar con ```azure account import nombre_del_archivo```:
![Ej8_4](http://i1155.photobucket.com/albums/p543/cesypozo/Ejercicios%20tema%206/ej8_4_zps6s9h9c7w.png)

Ahora tenemos que generar los certificados y los archivos PEM.
Ejecutamos en consola:
```
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout ~/.ssh/azurevagrant.key -out ~/.ssh/azurevagrant.key
chmod 600 ~/.ssh/azurevagrant.key
openssl x509 -inform pem -in ~/.ssh/azurevagrant.key -outform der -out ~/.ssh/azurevagrant.cer
```
![Ej8_5](http://i1155.photobucket.com/albums/p543/cesypozo/Ejercicios%20tema%206/ej8_5_zpsek1cuigl.png)

Ahora, nos vamos a nuestra página de Azure, en Configuración, Certificados de Administración, y le damos a cargar.
Añadimos el certificado que hemos creado anteriormente, **azurevagrant.cer**:
![Ej8_6](http://i1155.photobucket.com/albums/p543/cesypozo/Ejercicios%20tema%206/ejercicio8b_10_zps58cmljcw.png)


Para autenticar la maquina azure desde el Vagrantfile, necesitamos un archivo.pem. Para generarlo:

```openssl req -x509 -key ~/.ssh/id_rsa -nodes -days 365 -newkey rsa:2048 -out azurevagrant.pem```

Y ahora concatenarle el fichero.key. para que contenga la llave privada y la pública:
```cat /home/cesar/.ssh/azurevagrant.key > azurevagrant.pem ```

Ahora, tenemos que crear el archivo Vagrantfile. En mi caso tiene el siguiente contenido:
```
Vagrant.configure('2') do |config|
    config.vm.box = 'azure'
    config.vm.network "public_network"
    config.vm.network "private_network",ip: "192.168.56.10", virtualbox__intnet: "vboxnet0"
    config.vm.network "forwarded_port", guest: 80, host: 80
    config.vm.define "localhost" do |l|
            l.vm.hostname = "localhost"
    end


config.vm.provider :azure do |azure, override| 
    azure.mgmt_certificate = File.expand_path('/home/cesar/pruebaVagrant/azurevagrant.pem') 
    azure.mgmt_endpoint = 'https://management.core.windows.net'
    azure.subscription_id = '3014840c-c3a1-4794-979f-e2d0d3fbefba'
    azure.vm_image = 'b39f27a8b8c64d52b05eac6a62ebad85__Ubuntu-14_04_2-LTS-amd64-server-20150506-en-us-30GB'
    azure.vm_name = 'cesar' 
    azure.vm_password = 'Clave#Cesar#1'
    azure.vm_location = 'Central US' 
    azure.ssh_port = '22'
    azure.tcp_endpoints = '80:80'
end

config.vm.provision "ansible" do |ansible|
        ansible.sudo = true
        ansible.playbook = "bares.yml"
        ansible.verbose = "v"
        ansible.host_key_checking = false
end
end
```

Configuro todo lo relativo al aprovisionamiento mediante la herramienta ansible, indicándole el playbook que va a ejecutar.
El archivo **bares.yml** contendrá lo siguiente:
```
- hosts: localhost
  sudo: yes
  remote_user: vagrant
  tasks:
  - name: Actualizar sistema 
    apt: update_cache=yes upgrade=dist
  - name: Instalamos postgresql
    command: easy_install pip
    command: apt-get install -y python-dev libpq-dev python-psycopg2    
  - name: Instalar paquetes
    apt: name=python-setuptools state=present
    apt: name=build-essential state=present
    apt: name=python-dev state=present
    apt: name=python-pip state=present
    apt: name=git state=present
  - name: Ins Pyp
    action: apt pkg=python-pip
  - name: Obtener aplicacion git
    git: repo=https://github.com/cesar2/DAI-BARES.git  dest=appBares clone=yes force=yes
  - name: Permisos de ejecucion
    command: chmod -R +x appBares
  - name: Instalar requirements
    command: sudo pip install -r appBares/requirements.txt
  - name: Lanzar app
    command: nohup sudo python appBares/manage.py runserver 0.0.0.0:80
```


El archivo anterior se encarga de actualizar el sistema , instalar dependencia, descargar la aplicación de git, instalar los requisitos necesarios y ejecutar la aplicación.

Ahora, creamos el archivo **ansible_hosts**, con el siguiente contenido:
```
[localhost]
192.168.56.10
```

A continuación,para crear la maquina con vagrant, debemos ejecutar:

```vagrant box add azure https://github.com/msopentech/vagrant-azure/raw/master/dummy.box```

![Ej8_7](http://i1155.photobucket.com/albums/p543/cesypozo/Ejercicios%20tema%206/ej8_7_zpstpzmpdya.png)

Y después ```vagrant up --provider=azure```:

![Ej8_8](http://i1155.photobucket.com/albums/p543/cesypozo/Ejercicios%20tema%206/ej8_8_zps466ndig2.png)

![Ej8_9](http://i1155.photobucket.com/albums/p543/cesypozo/Ejercicios%20tema%206/ejercicio8b_16_zpsysckmonk.png)

Y ahora, accedemos a la dirección que nos ha generado, en mi tengo que acceder a **http://cesar-service-jskdg.cloudapp.net/rango/**:
![Ej8_10](http://i1155.photobucket.com/albums/p543/cesypozo/Ejercicios%20tema%206/ej8_10_zpsxi7zkbno.png)

El aprovisionamiento se lleva acabo también en esta ejecución, pero si queremos hacerlo después, podemos utilizar
```vagrant provision```





