#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ejemeplo.settings')
import django
django.setup()


from rango.models import Bar, Tapa


def populate():

	buho_bar = add_bar2('Bar del búho', 'Calle Doctor Pareja Yébenes 10')
	
	add_tapa(bar=buho_bar,name2="Carne",votos=1, url="http://i1155.photobucket.com/albums/p543/cesypozo/tapas/70cf9ac0-0360-413c-a562-ba5f56871765_zpsznocwbho.jpg")
	add_tapa(bar=buho_bar,name2="Hamburguesa",votos=5, url="http://i1155.photobucket.com/albums/p543/cesypozo/tapas/20151213_161105_zpspzataukb.jpg")
	add_tapa(bar=buho_bar,name2="Sushi",votos=8, url="http://i1155.photobucket.com/albums/p543/cesypozo/tapas/20160206_150655_zpsmam17l53.jpg")
		
	charlotte_bar = add_bar2('Bar Charlotte', 'Calle Pedro Antonio De Alarcón , Granada')
	
	add_tapa(bar=charlotte_bar,name2="Rejos",votos=9, url="http://i1155.photobucket.com/albums/p543/cesypozo/tapas/IMG-20160104-WA0023_zpss7t5wx3o.jpg")
	add_tapa(bar=charlotte_bar,name2="Cheedar",votos=120, url="http://i1155.photobucket.com/albums/p543/cesypozo/tapas/20151213_154739_zpsz5zc3jo0.jpg")
	add_tapa(bar=charlotte_bar,name2="Almejas",votos=33, url="http://i1155.photobucket.com/albums/p543/cesypozo/tapas/20151007_221038_zpsr4vv7nfa.jpg")
		
	peruano_bar = add_bar2("Peruano", 'Calle Severo Ochoa , Granada ')

	add_tapa(bar=peruano_bar,name2="Pollo",votos=450, url="http://i1155.photobucket.com/albums/p543/cesypozo/tapas/20151213_153956_zpsomww2aah.jpg")
	add_tapa(bar=peruano_bar,name2="Careta",votos=2, url="http://i1155.photobucket.com/albums/p543/cesypozo/tapas/20150729_200654_zps00wzxrsq.jpg")
	add_tapa(bar=peruano_bar,name2="Serranito", votos=28, url="http://i1155.photobucket.com/albums/p543/cesypozo/tapas/IMG-20160108-WA0047_zpswouhn3to.jpeg")

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
