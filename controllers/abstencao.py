from flask import jsonify
import controllers.utils.queriesAbstencao as function
import pymysql.cursors
import simplejson as json
import sys

def connectDb(request):
	json_data = request.get_json()

	data = (
		json_data["MN_MUNICIPIO"],
	)

	abstencao_municipio = ""
	comparecimento_municipio = ""

# Conexão com mysql
	try:
		connection = pymysql.connect(
			user="admin",
			password="admin",
			host="127.0.0.1",
			port=3306,
			database="api_dados"
		)

	except pymysql.Error as e:
		print(f"Erro de conexão ao SGBD {e}")
		sys.exit(1)

	with connection:

		with connection.cursor() as cursor:
			abstencao_municipio = function.abstencaoMunicipio(cursor, data)
			comparecimento_municipio = function.comparecimentoMunicipio(cursor, data)

	response = json.dumps({
		"eleitorado_municipio":abstencao_municipio, 
		"nome_social_municipio":comparecimento_municipio
	})

	return response


def abstencaoQuery(request):
	return connectDb(request)
