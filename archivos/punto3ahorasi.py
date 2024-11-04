#archivo ventas.txt cada refitro representa una venta, tiene nro vendedor fecha factura, importe
#vendedro del 1 al 40 
#mostarr cantidad de ventas e importe por vendedro, facturacion por mes , vendedor con mas ventas, maximo repetido

vventas=open('ventas.txt','w')
votro=''

while votro!='no':
    vendedor=input('nro vendedro: ')
    fecha=input('fecha dd/mm/aaaa')
    importe=input('importe')
    vregistro=vendedor+';'+fecha+';'+importe
    vventas.write(vregistro)
    vventas.write('\n')
    votro=input('continuar?')

vventas.close()

#variables
vectorarchivo=['']*3
vectorcantventas=[0]*41
vectoracumimportevendedor=[0.0]*41
vectormesfacturado=[0.0]*12
vmascantventas=0
vauximes=[0]*3

vventas1=open('ventas.txt','r')
vregistro=vventas1.readline()

while vregistro!='':
    vectorarchivo=vregistro.split(';')
    vauxivend=int(vectorarchivo[0])
    vectorcantventas[vauxivend-1]+=1
    vectoracumimportevendedor[vauxivend-1]+=float(vectorarchivo[2])
    #por mes
    vauximes=vectorarchivo[1].split('/')
    vectormesfacturado[int(vauximes[1])-1]+=float(vectorarchivo[2])
    vregistro=vventas1.readline()

for c in range (0,41):
    if vmascantventas<vectorcantventas[c]:
        vmascantventas=vectorcantventas[c]

for z in range(0,41):
    print('el vendedor nro: ',z+1,'realizo ',vectorcantventas[z],'ventas, y el total de importe: ', vectoracumimportevendedor[z])
#se muestra el que mas vendio
for i in range(0,41):
    if vectorcantventas[i]==vmascantventas:
        print('uno de los que mas vendio fue el: ',i+1)

for d in range(0,12):
    print('el importe facturado en el mes: ',d+1, vectormesfacturado[d])