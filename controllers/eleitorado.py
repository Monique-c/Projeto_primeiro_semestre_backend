from flask import jsonify
import pymysql.cursors
import simplejson as json
import sys
import controllers.utils.queriesEleitorado as function
from controllers.utils.calcularPorcentagem import construirRankingEleitorado

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

			retornoBancoFaixaEtaria = function.buscaFaixaEtáriaPorMunicipio(cursor, municipios)
			retornoBancoEstadoCivil = function.buscaEstadoCivilPorMunicipio(cursor, municipios)
			retornoBancoGrauEscolaridade = function.buscaGrauEscolaridadePorMunicipio(cursor, municipios)

			TotalEleitoresPorMunicipio = function.buscaTotalEleitoresPorMunicipio(cursor)
			JovensPorMunicipio = function.buscaJovensPorMunicipio(cursor)

			for x in range(len(retornoBancoEleitorado)):
				retornoBancoEleitorado[x]['faixa_etaria'] = []
				retornoBancoEleitorado[x]['estado_civil'] = []
				retornoBancoEleitorado[x]['grau_escolaridade'] = []

			for idx in range(len(retornoBancoEleitorado)):
				if not municipios:
					for idades_perfil in retornoBancoFaixaEtaria:
						retornoBancoEleitorado[idx]['faixa_etaria'].append(idades_perfil)
					
					for estado_civil in retornoBancoEstadoCivil:
						retornoBancoEleitorado[idx]['estado_civil'].append(estado_civil)
					
					for grau_escolaridade in retornoBancoGrauEscolaridade:
						retornoBancoEleitorado[idx]['grau_escolaridade'].append(grau_escolaridade)
				
				else:
					for idades_perfil in retornoBancoFaixaEtaria:
						if idades_perfil['municipio'] == retornoBancoEleitorado[idx]['municipio']:
							retornoBancoEleitorado[idx]['faixa_etaria'].append(idades_perfil)
					
					for estado_civil in retornoBancoEstadoCivil:
						if estado_civil['municipio'] == retornoBancoEleitorado[idx]['municipio']:
							retornoBancoEleitorado[idx]['estado_civil'].append(estado_civil)
					
					for grau_escolaridade in retornoBancoGrauEscolaridade:
						if grau_escolaridade['municipio'] == retornoBancoEleitorado[idx]['municipio']:
							retornoBancoEleitorado[idx]['grau_escolaridade'].append(grau_escolaridade)


			JsonOrganizado = {
				"eleitorado":retornoBancoEleitorado,
				"max_eleitorado_jovens": construirRankingEleitorado(JovensPorMunicipio, TotalEleitoresPorMunicipio, True),
				"min_eleitorado_jovens": construirRankingEleitorado(JovensPorMunicipio, TotalEleitoresPorMunicipio, False)
			}
			
	return json.dumps(JsonOrganizado)


def eleitoradoQuery(request):
	return connectDb(request)
