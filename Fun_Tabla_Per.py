#Funcion que recive una lista de nombres (Oxygen, Hydrogen, etc.) y regresa la informacion
#de los elementos correspondientes
#_________________________Alejandro Solorio__________________________________
def Busca_nombres(dic,Nom):
    for i in dic:
        for j in Nom:
            if (j==dic[i]['nombre'][:-1]):
                print i,dic[i]

def lines_nombres(nombreArchivo,Nombres):
    try:
        f = open(nombreArchivo,"r")
        l = f.readlines()
        dictionary={}

        for i in l:
            elemento={}
            k = i.split()
            elemento['nombre']=k[3]
            X=k[4:]
            elemento['resto']=X
            dictionary[k[1]]=elemento
        Busca(dictionary,Nombres)
    except:
          return("error")

#--------------------------------RICARDO CUAMO---------------------
def Busca_simbol(dic,sim):
    for i in dic:
        if (sim==i):
            print i,dic[i]

def lines_simbol(nombreArchivo,sim):
    try:
        f = open(nombreArchivo,"r")
        l = f.readlines()
        dictionary={}

        for i in l:
            elemento={}
            k = i.split()
            elemento['nombre']=k[3]
            X=k[4:]
            elemento['resto']=X
            dictionary[k[1]]=elemento
        Busca_simbol(dictionary,sim)
    except:
          return("error")
