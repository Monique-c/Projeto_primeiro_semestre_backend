from operator import itemgetter

def construirRankingEleitorado(CategoriaEstado:[], TotalEleitoresPorMunicipio:[], categoria:str ,ordemDescendente:bool):
  jsonPorcentagem = {'resultado':[]}
  jsonCategoria = [] 

  for item_categoria in CategoriaEstado:
    for item_total_elt in TotalEleitoresPorMunicipio:
      if item_categoria['municipio'] == item_total_elt['municipio']:
        calculo_porcentagem = item_categoria['max_eleitores_'+categoria] *100/item_total_elt['total_eleitores_aptos']

        jsonPorcentagem['resultado'].append({
          'municipio':item_categoria['municipio'],
          'porcentagem_eleitorado_'+categoria: float("{:.2f}".format(calculo_porcentagem))
        }) 
        break

  jsonPorcentagemSorted = sorted(jsonPorcentagem['resultado'], key=itemgetter("porcentagem_eleitorado_"+categoria), reverse=ordemDescendente)
  
  for index in range(5):	
    jsonCategoria.append(jsonPorcentagemSorted[index])

  return jsonCategoria



def limitarArray(arrayInteiro):
  arrayPivot = []
  for index in range(5):	
    arrayPivot.append(arrayInteiro[index])

  return arrayPivot