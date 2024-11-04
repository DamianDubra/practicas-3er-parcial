#crea un programa que contiene numero_socio;nombre;edad;ciudad
#El cliente agrega el nro de socio, si s elimina mostrar mensjae, si no mostrar que no existe
import shutil

varchivo=open('socios.txt','r')
vcopia=open('sociosbup.txt','w')
varchinew=open('sociosnew.txt','w')

shutil.copy('socios.txt','sociosbup.txt')

vregistro=varchivo.readline().rstrip()
vector=[]*4
eliminado=1

cliente=int(input('ingrese el cliente a eliminar'))

while vregistro!='':
    vector=vregistro.split(';')
    nrocli=int(vector[0])
    if nrocli==cliente:
        eliminado=0
        print('se elimino el socio')
    else:
        varchinew.write(vregistro)
        varchinew.write('\n')
    vregistro=varchivo.readline().rstrip()

if eliminado==1:
    print('no se encontro el cliente')

varchinew.close()
varchivo.close()
varchinew.close()
shutil.copy('sociosnew.txt','socios.txt')