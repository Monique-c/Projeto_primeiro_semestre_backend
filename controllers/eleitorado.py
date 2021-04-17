import csv
import json

def generateList(dataset):

	newList = []
	newdata = list(dataset.items())
	items = np.array(newdata)

	for item in items:
		newList.append({"name": item[0], "value": int(item[1])})

	return newList


def getMoreData(newData):
	data = pd.read_json(newData)

	grade = data.groupby(['DS_GRAU_ESCOLARIDADE'])[
		'DS_GRAU_ESCOLARIDADE'].count().to_dict()

	extraData = {
		"escolaridade": generateList(grade),
	}

	return extraData


def testQueryCSV(request):

	json_data = request.get_json()

	queryString = "DS_ESTADO_CIVIL == 'SOLTEIRO'"
	csvString = "./dados/file2.csv"

	data = pd.read_csv(csvString, sep=";", encoding="ISO-8859-1", skiprows=0)

	data.query(queryString, inplace=True)
	newData = data.to_json(orient='records')

	allData = {
		"solteiros": getMoreData(newData)
	}

	return allData
