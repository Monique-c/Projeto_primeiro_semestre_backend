from flask import jsonify
import controllers.utils.queriesAbstencao as function
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
			retornoBancoAbstencao =	function.buscaPorMunicipiosComColunas(cursor, municipios, colunas)
			retornoBancoFaixaEtaria = function.buscaFaixaEtáriaPorMunicipio(cursor, municipios)

			for x in range(len(municipios)):
				retornoBancoAbstencao[x]['faixa_etaria'] = []

			for idx in range(len(municipios)):
				for idades_perfil in retornoBancoAbstencao:
					if idades_perfil['municipio'] == municipios[idx]:
						retornoBancoAbstencao[idx]['faixa_etaria'].append(idades_perfil)

	return json.dumps(retornoBancoAbstencao)

def abstencaoQuery(request):
	return connectDb(request)
