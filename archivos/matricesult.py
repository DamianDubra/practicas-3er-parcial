#Se ingresa con opción a continuar las producciones realizadas por las distintas sucursales de una empresa:

#- Número de sucursal: entero (1-4)
#- Fecha de producción: cadena
#- Toneladas producidas: real

#Mostrar:

#- Cantidad de producciones por horno por sucursal
#- Total producido por horno por sucursal
#- Total producido por sucursal
#- Número de sucursal con el mayor total de toneladas producidas (repetido)

vcontinua=''
matriz=[[0,0,0,0],[0,0,0,0]]
vmaximaprodu=0
vsucursalmaspro=0
while vcontinua!='no':
    fecha=input('fecha')
    sucursal=int(input('sucrsal 1 al 4'))-1
    tonelasas=float(input('toneladas'))
    matriz[0][sucursal]+=1
    matriz[1][sucursal]+=tonelasas
    print(matriz)
    vcontinua=input('continua?')


for d in range(0,4):
    if vmaximaprodu<matriz[1][d]:
        vmaximaprodu=matriz[1][d]
        vsucursalmaspro=d+1

print(matriz)
print(vsucursalmaspro)