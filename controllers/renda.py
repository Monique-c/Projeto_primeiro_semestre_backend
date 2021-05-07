from flask import jsonify
import controllers.utils.queriesRenda as function
import pymysql.cursors
import simplejson as json
import sys

def connectDb(request):
	json_data = request.get_json()
	municipios = json_data["municipios"]

# Conexão com mysql
	try:
		connection = pymysql.connect(
			user="admin",
			password="admin",
			host="127.0.0.1",
			port=3306,
			database="api_dados",
			cursorclass=pymysql.cursors.DictCursor
		)

	except pymysql.Error as e:
		print(f"Erro de conexão ao SGBD {e}")
		sys.exit(1)

	with connection:
		with connection.cursor() as cursor:
			retornoBancoRendaEstado = function.mediaPIB_PIB_PercaptaESTADO(cursor)
			retornoMaxPIB = function.maxPIB(cursor)
			retornoMinPIB = function.minPIB(cursor)
			retornoMaxPIB_Percapta = function.maxPIB_Percapta(cursor)
			retornoMinPIB_Percapta = function.minPIB_Percapta(cursor)

			if not municipios:
				retornoBancoRendaMunicipio = []
			else:
				retornoBancoRendaMunicipio = function.mediaPIB_PIB_Percapta(cursor, municipios)

			jsonOrganizado = {
				"media_PIB_percapta_ESTADO": retornoBancoRendaEstado,
				"media_PIB_percapta_MUNICIPIO": retornoBancoRendaMunicipio,
				"max_PIB":retornoMaxPIB,
				"min_PIB":retornoMinPIB,
				"max_PIB_Percapta":retornoMaxPIB_Percapta,
				"min_PIB_Percapta":retornoMinPIB_Percapta
			}

	return json.dumps(jsonOrganizado)

def rendaQuery(request):
	return connectDb(request)
