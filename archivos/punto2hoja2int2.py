varchivo=open('juegoba.txt','r')
vregistro=varchivo.readline().rstrip()

vector=['']*5
vector=vregistro.split(';')
vdeporte=vector[3]
sexo=vector[5]
edad=int(vector[4])

vcontmuj=0
vconthom=0

vacummuj=0
vacumhom=0

vprommuj=0.0
vpromhom=0.0

vcontadorpersonaspordeport=0
vauxicantmaspersonas=0
vdeportemaspractic=''

while vregistro!='':
    vdeporte=vector[3]
    vcontadorpersonaspordeport=0
    vconthom=0
    vcontmuj=0
    vacumhom=0.0
    vacummuj=0.0
    while vregistro!='' and vdeporte == vector[3] :
        vcontadorpersonaspordeport+=1
        sexo=vector[5]
        edad=int(vector[4])
        if sexo=='m':
            vcontmuj+=1
            vacummuj+=edad
        else:
            vconthom+=1
            vacumhom+=edad

        if vcontadorpersonaspordeport>vauxicantmaspersonas:
            vauxicantmaspersonas=vcontadorpersonaspordeport
            vdeportemaspractic=vector[3]
        vregistro=varchivo.readline().rstrip()
        vector=vregistro.split(';')
    if vcontmuj!=0:
        vprommuj=vacummuj/vcontmuj
    if vconthom!=0:
        vpromhom=vacumhom/vconthom
    print('la cantidad de mujeres en', vdeporte,vcontmuj,'la edad promedio',vprommuj)
    print('la cantidad de hombres en', vdeporte,vconthom,'la edad promedio',vpromhom)
    print('lacantidad de personas que practian el deporte',vdeporte,'es',vcontadorpersonaspordeport)
   
print('la cantidad de personas que mas practican es',vauxicantmaspersonas,'y el deporte es',vdeportemaspractic)

varchivo.close()