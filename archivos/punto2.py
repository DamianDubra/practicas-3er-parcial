#se tiene un archivo de viajes de micros
#viajes_micros.txt
#tiene capo fechaviaje,campo pasajeros, campo nromicro seprado por ;
#nro de mirco entre 1 y 50
#mostrar cant viajes por micro, total de pasajeros tranpo por micro, total de pasajeros por semestre

#cargo los datos porque si
vviajes1=open('viajes_micros.txt','w')
votro='si'
while votro!='no':
    fecha=input('ingrese dia/mes')
    pasajeros=input('ingrese pasajeros')
    micro=input('ingrese numero de micro')
    vregistro1=fecha+';'+ pasajeros +';'+ micro
    vviajes1.write(vregistro1)
    vviajes1.write('\n')
    votro=input('continuar?')
vviajes1.close()

#programa pricnipal
vfecha=''
vmiccro=0
vmes=0
vectorfecha=[0]*2
vsemestre=0
vector=[]*3
vcontviajes=0
vectorcontpormicro=[0]*50
vectoracumpormicro=[0]*50
vviajes=open('viajes_micros.txt','r')
vacumsemetr1=0
vacumsemetr2=0

vregistro=vviajes.readline()

while vregistro!='':
    vector=vregistro.split(';')
    vfecha=vector[0]
    vectorfecha=vfecha.split('/')
    vmes=int(vectorfecha[1])
    vmiccro=int(vector[2])
    vectoracumpormicro[vmiccro-1]+=int(vector[1])
    vectorcontpormicro[vmiccro-1]+=1
    if vmes<=6:
        vacumsemetr1+=int(vector[1])
    else:
        vacumsemetr2+=int(vector[1])
    vregistro=vviajes.readline()

vviajes.close()
for c in range(0,50):
    print('la cantidad de viajes del micro', c+1,vectorcontpormicro[c], 'los pasajeros son',vectoracumpormicro[c])
print('primer semestre', vacumsemetr1)
print('segundo semestre',vacumsemetr2)
    