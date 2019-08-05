#Diccionarios
from Ejercicios import alumnos

alumnos={"V":10,"C":16,"P":18}
del alumnos["P"]
#alumnos.has_Key("C")
print(alumnos.get("C"))
print(alumnos.keys())
print(alumnos.values())
print(len(alumnos))
print(alumnos.get("Val"))
print(alumnos.pop("Casd","Null Pointer Exception"))
b=dict(j=20,a=19)
print(b)
c=dict(zip("abc",['awe','asd','zxc']))
print(c)
e=alumnos.copy()
print(e)





