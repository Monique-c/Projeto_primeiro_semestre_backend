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


@app.route("/consultas", methods=['GET', 'POST'])
@cross_origin()
def testQueryCSV():
	return controllers.eleitorado.testQueryCSV(request)

@app.route("/pesquisas-abstencao", methods=['GET', 'POST'])
@cross_origin()
def abstencaoQuery():
	return controllers.abstencao.abstencaoQuery(request)

@app.route("/testDB", methods=['GET', 'POST'])
@cross_origin()
def connectDb():
	return controllers.abstencao.connectDb(request)

if __name__ == '__main__':
	app.run(debug=True)