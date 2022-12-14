from pprint import pprint
# importar as bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from pprint import pprint

import funcoes


def bfsOfGraph(numero_Vertice, dic_Adj):
  
	bfs_traversal = []
	vis = [False]*numero_Vertice
	for i in range(numero_Vertice):

		# To check if already visited
		if (vis[i] == False):
			q = []
			vis[i] = True
			q.append(i)

			# BFS starting from ith node
			while (len(q) > 0):
				g_node = q.pop(0)

				bfs_traversal.append(g_node)
				for it in dic_Adj[g_node]:
					if (vis[it] == False):
						vis[it] = True
						q.append(it)

	return bfs_traversal


######################################################################################################################################################################################################
#################################################################################################################################################################################################################
#################################################
### função usando  na main primeira 
## TransformaEmLista é uma função que recebe um array np 
###  transforma em uma lista  de 2 indice 
def TransformaNPEmLista(arrayDi):
    l=[]
    #Numero_de_linhas=46824
    
    ListaNP =list(arrayDi)
    ultimo=ListaNP[-1]                      ## 11616 29809
    ultimoIndex=ListaNP.index(ultimo)
    #print("ultimo elemento",ultimo,"p",ultimoIndex)
    Numero_de_linhas =int(ultimoIndex)+1    ##  ultimo Index = 46824 +1
    
    for i in range(1,Numero_de_linhas):
        #print(arrayDi[i])
        string = str(arrayDi[i])
        #print(string)
        lista = string.split()
        l.append(lista)
    return l



##################################################################################################################
##################################################################################################
##############################################################################################################################################################################################
    #### Criar uma tuple que armazena todos os valores de um indice  segunda 
    ### Função usando na main 

### aqui pega os elemenntos que tem o indice [i][0] igual e coloca  esse indice[i][0]  e criar uma chave
#### todos os elementos que tiveram o msm  indice [i][0] serão atribuidos a uma chave 
def retornaVerticeAdj(lista):
    
  vertice=lista[0][0] #1
  idx =0
  listaAux =[]
  dictonarioAux={}
  ultimaAresta=lista[-1][1]
  #print(ultimaAresta)
  while True:
    
    if vertice == lista[idx][0]:
      
      #print("entro no while")
      #print(lista[idx][0],":",lista[idx][1])
      listaAux.append(lista[idx][1])
    if vertice != lista[idx][0]:
      tuplaAux = tuple(listaAux)
      dictonarioAux.update({vertice: (tuplaAux)})

      #print(dictonarioAux.get('1'))

      #print(dictonarioAux.get('2'))
      #print("else",lista[idx][0],":",lista[idx][1])
    
      vertice = lista[idx][0]
      listaAux=[]
      tuplaAux=()
      idx -=1
      

    if lista[idx][1]==ultimaAresta:
      tuplaAux = tuple(listaAux)
      dictonarioAux.update({vertice: (tuplaAux)})

      #print(dictonarioAux.get('1'))

      #print(dictonarioAux.get('2'))
      #print("else",lista[idx][0],":",lista[idx][1])
    
      vertice = lista[idx][0]
      listaAux=[]
      tuplaAux=()
      idx -=1
      break
    
    idx += 1 

 
    
    
  return dictonarioAux

 ###  é a lista so que oposto por exemplo se a lista 1 tem [1,22] a  lista 2 sera [22,1]
def primeiroUltimo_UltimoPrimeiro(ListaNP):
  listaAux=[]
  i = 0
  ultimo=ListaNP[-1]                      ## 11616 29809
  ultimoIndex=ListaNP.index(ultimo)
  #print(ultimoIndex)
  Numero_de_linhas =int(ultimoIndex)+1    ##  ultimo Index = 46824 +1
  #print(ListaNP[0])
  #print(ListaNP[-1])
  while i < Numero_de_linhas:
    #print(ListaNP[i][0],ListaNP[i][1])
    listaAux.append(ListaNP[i][1])
    listaAux.append(ListaNP[i][0])
    i += 1
  ListaInverso = listaAux
  return dividirListaInversa(ListaInverso)


def dividirListaInversa(lpu):
  listaParaDic=[]
  ue_lpu=lpu[-1]              #ultimo elemento de lpu
  iue_lpu=lpu.index(ue_lpu)    ## index do ultimo elememnto lpu
  #print(lpu[iue_lpu])
  indice =1
  ## tamanho 93643 93644 93645
  tamanho = len(lpu)
 # while indice != len(lpu):
  #  print(indice)
   # indice += 1
  #for indice in range (len(lpu)):
  for indice in range (0,len(lpu),2):
    juntando =''
    if indice % 2 ==0:
      idxPar=str(lpu[indice])
      #print(idxPar)
      #indice =+1
      indice +=1

      if indice % 2 != 0:
        
        
        idxImpar=str(lpu[indice])
        juntando = idxPar+' '+idxImpar
        stringCortadas = juntando.split()
        listaParaDic.append(stringCortadas)
  
  return listaParaDic




