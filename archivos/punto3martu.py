#elecciones.txt ordenado por campo ciudad 
#primero ciudad, votos milei, votos massa  
#calcular total votos de cada uno por ciudad, ciudad con mas votos x c/u no son repetidos


varchivo=open('elecciones.txt','r')
vector=[]*4
vauximasvotosmilei=0
vauximasvotosmassa=0
vectorciudad=''
vectorciudadmassa=''

vregistro=varchivo.readline()

while vregistro!='':
    vector=vregistro.split(';')
    if vauximasvotosmilei<int(vector[2]):
        vauximasvotosmilei=int(vector[2])
        vectorciudad=vector[1]
    if vauximasvotosmassa<int(vector[3]):
        vauximasvotosmassa=int(vector[3])
        vectorciudadmassa=vector[1]
    print('los votos de mieli en', vector[1],vector[2])
    print('los votos de massa en:', vector[1],vector[3])
    print('total de votos es: ',int(vector[2])+int(vector[3]),vector[1])
    vregistro=varchivo.readline()
varchivo.close()
print('la ciudad con mas votos de massa',vauximasvotosmassa, vectorciudadmassa)
print('la ciudad con mas votos de milei es ',vauximasvotosmilei, vectorciudad)
