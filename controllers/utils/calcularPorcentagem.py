from operator import itemgetter

def construirRankingEleitorado(JovensEstado:[], TotalEleitoresPorMunicipio:[], ordemDescendente:bool):
  jsonPorcentagem = {'resultado':[]}
  jsonJovens = [] 

  for item_jovens in JovensEstado:
    for item_total in TotalEleitoresPorMunicipio:
      if item_jovens['municipio'] == item_total['municipio']:
        calculo_porcentagem = item_jovens['max_eleitores_jovens'] *100/item_total['total_eleitores_aptos']

        jsonPorcentagem['resultado'].append({
          'municipio':item_jovens['municipio'],
          'porcentagem_eleitorado_jovens': float("{:.2f}".format(calculo_porcentagem))
        }) 
        break

  jsonPorcentagemSorted = sorted(jsonPorcentagem['resultado'], key=itemgetter('porcentagem_eleitorado_jovens'), reverse=ordemDescendente)
  
  for index in range(5):	
    jsonJovens.append(jsonPorcentagemSorted[index])

  return jsonJovens