
def parche(doc):
	parche=doc["version"]
	return parche
def disponibles(doc):
	num=len(doc["data"])
	return num
def campeones(doc):
	listacampeones=[]
	for elem in doc["data"]:
		listacampeones.append(elem)
	return listacampeones

def descripciones(campeon,doc):
	for elem in doc["data"]:
		if elem == campeon:
			descripcion=doc["data"][campeon]["blurb"]
	return descripcion

def stats(campeon,doc):
	for elem in doc["data"]:
		if elem == campeon:
			estadisticas=doc["data"][campeon]["stats"]
	return estadisticas
def busqueda(buscar,doc):
	listacampeones=[]
	for elem in doc["data"]:
		if elem.startswith(buscar):
			listacampeones.append(elem)
	return listacampeones

def roles(rol,doc):
	listacampeones=[]
	for elem in doc["data"].values():
		if rol in elem["tags"]:
			campeon={}
			campeon["nombre"]=elem["name"]
			campeon["titulo"]=elem["title"]
			listacampeones.append(campeon)
	return listacampeones