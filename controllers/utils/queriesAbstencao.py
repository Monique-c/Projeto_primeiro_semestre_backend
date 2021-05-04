import simplejson as json
import sys
import decimal

def buscaPorMunicipiosComColunas(cursor, municipios:[], colunas:[]):
	query = compoeSomaPorColuna(colunas, municipios)
	return buscarResultadoPara(query, cursor)

def compoeSomaPorColuna(colunas:[], municipios:[]):
	sumColumns = ', '.join(map(lambda coluna: "sum(`" + coluna + "`) as "+ coluna, colunas)) + " "
	inMunicipios = ", ".join(map(lambda municipio: "'"+municipio+"'", municipios)) + " "

	query = "SELECT `NM_MUNICIPIO` AS municipio, " +\
		sumColumns +\
		"FROM `abstencao_2020` " +\
		"WHERE `NM_MUNICIPIO` IN(" + inMunicipios + ") " +\
		"GROUP BY `NM_MUNICIPIO`"

	return query

def buscaFaixaEtáriaPorMunicipio(cursor, municipios:[]):
	inMunicipios = ", ".join(map(lambda municipio: "'"+municipio+"'", municipios)) + " "

	query = "SELECT `NM_MUNICIPIO` AS 'municipio', \
					`CD_FAIXA_ETARIA` AS 'cd_faixa_etaria', `DS_FAIXA_ETARIA` AS 'desc_faixa_etaria', \
					SUM(QT_APTOS) AS 'soma_abstencao' \
					FROM `abstencao_2020` " +\
					"WHERE `NM_MUNICIPIO` IN(" + inMunicipios + ") " +\
					"GROUP BY NM_MUNICIPIO, CD_FAIXA_ETARIA, DS_FAIXA_ETARIA \
					ORDER BY NM_MUNICIPIO ASC"

	return buscarResultadoPara(query, cursor)

def buscarResultadoPara(query:str, cursor):
	cursor.execute(query)
	response = cursor.fetchall()
	return response
