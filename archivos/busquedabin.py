#Crea una lista ordenada de 50 números enteros (aleatorios, entre 100 y 999 inclusive) que representa el inventario de identificadores únicos de productos en un almacén. Diseña una función de búsqueda binaria que permita al usuario ingresar un número de ID y verifique si existe en el inventario.

#El programa debe mostrar la lista generada, luego permitir al usuario ingresar un número, y finalmente mostrar un mensaje que indique si el ID fue encontrado o no, y en qué posición de la lista se encuentra.

def ordenar(vector):
    ef=0
    elementos=len(vector)
    for barrido in range(0,elementos-1):
        for ev in range(ef+1,elementos):
            if vector[ev]<vector[ef]:
                vauxi=vector[ev]
                vector[ev]=vector[ef]
                vector[ef]=vauxi
        ef+=1
    return vector

def busquedabin(vector,elemento):
    senal=0
    vinicial=0
    vfinal=49
    posicio=-1
    while senal==0 and elemento<= vector[vfinal] and elemento >= vector[vinicial]:
        vcentra=(vinicial+vfinal)//2
        if elemento== vector[vcentra]:
            posicio=vcentra
            vsena=1
        if elemento> vector[vcentra]:
            vinicial=vcentra+1
        else:
            vfinal=vcentra-1
    if posicio<0:
        vsena=-1
    return posicio,vsena

import random
vector=[0]*50

for c in range(0,50):
    vector[c]=random.randint(100,999)

vector=ordenar(vector)
print(vector)
numero=int(input('ingrese la id'))
posicion,sena=busquedabin(vector,numero)

if sena!=-1:
    print('la posicion es',posicion)

else:
    print('no esta')