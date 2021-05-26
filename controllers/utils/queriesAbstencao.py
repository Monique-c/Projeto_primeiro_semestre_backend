import simplejson as json
import sys
import decimal

def buscaPorMunicipiosComColunas(cursor, municipios:[], colunas:[]):
	query = compoeSomaPorColuna(colunas, municipios)
	return buscarResultadoPara(query, cursor)

def compoeSomaPorColuna(colunas:[], municipios:[]):
	sumColumns = ', '.join(map(lambda coluna: "sum(`" + coluna + "`) as "+ coluna, colunas)) + " "

	if not municipios:
		query = "SELECT " + sumColumns +\
			"FROM `abstencao_2020` \
			WHERE NR_TURNO = '1'"

	else:
		inMunicipios = ", ".join(map(lambda municipio: "'"+municipio+"'", municipios)) + " "
		query = "SELECT `NM_MUNICIPIO` AS municipio, " +\
			sumColumns +\
			"FROM `abstencao_2020` " +\
			"WHERE `NM_MUNICIPIO` IN(" + inMunicipios + ") " +\
			"AND NR_TURNO = '1' \
			GROUP BY `NM_MUNICIPIO`"

	return query


def buscaFaixaEtáriaPorMunicipio(cursor, municipios:[]):
	if not municipios:
		query = "SELECT `DS_FAIXA_ETARIA` AS 'desc_faixa_etaria', \
						SUM(QT_APTOS) AS 'qt_aptos', \
						SUM(QT_ABSTENCAO) AS 'qt_abstencao', \
						SUM(QT_COMPARECIMENTO) AS 'qt_comparecimento' \
						FROM `abstencao_2020` " +\
						"WHERE `NR_TURNO` = '1' " +\
						"GROUP BY DS_FAIXA_ETARIA \
						ORDER BY DS_FAIXA_ETARIA ASC"

	else:
		inMunicipios = ", ".join(map(lambda municipio: "'"+municipio+"'", municipios)) + " "

		query = "SELECT `NM_MUNICIPIO` AS 'municipio', \
						`DS_FAIXA_ETARIA` AS 'desc_faixa_etaria', \
						SUM(QT_APTOS) AS 'qt_aptos', \
						SUM(QT_ABSTENCAO) AS 'qt_abstencao', \
						SUM(QT_COMPARECIMENTO) AS 'qt_comparecimento' \
						FROM `abstencao_2020` " +\
						"WHERE `NM_MUNICIPIO` IN(" + inMunicipios + ") " +\
						"AND `NR_TURNO` = '1'" +\
						"GROUP BY NM_MUNICIPIO, DS_FAIXA_ETARIA \
						ORDER BY NM_MUNICIPIO ASC"

	return buscarResultadoPara(query, cursor)

def buscaEstadoCivilPorMunicipio(cursor, municipios:[]):
	if not municipios:
		query = "SELECT `DS_ESTADO_CIVIL` AS 'desc_estado_civil', \
						SUM(QT_APTOS) AS 'qt_aptos', \
						SUM(QT_ABSTENCAO) AS 'qt_abstencao', \
						SUM(QT_COMPARECIMENTO) AS 'qt_comparecimento' \
						FROM `abstencao_2020` " +\
						"WHERE `NR_TURNO` = '1'" +\
						"GROUP BY DS_ESTADO_CIVIL \
						ORDER BY DS_ESTADO_CIVIL ASC"

	else:
		inMunicipios = ", ".join(map(lambda municipio: "'"+municipio+"'", municipios)) + " "

		query = "SELECT `NM_MUNICIPIO` AS 'municipio', \
						`DS_ESTADO_CIVIL` AS 'desc_estado_civil', \
						SUM(QT_APTOS) AS 'qt_aptos', \
						SUM(QT_ABSTENCAO) AS 'qt_abstencao', \
						SUM(QT_COMPARECIMENTO) AS 'qt_comparecimento' \
						FROM `abstencao_2020` " +\
						"WHERE `NM_MUNICIPIO` IN(" + inMunicipios + ") " +\
						"AND `NR_TURNO` = '1'" +\
						"GROUP BY NM_MUNICIPIO,DS_ESTADO_CIVIL \
						ORDER BY NM_MUNICIPIO ASC"

	return buscarResultadoPara(query, cursor)

