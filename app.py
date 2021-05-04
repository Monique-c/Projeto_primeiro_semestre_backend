import controllers.abstencao
import controllers.eleitorado

from flask import Flask, request, jsonify, send_file
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def test():
  jsonTest = {"status": "API Online"}
  return jsonify(jsonTest)

@app.route("/pesquisas-eleitorado", methods=['GET', 'POST'])
@cross_origin()
def testQueryCSV():
	return controllers.eleitorado.eleitoradoQuery(request)

@app.route("/pesquisas-abstencao", methods=['GET', 'POST'])
@cross_origin()
def abstencaoQuery():
	return controllers.abstencao.abstencaoQuery(request)

if __name__ == '__main__':
	app.run(debug=True)
