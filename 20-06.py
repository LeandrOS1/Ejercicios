lista = [1,2,3,'hola']

def funcion(lista):
    while True:
        for i in lista:
            yield i



di = {"v1":2, "v2":3, "v3":4, "v4":5, "v5":6}
di2 = {"v1":5, "v2":6, "v3":7, "v4":8, "v5":9}
di3 = {"v1":5, "v2":6, "v3":7, "v4":8, "v5":9}

def UwU(x):
    dicc={}
    a = 0
    b = 1
    c = 0
    for i in x.values():
        a = a + i
        b = b * i
    c = a / len(x)

    dicc['suma']=a
    dicc['mult']=b
    dicc['prom']=c

    return dicc
UwU(x)

def standardDeviation(d1,d2,d3):
    sD = {}
    lista1 = list(d1.values())
    lista2 = list(d2.values())
    lista3 = list(d3.values())
    if len(d1) != len(d2):
        return "Fuck you.exe"
    a = 0
    for i in range(len(lista1)):
        a = a + ((lista1[i] + lista2[i]+lista3[i])**2)
    b = a/len(lista1) 
    sD["OwO"]=b
    return sD