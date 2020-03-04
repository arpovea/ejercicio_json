import json

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
		print("La version del parche es:",doc["version"])
	elif opcion==2:
		print("Los Campeones disponibles son: ") 
		for elem in doc["data"]:
			print (elem)
	elif opcion==3:
		campeon=str(input("Dime el nombre de un campeon:"))
		for elem in doc["data"]:
			if elem == campeon:
				descripcion=doc["data"][campeon]["blurb"]
	elif opcion==4:
		campeon=str(input("Dime el nombre de un campeon:"))
		print("Foto campeon:","http://ddragon.leagueoflegends.com/cdn/%s/img/champion/%s.png"%(doc["version"],campeon))
		for elem in doc["data"]:
			if elem == campeon:
				estadisticas=doc["data"][campeon]["stats"]
		for clave,valor in estadisticas.items():
			print(clave,"->",valor)
	elif opcion==5:
		rol=str(input("Dime un rol: "))
		for elem in doc["data"].values():
			if rol in elem["tags"]:
				print (elem["name"],elem["title"])
			
				#if rol in elemento["tags"]:
				#	print (doc["data"][elem]["name"],doc["data"][elem]["title"])