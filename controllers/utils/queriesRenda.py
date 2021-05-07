import simplejson as json
import sys
import decimal


def mediaPIB_PIB_PercaptaESTADO(cursor):
	query = "SELECT AVG(`PIB`) as 'media_PIB', AVG(`PIB_percapita`) as 'media_PIB_percapta' from renda_2020"
	return buscarResultadoPara(query, cursor)

def mediaPIB_PIB_Percapta(cursor, municipios:[],):
		inMunicipios = ", ".join(map(lambda municipio: "'"+municipio+"'", municipios)) + " "
		query = "SELECT `nome` as 'municipio', `PIB`, `PIB_percapita` FROM renda_2020 \
						WHERE nome IN (" + inMunicipios + ")"

		return buscarResultadoPara(query, cursor)


def minPIB(cursor):
	query = "SELECT `nome` as 'municipio', `PIB` as 'min_PIB' from renda_2020 \
					group by nome, PIB \
					ORDER BY PIB ASC \
					limit 5"

	return buscarResultadoPara(query, cursor)

def maxPIB(cursor):
	query = "SELECT `nome` as 'municipio', `PIB` as 'max_PIB' from renda_2020 \
					group by nome, PIB \
					ORDER BY PIB DESC \
					limit 5"

	return buscarResultadoPara(query, cursor)

def maxPIB_Percapta(cursor):
	query = "SELECT `nome` as 'municipio', `PIB_percapita` as 'max_PIB_percapita' from renda_2020 \
					group by nome, PIB_percapita \
					ORDER BY PIB_percapita DESC \
					limit 5"

	return buscarResultadoPara(query, cursor)

def minPIB_Percapta(cursor):
	query = "SELECT `nome` as 'municipio', `PIB_percapita` as 'min_PIB_percapita' from renda_2020 \
					group by nome, PIB_percapita \
					ORDER BY PIB_percapita ASC \
					limit 5"

	return buscarResultadoPara(query, cursor)



def buscarResultadoPara(query:str, cursor):
	cursor.execute(query)
	response = cursor.fetchall()
	return response