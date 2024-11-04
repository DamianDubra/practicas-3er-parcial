#se tiene el archivo de los deportistas d eolimpiadas
#juegoba.txt
#campo apellido y nombe, dni,ciudad,deporte, edad, sexo h o m
#mostrar personas por deporte, mujeres por deporte, prom edad mujeres por deporte, promedio edad hombre por deporte, deporte mas practicado

varchivo=open('juegoba.txt','r')
vregistro=varchivo.readline().rstrip()
vdeporte=''
vector=['']*5
vcantimuj=0
vacumedmuj=0
vprommuj=0.0
vcantihom=0
vacumhomb=0
vpromhom=0.0
vauxicantmaspracti=0
vauximaspracticado=''
vector=vregistro.split(';')
vdeportecontrol=vector[0]


while vregistro!='':
    vcantipersonasdepor=0
    while vregistro!='' and vdeportecontrol==vector[0]:
        if vcantimuj!=0:
            vprommuj=vacumedmuj/vcantimuj
        print('la cantidad mujeres en el deporte',vector[0],'es',vcantimuj,'la edad promedio ',vprommuj)
        if vcantihom!=0:
            vpromhom=vacumhomb/vcantihom
        print('el promedio de edad de hombres en el depote',vcantihom, vector[0],'es',vpromhom)
        if vcantipersonasdepor>vauxicantmaspracti:
            vauxicantmaspracti=vcantipersonasdepor
            vauximaspracticado=vector[0]
        vcantipersonasdepor+=1
        if vector[5]=='m':
            vcantimuj+=1
            vacumedmuj+=int(vector[4])
        if vector[5]=='h':
            vcantihom+=1
            vacumhomb+=int(vector[4])
        vector=vregistro.split(';')
        vdeportecontrol=vector[0]
        vregistro=varchivo.readline().rstrip()

        
print('el deporte mas practicado es ', vauximaspracticado,'con persons que lo practican', vauxicantmaspracti)
varchivo.close()
