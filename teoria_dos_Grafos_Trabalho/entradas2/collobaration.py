import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from pprint import pprint
from pprint import pprint

from  funcoes import*
# estilo notebook
sns.set()
# url dos datasets
#url_path = 'https://raw.githubusercontent.com/reidnersousa/6semestre/Teoria-Grafos/GrafoExemplo.txt'
url_path = "https://raw.githubusercontent.com/reidnersousa/6semestre/Teoria-Grafos/collaboration_graph.txt"
# df recebe o arquivo e transforma em DataFrame
df = pd.read_csv(url_path , sep ='\t',names=["Teste1"])

csv_in_numpy = df['Teste1'].to_numpy()

lista1=TransformaNPEmLista(csv_in_numpy)  ## ok 

lista2=primeiroUltimo_UltimoPrimeiro(lista1)

dic1=retornaVerticeAdj(lista1)
dic2=retornaVerticeAdj(lista2)
print()
qVertice = numeroDeVertice(dic1,dic2)


###
url_path1 = 'https://raw.githubusercontent.com/reidnersousa/6semestre/Teoria-Grafos/collaboration_graph_entrada_ida_volta.txt'

# df recebe o arquivo e transforma em DataFrame
df1 = pd.read_csv(url_path1 , sep ='\t',names=["Teste1"])

csv_in_numpy1 = df1['Teste1'].to_numpy()
#print(arrayDi)


lista3=TransformaNPEmLista(csv_in_numpy1)  ## ok 


lista3_inteiros=convertString_int(lista3)
#print(lista1_inteiros)
lista3_inteiros.sort()

#print(lista3_inteiros)

d_Adj=criandoDicionarioAdj(lista3_inteiros)

dicio_Ordenado = sorted(d_Adj.items(),key=lambda t:t[0])


grau_Vertice=calcular_Grau(dicio_Ordenado)


quantidade_Aresta=len(lista1)
print("quantida de aresta ",quantidade_Aresta)

qVertice = numeroDeVertice(dic1,dic2)
print("Quantidade de vertice ",qVertice)

grau_Vertice=calcular_Grau(dicio_Ordenado)
print(grau_Vertice)


with open ('grafos_collaboration_saida.txt','w') as arquivo:
  #for valor in qVertice:
  arquivo.write("n(quantidade de Vertice) ="+str(qVertice)+'\n')
  arquivo.write("m(quantidade de Aresta)  ="+str(quantidade_Aresta)+'\n')
  for i in grau_Vertice:
    arquivo.write(str(i)+' '+str(grau_Vertice.get(i))+'\n')


opaaa= len(lista3_inteiros)
lll=bfsOfGraph(opaaa,lista3_inteiros)

