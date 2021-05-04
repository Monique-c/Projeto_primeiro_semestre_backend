import controllers.eleitorado
import controllers.abstencao
import controllers.renda
import controllers.graficosRelevantes

from flask import Flask, request, jsonify, send_file
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def test():
  jsonTest = {"status": "API Online"}
  return jsonify(jsonTest)

@app.route("/testDB", methods=['GET', 'POST'])
@cross_origin()
def connectDb():
	return controllers.abstencao.connectDb(request)


@app.route("/pesquisas-eleitorado", methods=['GET', 'POST'])
@cross_origin()
def eleitoradoQuery():
	return controllers.eleitorado.eleitoradoQuery(request)

@app.route("/pesquisas-abstencao", methods=['GET', 'POST'])
@cross_origin()
def abstencaoQuery():
	return controllers.abstencao.abstencaoQuery(request)

@app.route("/pesquisas-renda", methods=['GET', 'POST'])
@cross_origin()
def rendaQuery():
	return controllers.renda.rendaQuery(request)

@app.route("/pesquisas-graficos-relevantes", methods=['GET', 'POST'])
@cross_origin()
def graficosRelevantesQuery():
	return controllers.graficosRelevantes.graficosRelevantesQuery(request)

if __name__ == '__main__':
	app.run(debug=True)