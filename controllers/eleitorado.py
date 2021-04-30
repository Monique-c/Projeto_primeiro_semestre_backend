from flask import jsonify
import controllers.utils.queriesEleitorado as function
import pymysql.cursors
import simplejson as json
import sys

def connectDb(request):
	json_data = request.get_json()
	municipios = json_data["municipios"]
	colunas = json_data["colunas"]

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
			retornoBancoEleitorado = function.buscaPorMunicipiosComColunas(cursor, municipios, colunas)
			# retornoBancoFaixaEtaria = function.buscaFaixaEtáriaPorMunicipio(cursor, municipios)

	# return json.dumps(retornoBancoFaixaEtaria, retornoBancoFaixaEtaria)
	return json.dumps(retornoBancoEleitorado)

def eleitoradoQuery(request):
	return connectDb(request)
