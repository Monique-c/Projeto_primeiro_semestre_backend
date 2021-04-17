import json
import sys

def estado_civil(cursor, data):
	query ="SELECT count(*) FROM `eleitorado` \
					WHERE `DS_ESTADO_CIVIL` LIKE %s \
					AND `NM_MUNICIPIO` LIKE %s \
					GROUP BY DS_ESTADO_CIVIL" 

	cursor.execute(query, data)
	response = cursor.fetchone()

	return response

def ds_genero(cursor, data):
	query ="SELECT count(*) FROM `eleitorado` \
					WHERE `DS_ESTADO_CIVIL` LIKE %s \
					AND `NM_MUNICIPIO` LIKE %s \
					GROUP BY DS_ESTADO_CIVIL" 

	cursor.execute(query, data)
	response = cursor.fetchall()

	return response