def buscaGrauEscolaridadePorMunicipio(cursor, municipios:[]):
	if not municipios:
		query = "SELECT `DS_GRAU_ESCOLARIDADE` AS 'desc_grau_escolaridade', \
						SUM(QT_APTOS) AS 'qt_aptos', \
						SUM(QT_ABSTENCAO) AS 'qt_abstencao', \
						SUM(QT_COMPARECIMENTO) AS 'qt_comparecimento' \
						FROM `abstencao_2020` " +\
						"WHERE `NR_TURNO` = '1'" +\
						"GROUP BY DS_GRAU_ESCOLARIDADE \
						ORDER BY DS_GRAU_ESCOLARIDADE ASC"
						
	else:
		inMunicipios = ", ".join(map(lambda municipio: "'"+municipio+"'", municipios)) + " "

		query = "SELECT `NM_MUNICIPIO` AS 'municipio', \
						`DS_GRAU_ESCOLARIDADE` AS 'desc_grau_escolaridade', \
						SUM(QT_APTOS) AS 'qt_aptos', \
						SUM(QT_ABSTENCAO) AS 'qt_abstencao', \
						SUM(QT_COMPARECIMENTO) AS 'qt_comparecimento' \
						FROM `abstencao_2020` " +\
						"WHERE `NM_MUNICIPIO` IN(" + inMunicipios + ") " +\
						"AND `NR_TURNO` = '1'" +\
						"GROUP BY NM_MUNICIPIO, DS_GRAU_ESCOLARIDADE \
						ORDER BY NM_MUNICIPIO ASC"

	return buscarResultadoPara(query, cursor)

def buscaMenoresAbstencoes(cursor):
	query = "SELECT `NM_MUNICIPIO` as 'municipio', \
					(sum(`QT_ABSTENCAO`) * 100) / sum(`QT_APTOS`) as 'min_abstencao' \
					FROM abstencao_2020 \
					WHERE `SG_UF` = 'SP' \
					AND `NR_TURNO` = '1'\
					GROUP BY NM_MUNICIPIO \
					ORDER BY min_abstencao ASC"
	return buscarResultadoPara(query, cursor)

def buscaMenoresAbstencoesJovens(cursor):
	query = "SELECT `NM_MUNICIPIO` as 'municipio', \
					(sum(`QT_ABSTENCAO`) * 100) / sum(QT_APTOS) as 'abstencao_jovens' \
					FROM abstencao_2020 \
					WHERE SG_UF = 'SP' \
					AND NR_TURNO = '1' \
					AND CD_FAIXA_ETARIA IN( \
					'1600', \
					'1700', \
					'1800', \
					'1900', \
					'2000', \
					'2124', \
					'2529' \
					) \
					GROUP BY NM_MUNICIPIO \
					ORDER BY abstencao_jovens ASC"

	return buscarResultadoPara(query, cursor)

def buscaMenoresAbstencoesAdultos(cursor):
	query = "SELECT `NM_MUNICIPIO` as 'municipio', \
					(sum(`QT_ABSTENCAO`) * 100) / sum(QT_APTOS) as 'abstencao_adultos' \
					FROM abstencao_2020 \
					WHERE SG_UF = 'SP' \
					AND NR_TURNO = '1' \
					AND CD_FAIXA_ETARIA IN( \
					'3034', \
					'3539', \
					'4044', \
					'4549', \
					'5054', \
					'5559' \
					) \
					GROUP BY NM_MUNICIPIO \
					ORDER BY abstencao_adultos ASC"

	return buscarResultadoPara(query, cursor)

