#desarrolle una funcion inversa que recibe un diccionario y devuelva
'''
'''

def dicc():
    Lista1=[]
    Lista2=[]
    print("Para detener ingrese 'Alto'")
    while True:
        x=input("Ingrese llave: ")
        if x=="Alto" or x=="alto":
            break
        if x not in Lista1:
            y=input("Ingrese valor: ")
            Lista1.append(x)
            Lista2.append(y)

    llave=tuple(Lista1)
    valor=tuple(Lista2)
    dicc=dict(zip(llave,valor))
    print(dicc,"DIDIDIDIDI")
    
    a=dicc.values()
    b=dicc.keys()
    aaaa=dict(zip(a,b))
    print(aaaa)
    
#dicc()

'''
2 Cree un diccionario que tenga como llave el nombre de una persona, y los valores dentro de una lista
#desarrolle una funcion que, contenga como argumento el diccionario la persona y un gusto
 def x(diccionario,persona,gusto)
 si la persona ingresada no existe, la agrega al diccionario, con una lista que contiene un solo elemento
 si la persona existe y el gusto existe, no se hace nada, si el gusto no existe agrego el gusto.
 
'''

def GUSTO():
    Lista1=[]
    Lista2=[]
    print("Para detener ingrese '*'")
    while True:
        x=input("Ingrese el nombre de la persona:  ")
        if x=="*":
            break
        if x not in Lista1:
            Lista1.append(x)
            y=input("Ingrese gustos:  ")
            if y not in Lista2: 
                Lista2.append(y)

    llave=tuple(Lista1)
    valor=tuple(Lista2)
    dicc=dict(zip(llave,valor))
    print("Imprimiendo el diccionario......")
    print(dicc)
GUSTO()