### demoras msms
def ordenarLista(olpcnd):
  lop=[]
  j=1
  for j in range (len(olpcnd)):
    for i in range (len(olpcnd)):
      if olpcnd[j][0] == olpcnd[i][0]:
        lop.append(olpcnd[i])        
  return lop



#  QuaisVerticeEstaoRepetidos?
### função que recebe o dic1:
######(que tem a chave que representa quais vertice estão conectados
##### e o valeus que repsenta quais vertice estão conectados

###### dic2 q(que tem a chave que repsenta quais vertice  e o values que 
#### repsenta quais vertice estão conectados )

def qver(d1,d2):

  
  chavesDic1 = tuple(d1.keys())
  chavesDic2 = tuple(d2.keys())
  verticeIguais=[]

  for i in range (len(chavesDic1)):
    for  j in range (len(chavesDic2)):
      if chavesDic1[i] in chavesDic2[j]:
        verticeIguais.append(chavesDic2[j])

  return verticeIguais
def elementosNaListaRepetidos(dados):
    
  valores = []
  repetidos = set() ## para coloca o elemento reptidos so uma vez 

  for dado in dados:
      if dado not in valores: 
        valores.append(dado)
      else:
        repetidos.add(dado)
  return valores

def numeroDeVertice(dic1,dic2):
  lista1Dic1 = dic1
  lista2Dic2 = dic2
  todosVertice =[y for x in [lista1Dic1,lista2Dic2] for y in x]
  qtdVertice =(elementosNaListaRepetidos(todosVertice))
  todosVerticeSemRepeticao =qtdVertice
  
 
  qtdVertice = list(qtdVertice)
  
  quantidadeDeVertice = len(qtdVertice)
  return quantidadeDeVertice


def todosOsVerticeSemRepeticao(dic1,dic2):
  lista1Dic1 = dic1
  lista2Dic2 = dic2
  todosVertice =[y for x in [lista1Dic1,lista2Dic2] for y in x]
  qtdVertice =(elementosNaListaRepetidos(todosVertice))
  todosVerticeSemRepeticao =qtdVertice
  
 
  qtdVertice = list(qtdVertice)
  
  quantidadeDeVertice = len(qtdVertice)
  return todosVerticeSemRepeticao

def juntandoAsDuasLista(lista1,lista1Oposta):
  lista1Dic1 = lista1
  lista2Dic2 = lista1Oposta
  listaPrincipal =[y for x in [lista1Dic1,lista2Dic2] for y in x]
  
  return listaPrincipal

def convertString_int(listaNP):
  #print(listaNP)
  #y = [['123','10'], ['456','10'], ['789','20']]
  y = listaNP
  v=[]
  l=[]
  
  
   
  for i in range(len(y)):
    
    l.append(int(y[i][0]))
    l.append(int(y[i][1]))
    v.append(l)
    l=[]
  
  return v

def criandoDicionarioAdj(li):
  dicio_Adj={}
  auxList=[]
  verticeAtual=li[0][0]
  tamanho=len(li)
  i=0
  while i != tamanho:
  #for i in range(len(li)):
    if verticeAtual==li[i][0]:
      auxList.append(li[i][1])
      
    else:
      tuplaAux=tuple(auxList)
      dicio_Adj.update({verticeAtual:tuplaAux})
      auxList=[]
      verticeAtual=li[i][0]
      i -=1
    
    i+=1
  return dicio_Adj


def remove_repetidos(lista):
    l = []
    laux=list(lista)
    lista=laux
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l

def calcular_Grau(lista_Ordenada):
  grau_cada_Vertice={}
  for i in range(len(lista_Ordenada)):
    verticeAux= int(lista_Ordenada[i][0])
   
   
    #grau1=len(lista_Ordenada[i][1])
    
    g=list(lista_Ordenada[i][1])
    g1=remove_repetidos(g)
    grau=len(g1)
    
    grau_cada_Vertice.update({verticeAux: (grau)})
    
  return grau_cada_Vertice



def criarDicioAdj(lista_Ordenado):
  dicionario_Adjacente={}

  for i in range(len(lista_Ordenado)):
    verticeAux= int(lista_Ordenado[i][0])
    tuplaAux = tuple(lista_Ordenado[i][1])
    dicionario_Adjacente.update({verticeAux: (tuplaAux)})
    
  return dicionario_Adjacente