import simplejson as json
import sys
import decimal

def buscaIdososPorMunicipio(cursor):
	query = "SELECT \
					`NM_MUNICIPIO` as 'municipio', \
					SUM(`QT_ELEITORES_PERFIL`) AS 'max_eleitores_idosos' \
					FROM eleitorado_ATUAL \
					WHERE `DS_FAIXA_ETARIA` IN( \
						'60 a 64 anos                  ', \
						'65 a 69 anos                  ',  \
						'70 a 74 anos                  ',  \
						'75 a 79 anos                  ',  \
						'80 a 84 anos                  ', \
						'85 a 89 anos                  ', \
						'90 a 94 anos                  ', \
						'95 a 99 anos                  ', \
						'100 anos ou mais              ' \
					) \
					GROUP BY NM_MUNICIPIO \
					ORDER BY max_eleitores_idosos DESC"

	return buscarResultadoPara(query, cursor)

def buscaJovensPorMunicipio(cursor):
	query = "SELECT \
					`NM_MUNICIPIO` as 'municipio', \
					SUM(`QT_ELEITORES_PERFIL`) AS 'max_eleitores_jovens' \
					FROM eleitorado_ATUAL \
					WHERE `DS_FAIXA_ETARIA` IN( \
						'16 anos                       ', \
						'17 anos                       ',  \
						'18 anos                       ',  \
						'19 anos                       ', \
						'20 anos                       ',  \
						'21 a 24 anos                  ', \
						'25 a 29 anos                  ' \
					) \
					GROUP BY NM_MUNICIPIO \
					ORDER BY max_eleitores_jovens DESC"

	return buscarResultadoPara(query, cursor)

def buscaTotalEleitoresPorMunicipio(cursor):
	query = "SELECT \
					`NM_MUNICIPIO` as 'municipio', \
					SUM(`QT_ELEITORES_PERFIL`) AS 'total_eleitores_aptos' \
					FROM eleitorado_ATUAL \
					GROUP BY NM_MUNICIPIO \
					ORDER BY SUM(QT_ELEITORES_PERFIL) desc"

	return buscarResultadoPara(query, cursor)

def buscaFaixaEtáriaPorMunicipio(cursor, municipios:[]):
	if not municipios:
		query = "SELECT `DS_FAIXA_ETARIA` AS 'desc_faixa_etaria', \
					 	SUM(QT_ELEITORES_PERFIL) AS 'soma_eleitores_perfil' \
						FROM `eleitorado_ATUAL` " +\
						"GROUP BY `DS_FAIXA_ETARIA` \
						ORDER BY `DS_FAIXA_ETARIA` ASC"

	else:
		inMunicipios = ", ".join(map(lambda municipio: "'"+municipio+"'", municipios)) + " "

		query = "SELECT `NM_MUNICIPIO` AS 'municipio', \
						`DS_FAIXA_ETARIA` AS 'desc_faixa_etaria', \
						SUM(QT_ELEITORES_PERFIL) AS 'soma_eleitores_perfil' \
						FROM `eleitorado_ATUAL` " +\
						"WHERE `NM_MUNICIPIO` IN(" + inMunicipios + ") " +\
						"GROUP BY NM_MUNICIPIO, DS_FAIXA_ETARIA \
						ORDER BY NM_MUNICIPIO ASC"

	return buscarResultadoPara(query, cursor)


def buscaEstadoCivilPorMunicipio(cursor, municipios:[]):
	if not municipios:
		query = "SELECT `DS_ESTADO_CIVIL` AS 'desc_estado_civil', \
						SUM(QT_ELEITORES_PERFIL) AS 'soma_eleitores_perfil' \
						FROM `eleitorado_ATUAL` " +\
						"GROUP BY DS_ESTADO_CIVIL \
						ORDER BY DS_ESTADO_CIVIL ASC"

	else:
		inMunicipios = ", ".join(map(lambda municipio: "'"+municipio+"'", municipios)) + " "

		query = "SELECT `NM_MUNICIPIO` AS 'municipio', \
						`DS_ESTADO_CIVIL` AS 'desc_estado_civil', \
						SUM(QT_ELEITORES_PERFIL) AS 'soma_eleitores_perfil' \
						FROM `eleitorado_ATUAL` " +\
						"WHERE `NM_MUNICIPIO` IN(" + inMunicipios + ") " +\
						"GROUP BY NM_MUNICIPIO, DS_ESTADO_CIVIL \
						ORDER BY NM_MUNICIPIO ASC"

	return buscarResultadoPara(query, cursor)


def buscaGrauEscolaridadePorMunicipio(cursor, municipios:[]):
	if not municipios:
		query = "SELECT `DS_GRAU_ESCOLARIDADE` AS 'desc_grau_escolaridade', \
						SUM(QT_ELEITORES_PERFIL) AS 'soma_eleitores_perfil' \
						FROM `eleitorado_ATUAL` " +\
						"GROUP BY DS_GRAU_ESCOLARIDADE \
						ORDER BY DS_GRAU_ESCOLARIDADE ASC"

	else:
		inMunicipios = ", ".join(map(lambda municipio: "'"+municipio+"'", municipios)) + " "

		query = "SELECT `NM_MUNICIPIO` AS 'municipio', \
						`DS_GRAU_ESCOLARIDADE` AS 'desc_grau_escolaridade', \
						SUM(QT_ELEITORES_PERFIL) AS 'soma_eleitores_perfil' \
						FROM `eleitorado_ATUAL` " +\
						"WHERE `NM_MUNICIPIO` IN(" + inMunicipios + ") " +\
						"GROUP BY NM_MUNICIPIO, DS_GRAU_ESCOLARIDADE \
						ORDER BY NM_MUNICIPIO ASC"

	return buscarResultadoPara(query, cursor)


def buscaPorMunicipiosComColunas(cursor, municipios:[], colunas:[]):
	query = compoeSomaPorColuna(colunas, municipios)
	return buscarResultadoPara(query, cursor)

def compoeSomaPorColuna(colunas:[], municipios:[]):
	if not municipios:
		sumColumns = ', '.join(map(lambda coluna: "sum(`" + coluna + "`) as "+ coluna, colunas)) + " "

		query = "SELECT " + sumColumns +\
			"FROM `eleitorado_ATUAL` "

	else:
		sumColumns = ', '.join(map(lambda coluna: "sum(`" + coluna + "`) as "+ coluna, colunas)) + " "
		inMunicipios = ", ".join(map(lambda municipio: "'"+municipio+"'", municipios)) + " "

		query = "SELECT `NM_MUNICIPIO` AS municipio, " +\
			sumColumns +\
			"FROM `eleitorado_ATUAL` " +\
			"WHERE `NM_MUNICIPIO` IN(" + inMunicipios + ") " +\
			"GROUP BY `NM_MUNICIPIO`"

	return query



def buscarResultadoPara(query:str, cursor):
	cursor.execute(query)
	response = cursor.fetchall()
	return response