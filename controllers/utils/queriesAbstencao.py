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
		"FROM `abstencao_2020` " +\
		"WHERE `NM_MUNICIPIO` IN(" + inMunicipios + ") " +\
		"AND `NR_TURNO` = '1'" +\
		"GROUP BY `NM_MUNICIPIO` "

	return query

def buscaFaixaEtáriaPorMunicipio(cursor, municipios:[]):
	inMunicipios = ", ".join(map(lambda municipio: "'"+municipio+"'", municipios)) + " "
	query = "SELECT `CD_FAIXA_ETARIA`, `DS_FAIXA_ETARIA`, SUM(`QT_ABSTENCAO`) as 'quant_abstencao_faixa_etaria' \
					FROM `abstencao_2020` " +\
					"WHERE `NM_MUNICIPIO` IN(" + inMunicipios + ") " +\
					"GROUP BY `CD_FAIXA_ETARIA`, `DS_FAIXA_ETARIA` \
					ORDER BY `CD_FAIXA_ETARIA` DESC"

	return buscarResultadoPara(query, cursor)

def buscarResultadoPara(query:str, cursor):
	cursor.execute(query)
	response = cursor.fetchall()
	print("=" * 20)
	print(response)
	print("=" * 20)
	return response
