def Busca(dic,Nom):
    for i in dic:
        for j in Nom:
            if (j==dic[i]['nombre'][:-1]):
                print i,dic[i]

def lines(nombreArchivo,Nombres):
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
