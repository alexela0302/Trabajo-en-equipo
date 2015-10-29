def lines(nombreArchivo,Nombres):
    try:
        f = open(nombreArchivo,"r")
        l = f.readlines()
        dictionary={}

        for i in l:
            elemento={}
            k = i.split()
            elemento['nombre']=k[3]
            X=k[3:]
            elemento['resto']=X
            dictionary[k[2]]=elemento
            print dictionary[k[2]]
        return dictionary
    except:
          return("error")
