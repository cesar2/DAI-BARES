#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ejemeplo.settings')
import django
django.setup()


from rango.models import Bar, Tapa


def populate():

	buho_bar = add_bar2('Bar del búho', 'Calle Doctor Pareja Yébenes 10')
	
	add_tapa(bar=buho_bar,name2="Tortilla",votos=1, url="http://recetatortilladepatatas.net/wp-content/uploads/2014/11/ingredientes-tortilla-de-patatas.jpg")
	add_tapa(bar=buho_bar,name2="Hamburguesa",votos=5, url="http://pizzerialaestacion.com/wp-content/uploads/2014/03/big_3380c-amburguesa.jpg")
	add_tapa(bar=buho_bar,name2="Burrito",votos=8, url="http://www.lasirena.es/images/cache/files/product/platos-preparados/2781-Burrito-Mexicano-carne500x500.jpg")
		
	charlotte_bar = add_bar2('Bar Charlotte', 'Calle Pedro Antonio De Alarcón , Granada')
	
	add_tapa(bar=charlotte_bar,name2="Rejos",votos=9, url="http://farm4.static.flickr.com/3192/2757106117_d051679d4f.jpg?v=0")
	add_tapa(bar=charlotte_bar,name2="Calamares",votos=120, url="https://recetassaboresypasiones.files.wordpress.com/2014/10/calamares-a-la-romana.jpg")
	add_tapa(bar=charlotte_bar,name2="Chopitos",votos=33, url="http://chefalpaso.com/wp-content/uploads/2011/03/chopitos-Chef-al-paso.jpg")
		
	peruano_bar = add_bar2("Peruano", 'Calle Severo Ochoa , Granada ')

	add_tapa(bar=peruano_bar,name2="Pizza",votos=450, url="http://i.imgur.com/yS3TV.jpg")
	add_tapa(bar=peruano_bar,name2="Pinchito",votos=2, url="http://www.decaminoamicocina.com/wp-content/uploads/2012/07/pinchitos-morunos.jpg")
	add_tapa(bar=peruano_bar,name2="Serranito", votos=28, url="http://i.blogs.es/0c9744/serranito-20bocadillo-20del-20sur/original.jpg")

    # Print out what we have added to the user.
	for b in Bar.objects.all():
		for t in Tapa.objects.filter(bar=b):
			print "- {0} - {1}".format(str(b), str(t))
			
def add_tapa(bar, name2, votos=0, url=''):
	t = Tapa.objects.get_or_create(bar=bar, name2=name2)[0]
	t.votos=votos
	t.url = url
	t.save()
	return t

def add_bar(name):
	b = Bar.objects.get_or_create(name=name)[0]
	return b
	
def add_bar2(name, address):
	b = Bar.objects.get_or_create(name=name,address=address)[0]
	return b

# Start execution here!
if __name__ == '__main__':
	print "Starting Rango population script..."
	populate()