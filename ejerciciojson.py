import json
from funciones import parche
from funciones import campeones
from funciones import descripciones
from funciones import stats
from funciones import roles

with open("champion.json") as fichero:
	doc=json.load(fichero)
print (type(doc))

while True:
	print ('''
	Elige una opcion:
	1-Muestra la versión del parche y el número de campeones del que tenemos información.
	2-Muestra el nombre de todos los campeones.
	3-Pide por teclado un campeon y muestra su descripción.
	4-Pide por teclado un campeon te muestra sus estadisticas y la url de su imagen.
	5-Pide por teclado un rol(Tank, Figther,Mage,Assassin,Support,Marksman), y te muestra los campeones junto a su titulo que tengan ese rol.
	0-Para salir.
	''')
	opcion=int(input("Opcion: "))

	if opcion==1:
		print("La version del parche es:",parche(doc))
	elif opcion==2:
		print("Los Campeones disponibles son: ") 
		for elem in campeones(doc):
			print (elem)
	elif opcion==3:
		campeon=str(input("Dime el nombre de un campeon: "))
		print("Descripción: ",descripciones(campeon,doc))
	elif opcion==4:
		campeon=str(input("Dime el nombre de un campeon: "))
		print("Foto campeon:","http://ddragon.leagueoflegends.com/cdn/%s/img/champion/%s.png"%(doc["version"],campeon))
		for clave,valor in stats(campeon,doc).items():
			print(clave,"->",valor)
	elif opcion==5:
		rol=str(input("Dime un rol: "))
		for elem in roles(rol,doc):
			print (elem["nombre"],elem["titulo"])
	elif opcion==0:
		print ("¡Hasta la proxima!")
		break