def lines(nombreArchivo,Nombres):
  try:
    f = open(nombreArchivo,"r")
    l = f.readlines()
    for i in l:
        for j in Nombres:
            k = i.split()
            if (k[3][:-1]==j):
                print i
  except:
   return("error")
