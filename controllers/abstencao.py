from flask import jsonify
import pymysql.cursors
import simplejson as json
import sys
import controllers.utils.queriesAbstencao as function
from controllers.utils.services.calcularPorcentagem import limitarArray

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

			MenoresAbstencoes = function.buscaMenoresAbstencoes(cursor)
			MaioresAbstencoes = list(reversed(MenoresAbstencoes))

			MenoresAbstencoesJovens = function.buscaMenoresAbstencoesJovens(cursor)
			MaioresAbstencoesJovens = list(reversed(MenoresAbstencoesJovens))
			MenoresAbstencoesAdultos = function.buscaMenoresAbstencoesAdultos(cursor)
			MaioresAbstencoesAdultos = list(reversed(MenoresAbstencoesAdultos))
			MenoresAbstencoesIdosos = function.buscaMenoresAbstencoesIdosos(cursor)
			MaioresAbstencoesIdosos = list(reversed(MenoresAbstencoesIdosos))

			MenoresAbstencoesAnalfabetos = function.buscaMenoresAbstencoesAnalfabetos(cursor)
			MaioresAbstencoesAnalfabetos = list(reversed(MenoresAbstencoesAnalfabetos))
			MenoresAbstencoesMedioCompleto = function.buscaMenoresAbstencoesMedioCompleto(cursor)
			MaioresAbstencoesMedioCompleto = list(reversed(MenoresAbstencoesMedioCompleto))
			MenoresAbstencoesSuperiorCompleto = function.buscaMenoresAbstencoesSuperiorCompleto(cursor)
			MaioresAbstencoesSuperiorCompleto = list(reversed(MenoresAbstencoesSuperiorCompleto))

			MenoresAbstencoesCasados = function.buscaMenoresAbstencoesCasados(cursor)
			MaioresAbstencoesCasados = list(reversed(MenoresAbstencoesCasados))
			MenoresAbstencoesSolteiros = function.buscaMenoresAbstencoesSolteiros(cursor)
			MaioresAbstencoesSolteiros = list(reversed(MenoresAbstencoesSolteiros))

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

			JsonOrganizado = {
				"comparecimento_abstencao":retornoBancoAbstencao,
				"maiores_abstencoes":limitarArray(MaioresAbstencoes),
				"menores_abstencoes":limitarArray(MenoresAbstencoes),

				"min_abstencoes_jovens":limitarArray(MenoresAbstencoesJovens),
				"max_abstencoes_jovens":limitarArray(MaioresAbstencoesJovens),
				"min_abstencoes_adultos":limitarArray(MenoresAbstencoesAdultos),
				"max_abstencoes_adultos":limitarArray(MaioresAbstencoesAdultos),
				"min_abstencoes_idosos":limitarArray(MenoresAbstencoesIdosos),
				"max_abstencoes_idosos":limitarArray(MaioresAbstencoesIdosos),

				"min_abstencoes_analfabeto":limitarArray(MenoresAbstencoesAnalfabetos),
				"max_abstencoes_analfabeto":limitarArray(MaioresAbstencoesAnalfabetos),
				"min_abstencoes_medio_completo":limitarArray(MenoresAbstencoesMedioCompleto),
				"max_abstencoes_medio_completo":limitarArray(MaioresAbstencoesMedioCompleto),
				"min_abstencoes_superior_completo":limitarArray(MenoresAbstencoesSuperiorCompleto),
				"max_abstencoes_superior_completo":limitarArray(MaioresAbstencoesSuperiorCompleto),

				"min_abstencoes_casados":limitarArray(MenoresAbstencoesCasados),
				"max_abstencoes_casados":limitarArray(MaioresAbstencoesCasados),
				"min_abstencoes_solteiros":limitarArray(MenoresAbstencoesSolteiros),
				"max_abstencoes_solteiros":limitarArray(MaioresAbstencoesSolteiros)
			}

	return json.dumps(JsonOrganizado)

def abstencaoQuery(request):
	return connectDb(request)
