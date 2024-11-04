#Sse tiene cargado un vector de 1000 elementos cargardo y ordenado, mostrar cuantas veces se repite cada uno

def f_ordenar(vector):
    ef=0
    elementos=len(vector)
    for barrdio in range(0,elementos-1):
        for ev in range(ef+1,elementos):
            if vector[ev]<vector[ef]:
                vauxi=vector[ef]
                vector[ef]=vector[ev]
                vector[ev]=vauxi
        ef+=1
    return vector

import random

vector=[0]*1000
for c in range(0,1000):
    vector[c]=random.randint(0,10)
vector=f_ordenar(vector)

vauxi=vector[0]
for c in range (0,1000):
    vauxi=vector[c]
    vcontnum=0
    for d in range(0,1000):
        if vector[d]==vauxi:
            vcontnum+=1
    if c<999:
        if vauxi<vector[c+1]:
            print(vauxi,'se repite',vcontnum)
    
