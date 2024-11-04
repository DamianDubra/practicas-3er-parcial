#crea una matriz de 3x3, caargarla y dar la suma de sus elementos de la diagonal
#suma de filas y columas
# mayor elemento y menor elemenot


matrix=[[0,0,0],[0,0,0],[0,0,0]]
fila=0
columna=0
for i in range(0,3):
    for d in range(0,3):
        numero=int(input('ingrese un numero'))
        matrix[i][d]=numero

print(matrix)

vsumdiag=0

for c in range(0,3):
    vsumdiag+=matrix[c][c]
print(vsumdiag)

vsumfil=[0]*3
for p in range(0,3):
    for z in range(0,3):
        vsumfil[p]+=matrix[p][z]

print(vsumfil)

vsumcol=[0]*3
for h in range(0,3):
    for j in range(0,3):
        vsumcol[h]+=matrix[j][h]
print(vsumcol)

vauximax=0
vauximin=9999

for c in range(0,3):
    for d in range(0,3):
        if matrix[c][d]>vauximax:
            vauximax=matrix[c][d]
        if matrix[c][d]<vauximin:
            vauximin=matrix[c][d]

print(vauximax, vauximin)