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
			retornoBancoEstadoCivil = function.buscaEstadoCivilPorMunicipio(cursor, municipios)
			retornoBancoGrauEscolaridade = function.buscaGrauEscolaridadePorMunicipio(cursor, municipios)

			for x in range(len(retornoBancoAbstencao)):
				retornoBancoAbstencao[x]['faixa_etaria'] = []
				retornoBancoAbstencao[x]['estado_civil'] = []
				retornoBancoAbstencao[x]['grau_escolaridade'] = []

			for idx in range(len(retornoBancoAbstencao)):
				if not municipios:
					for idades_perfil in retornoBancoFaixaEtaria:
						retornoBancoAbstencao[idx]['faixa_etaria'].append(idades_perfil)

					for estado_civil in retornoBancoEstadoCivil:
						retornoBancoAbstencao[idx]['estado_civil'].append(estado_civil)

					for grau_escolaridade in retornoBancoGrauEscolaridade:
						retornoBancoAbstencao[idx]['grau_escolaridade'].append(grau_escolaridade)

				else:
					for idades_perfil in retornoBancoFaixaEtaria:
						if idades_perfil['municipio'] == retornoBancoAbstencao[idx]['municipio']:
							retornoBancoAbstencao[idx]['faixa_etaria'].append(idades_perfil)

					for estado_civil in retornoBancoEstadoCivil:
						if estado_civil['municipio'] == retornoBancoAbstencao[idx]['municipio']:
							retornoBancoAbstencao[idx]['estado_civil'].append(estado_civil)

					for grau_escolaridade in retornoBancoGrauEscolaridade:
						if grau_escolaridade['municipio'] == retornoBancoAbstencao[idx]['municipio']:
							retornoBancoAbstencao[idx]['grau_escolaridade'].append(grau_escolaridade)

	return json.dumps(retornoBancoAbstencao)

def abstencaoQuery(request):
	return connectDb(request)
