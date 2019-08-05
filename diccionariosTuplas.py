#11111 dadas 2 tuplas donde la primera se la clave y la seugnda el valor
i=str
l={}
while i!="ya no":
    j=str(input("Desea ingresar mas usuarios? yes or no:    "))
    if  j=="yes":      
        i=str(input("Ingrese usuarios:  "))
        h=str(input("Ingrese password:  "))
        if i not in l:
            l[i]=h
        else:
            print(i,"El usuario ingresado ya existe:.   ")
    else:
        break
print(l)


#2222Escribir una funcion que reciba una cadena
#y devuelva un diccionario con la cantidad
#de apariciones de cada palabra en la cadena

#33333Escribir una funcion que reciba una cadena
#y devuelva un diccionario con la cantidad
#de apariciones de cada palabra en la cadena