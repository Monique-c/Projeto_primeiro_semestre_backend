import simplejson as json
import sys
import decimal

def buscaPorMunicipiosComColunas(cursor, municipios:[], colunas:[]):
	query = compoeSomaPorColuna(colunas, municipios)
	return buscarResultadoPara(query, cursor)

def compoeSomaPorColuna(colunas:[], municipios:[]):
	sumColumns = ', '.join(map(lambda coluna: "sum(`" + coluna + "`) as "+ coluna, colunas)) + " "
	inMunicipios = ", ".join(map(lambda municipio: "'"+municipio+"'", municipios)) + " " 
	query = "SELECT `NM_MUNICIPIO`, " +\
		sumColumns +\
		"FROM `eleitorado_ATUAL` " +\
		"WHERE `NM_MUNICIPIO` IN(" + inMunicipios + ") " +\
		"GROUP BY `NM_MUNICIPIO`"	

	return query

def buscarResultadoPara(query:str, cursor):
	cursor.execute(query)
	response = cursor.fetchall()
	return response
