#crea una funcio qye devuelve el nro de elemento dode esya ek nrodelegjo
#vector_legajo de 1000 elementrs, ya ordenado el legajo_bajo, si noe sta devuelve -1

def bsucar_legajo(vecto_legajo,legajo_buscar):
    vincial=0
    vfinal=9
    vsenal=0
    vposicion=-1
    while vsenal==0 and legajo_buscar>=vecto_legajo[vincial] and legajo_buscar<=vecto_legajo[vfinal]:
        vcentro=(vincial+vfinal)//2
        if legajo_buscar==vecto_legajo[vcentro]:
            vsenal=1
            vposicion=vcentro
        if legajo_buscar>vecto_legajo[vcentro]:
            vincial=vcentro+1
        else:
            vfinal=vcentro-1
    if vposicion<0:
        vsenal=-1
    return vposicion,vsenal
import random
vecro_legajo=[0]*10
for c in range(0,10):
    vecro_legajo[c]=random.randint(0,10)

vecro_legajo.sort()
print(vecro_legajo)
numero=5
posicion,encuentra=bsucar_legajo(vecro_legajo,numero)

print(posicion,encuentra)
        
