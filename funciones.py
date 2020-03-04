
def parche(doc):
	parche=doc["version"]
	return parche

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