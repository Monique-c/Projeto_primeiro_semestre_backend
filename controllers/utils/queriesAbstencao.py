import simplejson as json
import sys
import decimal

def abstencaoMunicipio(cursor, data):
	query = "SELECT sum(`QT_ELEITORES_PERFIL`) FROM `eleitorado_ATUAL` \
					WHERE `NM_MUNICIPIO` = %s"

	cursor.execute(query, data)
	response = cursor.fetchone()

	return json.dumps(response)


def comparecimentoMunicipio(cursor, data):
	query ="SELECT sum(`QT_ELEITORES_INC_NM_SOCIAL`) FROM `eleitorado_ATUAL` \
					WHERE `NM_MUNICIPIO` = %s"

	cursor.execute(query, data)
	response = cursor.fetchall()

	return json.dumps(response)