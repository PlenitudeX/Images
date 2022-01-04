from custom_simple_image_download import simple_image_download as simp 
import csv
OpenFileCSV = '3coracoes-Teste.csv'
openProducts = open(OpenFileCSV, encoding='utf-8', errors='ignore')
productsCarajas = csv.reader(openProducts, delimiter= ",")
productsCarajasData = list(productsCarajas)

myDict = dict()

for row in productsCarajasData:
    myDict[row[0]] = row[7]

# fatiar a lista de produtos
#sliceDict = dict(list(myDict.items())[4960:6210])
sliceDict = dict(list(myDict.items()))

response = simp.simple_image_download

for k, v in sliceDict.items():
    print(k,v)
    response().download(v.replace("/", ' '), 2, k) # v (valor) k (chave) replace ([procura],[troca],[quantidade de imagem],[chave])

