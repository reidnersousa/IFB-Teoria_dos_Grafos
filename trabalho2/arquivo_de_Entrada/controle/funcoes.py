import networkx as nx

def opcoes(o):
    #print("Digite 1 para escolha o grafo 1")
    #print("Digite 2 para escolha o grafo 2")
    #print("Digite 3 para escolha o grafo 3")
    #print("Digite 4 para escolha o grafo 4")
    #print("Digite 5 para escolha o grafo 5")
    return escolha_Arquivo(o)

def escolha_Arquivo(escolha):
    
    switcher ={
        1:"https://raw.githubusercontent.com/reidnersousa/IFB-Teoria_dos_Grafos/main/trabalho2/arquivo_de_Entrada/trab2grafo_1.txt",
        2:"https://raw.githubusercontent.com/reidnersousa/IFB-Teoria_dos_Grafos/main/trabalho2/arquivo_de_Entrada/trab2grafo_2.txt",
        3:"https://raw.githubusercontent.com/reidnersousa/IFB-Teoria_dos_Grafos/main/trabalho2/arquivo_de_Entrada/trab2grafo_3.txt",
        4:"https://raw.githubusercontent.com/reidnersousa/IFB-Teoria_dos_Grafos/main/trabalho2/arquivo_de_Entrada/trab2grafo_4.txt",
        5:"https://raw.githubusercontent.com/reidnersousa/IFB-Teoria_dos_Grafos/main/trabalho2/arquivo_de_Entrada/trab2grafo_5.txt"
    }

    return switcher.get(escolha,"escolha invalida")


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



def Criar_Vertice_Aresta(ll):
   
    E={}
    lista_Aux=[]
    lista_Aux2=[]
    for i in range(len(ll)):
        
        ll[i][2]=int(ll[i][2])
        lista_Aux.append(ll[i][0])
        lista_Aux2.append(tuple(ll[i]))
    Vertice=set(lista_Aux)
    Aresta=lista_Aux2
    return Vertice,Aresta


def dijkstra_caminho(G,V):
    print(nx.dijkstra_path(G,'1','10',weight='weight')) 
    print(nx.dijkstra_path(G,'1','100',weight='weight'))
    
 
    if len(V)>1000:
        print(nx.dijkstra_path(G,'1','1000',weight='weight')) 
        if len(V)> 10000:
            print(nx.dijkstra_path(G,'1','10000',weight='weight')) 