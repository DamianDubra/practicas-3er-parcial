#ventas_autos.txt , tien fecha, vendedor  eimporte
#ya esta ordenado por vendedor
#mostarr cnatidad de ventas por vendedor,total por vendedor, vendedor con mas ventas, mayor importe vendedro

varchivo=open('ventas_autos.txt','r')
vregistro=varchivo.readline().rstrip()
vector=['']*3
vector=vregistro.split(';')
vendedor=int(vector[1])
vauxicantventas=0
vauximejorvend=0
vauximayorimpo=0.0
vauximejorfactura=0


while vregistro!='':
    vendedor=int(vector[1])
    vacumventas=0
    vcantiventas=0
    while vregistro!='' and vendedor==int(vector[1]):
        vcantiventas+=1
        vacumventas=float(vector[2])

        if vauxicantventas<vcantiventas:
            vauxicantventas=vcantiventas
            vauximejorvend=vendedor
        if vauximayorimpo<vacumventas:
            vauximayorimpo=vacumventas
            vauximejorfactura=vendedor
        vregistro=varchivo.readline().rstrip()
        vector=vregistro.split(';')
    print('elvendedor nro', vendedor,'facturo veces',vcantiventas,'el importe es',vacumventas)

print('el que mas tickets hizo fue',vauximejorvend,'el que mayor importe',vauximejorfactura)

varchivo.close()