def buscaMenoresAbstencoesIdosos(cursor):
	query = "SELECT `NM_MUNICIPIO` as 'municipio', \
					(sum(`QT_ABSTENCAO`) * 100) / sum(QT_APTOS) as 'abstencao_idosos' \
					FROM abstencao_2020 \
					WHERE SG_UF = 'SP' \
					AND NR_TURNO = '1' \
					AND CD_FAIXA_ETARIA IN( \
					'6064', \
					'6569', \
					'7074', \
					'7579', \
					'8084', \
					'8589', \
					'9094', \
					'9599', \
					'9999' \
					) \
					GROUP BY NM_MUNICIPIO \
					ORDER BY abstencao_idosos ASC"

	return buscarResultadoPara(query, cursor)

def buscaMenoresAbstencoesAnalfabetos(cursor):
	query = "SELECT `NM_MUNICIPIO` as 'municipio', \
					(sum(`QT_ABSTENCAO`) * 100) / sum(QT_APTOS) as 'abstencao_analfabetos' \
					FROM abstencao_2020 \
					WHERE SG_UF = 'SP' \
					AND NR_TURNO = '1' \
					AND DS_GRAU_ESCOLARIDADE IN('ANALFABETO') \
					GROUP BY NM_MUNICIPIO \
					ORDER BY abstencao_analfabetos ASC"

	return buscarResultadoPara(query, cursor)

def buscaMenoresAbstencoesMedioCompleto(cursor):
	query = "SELECT `NM_MUNICIPIO` as 'municipio', \
					(sum(`QT_ABSTENCAO`) * 100) / sum(QT_APTOS) as 'abstencao_medio_completo' \
					FROM abstencao_2020 \
					WHERE SG_UF = 'SP' \
					AND NR_TURNO = '1' \
					AND DS_GRAU_ESCOLARIDADE IN('ANALFABETO') \
					GROUP BY NM_MUNICIPIO \
					ORDER BY abstencao_medio_completo ASC"

	return buscarResultadoPara(query, cursor)

def buscaMenoresAbstencoesSuperiorCompleto(cursor):
	query = "SELECT `NM_MUNICIPIO` as 'municipio', \
					(sum(`QT_ABSTENCAO`) * 100) / sum(QT_APTOS) as 'abstencao_superior_completo' \
					FROM abstencao_2020 \
					WHERE SG_UF = 'SP' \
					AND NR_TURNO = '1' \
					AND DS_GRAU_ESCOLARIDADE IN('ANALFABETO') \
					GROUP BY NM_MUNICIPIO \
					ORDER BY abstencao_superior_completo ASC"

	return buscarResultadoPara(query, cursor)

def buscaMenoresAbstencoesCasados(cursor):
	query = "SELECT `NM_MUNICIPIO` as 'municipio', \
					(sum(`QT_ABSTENCAO`) * 100) / sum(QT_APTOS) as 'abstencao_casados' \
					FROM abstencao_2020 \
					WHERE SG_UF = 'SP' \
					AND NR_TURNO = '1' \
					AND DS_ESTADO_CIVIL IN('SOLTEIRO') \
					GROUP BY NM_MUNICIPIO \
					ORDER BY abstencao_casados ASC"

	return buscarResultadoPara(query, cursor)

def buscaMenoresAbstencoesSolteiros(cursor):
	query = "SELECT `NM_MUNICIPIO` as 'municipio', \
					(sum(`QT_ABSTENCAO`) * 100) / sum(QT_APTOS) as 'abstencao_solteiros' \
					FROM abstencao_2020 \
					WHERE SG_UF = 'SP' \
					AND NR_TURNO = '1' \
					AND DS_ESTADO_CIVIL IN('CASADO') \
					GROUP BY NM_MUNICIPIO \
					ORDER BY abstencao_solteiros ASC"

	return buscarResultadoPara(query, cursor)


def buscarResultadoPara(query:str, cursor):
	cursor.execute(query)
	response = cursor.fetchall()
	return response
