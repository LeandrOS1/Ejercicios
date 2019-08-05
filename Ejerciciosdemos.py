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
