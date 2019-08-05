"""
1.- Dadas 2 tuplas crear un diccionario donde  la primera tupla sean las claves y la segunda los valores.
"""

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
        else:
            print("Usuario repetido, Ingrese nuevamente.")

    llave=tuple(Lista1)
    valor=tuple(Lista2)
    dicc=dict(zip(llave,valor))
    print(dicc)

#dicc()

#2.- Escribir una funcion que reciba una cadena y devuelva un diccionario con la cantidad de apariciones de cada palabra".


def cadena():
    cadena=str(input("Ingrese oracion: "))
    a=""
    Lista1=[]
    Lista2=[]
    Lista3=[]
    for i in cadena:
        if i != " ":
            a=a+i
        elif i== " ":
            Lista1.append(a)
            a=""
    Lista1.append(a)
    for j in Lista1:
        b=Lista1.count(j)
        if j not in Lista3:
            Lista3.append(j)
            Lista2.append(b)
    dicc=dict(zip(Lista3,Lista2))
    print(dicc)
#cadena()

#3.- Lo mismo pero para cada cantidad de caracter.

def cadenaC():
    cadena=str(input("Ingrese oracion: "))
    a=""
    Lista1=[]
    Lista2=[]
    Lista3=[]
    for i in cadena:
        if i != "":
            a=a+i
        elif i== "":
            Lista1.append(a)
            a=""
    Lista1.append(a)
    for j in Lista1:
        b=Lista1.count(j)
        if j not in Lista3:
            Lista3.append(j)
            Lista2.append(b)
    dicc=dict(zip(Lista3,Lista2))
    print(dicc)
cadenaC()
