from curses.ascii import CAN
from test.test_socket import CANTest
def generarPares(lim):
    num=0
    lisPar=[]
    while num<lim:
        lisPar.append(num*2)
        num=num+1
    return lisPar
print("GENERAR PARES>>>>")
print(generarPares(10))

#El Mismo ejercicio pero con YIELD()>>>>>>
#USANDO GENERADORES>>>>

def generarParesY(lim):
    num=0
    while num<lim:
        yield(num*2)
        num=num+1
devolverPar=(generarParesY(10))
print("DEVOLVER PAR>>>>>")
print(next(devolverPar))


#SIN YIELD

def Recorrer0(*l): #el * significa que creara una tupla con el parametro ingresado
    for e in l:
        for se in e:
            print("SIN YIELD Y CON 2 FOR's>>>")
            print(e)
city=(Recorrer0("Norway","Amsterdam","Ibiza"))

#USANDO YIELD

def Recorrer(*l): #el * significa que creara una tupla con el parametro ingresado
    for e in l:
        for se in e:
            yield(se)
city=(Recorrer("Norway","Amsterdam","Ibiza"))
print("Con YIELD>>>>>")
print(next(city))

#SOLO CON UN FOR

def Recorrer2(*g): #el * significa que creara una tupla con el parametro ingresado
    for e in g:
        yield from e    
city2=(Recorrer2("Norway","Amsterdam","Ibiza"))
print("Recorrer, YIELD FROM>>>>>>")
print(next(city2))

#CONTINUE>>

nombre="LINO PINTO"
can = len(nombre)
print(can)
cuenta =0
for a in nombre:
    if a==" ":
        continue
    cuenta=cuenta+1
print("CONTINUE>>>>>>>")
print(cuenta)
        







