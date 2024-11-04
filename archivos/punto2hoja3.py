#se tiene un archvio con las produ de cobre
#los campos son fecha, turno,toneladas y nro hrono
#horno entre 1 y 30
#mostrar cantidad producc por horno,total tones por horn, tones por cuATi

#varchivo=open('produ_cobre.txt','w')
#votro=''

#while votro!='no':
    #fecha=input('cargue fecha')
    #turno=input('truno')
    #tone=input('cargeu tone')
    #horno=input('nro horno')
    #vregsitro=fecha+';'+turno+';'+tone + ';'+ horno
    #varchivo.write(vregsitro)
    #varchivo.write('\n')
    #votro=input('otro?')

#archivo.close()

varchivo1=open('produ_cobre.txt','r')
vregistro1=varchivo1.readline().rstrip()
vector=[]*4
vectoracumhorno=[0.0]*30
vectorcontahorno=[0]*30
vectorcuatri=[0.0]*30
vfecha=['']*12

while vregistro1!='':
    vector=vregistro1.split(';')
    vtone=float(vector[2])
    vfecha=vector[0].split('/')
    vmes=int(vfecha[1])
    nrohorno=int(vector[3])-1
    match vmes:
        case vmes if vmes<=4:
            cuatrimetre=0
        case vmes if vmes>4 and vmes<=8:
            cuatrimetre=1
        case vmes if vmes>8:
            cuatrimetre=2
    vectorcuatri[cuatrimetre]+=vtone
    vectoracumhorno[nrohorno]+=vtone
    vectorcontahorno[nrohorno]+=1
    vregistro1=varchivo1.readline().rstrip()

varchivo1.close()

for c in range(0,30):
    print('el horno nro', c+1,'total produs',vectorcontahorno[c],'toneladas', vectoracumhorno[c])

for d in range(0,3):
    print('el cuatrimestre',d+1,'hizo toneladas', vectorcuatri[d])