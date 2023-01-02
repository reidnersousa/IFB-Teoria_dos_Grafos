# importar as bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import seaborn as sns
from pprint import pprint
from pprint import pprint

from  funcoes import *

### Autor Reidner ,Emerson,Ruan

## grafo 1 100  g2  1000       grafo 3   10000   grafo4 50000     grafo5  100000
## grafo 1 419  g2  337750     grafo 3   85558   grafo4 332089    grafo5  297881


###  digite qual grafo quer ler; as opçções são 1,2,3,4,5


url_path =opcoes(5) ### escolhe qual datecenter vai puxa o grafo


df = pd.read_csv(url_path , sep ='\t',names=["Grafo2"])

csv_in_numpy = df['Grafo2'].to_numpy()

Lista1=TransformaNPEmLista(csv_in_numpy)  ## ok 



# Criand o Vertice(V)  e Aresta (A)
V,A=Criar_Vertice_Aresta(Lista1)



G=nx.Graph()
### add Vertice no Grafo
G.add_nodes_from(V)
### Add Aresta no Grafo
G.add_weighted_edges_from(A)



##3 retorna aresta positivos
e_positivo=([(u, v,d) for (u, v, d) in G.edges(data=True) if float(d["weight"]) > 0.0])
### retorna aresta negativas
e_negativo=([(u, v,d) for (u, v, d) in G.edges(data=True) if float(d["weight"]) < 0.0])    

### retorna a lista do menor caminho
dijkstra_caminho(G,V)
 

