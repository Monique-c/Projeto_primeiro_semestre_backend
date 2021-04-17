import json
import pymysql.cursors
import sys
from flask import jsonify

import controllers.utils.defs as function

def connectDb(request):
	json_data = request.get_json()

	data = (
		'"' + json_data["parametro_busca"] +'"',
		'"' + json_data["filtro_busca"] + '"'
	)

	estadoCivil = []
	genero = []

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
			estadoCivil.append(function.estado_civil(cursor, data))
			# genero.append(function.ds_genero(cursor, data))

	response = jsonify(estadoCivil, genero)

	return response


def abstencaoQuery(request):

	json_data = request.get_json()

	data = (
		'"' + json_data["parametro_busca"] +'"',
		'"' + json_data["filtro_busca"] + '"'
	)

	return data
