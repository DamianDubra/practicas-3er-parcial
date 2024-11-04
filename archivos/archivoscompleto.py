#objetivo: un programa, que cree copias de segurada, permita eliminar o cargar cliente y si llego que permita buscar un cliente

import shutil
quehacer=input('si desea cargar datos ingrese A, eliminar B, buscar un cliente C:')
continuar='si'


if quehacer=='A':
    varchivo=open('completo.txt','w')
    while continuar!='no':
        socio=input('nro de socio')
        nombre=input('nombre')
        edad=input('edad')
        ciudad=input('ciudad')
        trabajo=input('trabajo')
        vregistro=socio+';'+nombre+';'+edad+';'+ciudad+';'+trabajo
        varchivo.write(vregistro)
        varchivo.write('\n')
        continuar=input('desea cragar otro?')
    varchivo.close()

if quehacer=='B':
    varchivo1=open('completo.txt','r')
    shutil.copy('completo.txt','completobup.txt')
    varchinew=open('completonew.txt','w')
    vregistro1=varchivo1.readline().rstrip()
    eliminado=0
    vector=[]*5
    socioeliminar=int(input('socio a eliminar'))
    while vregistro1!='':
        vector=vregistro1.split(';')
        vsocio=int(vector[0])
        if vsocio==socioeliminar:
            eliminado=1
        else:
            varchinew.write(vregistro1)
            varchinew.write('\n')
        vregistro1=varchivo1.readline().rstrip()
    if eliminado==1:
        print('se elimino el socio')
    else:
        print('no se encontro el socio')
    varchinew.close()
    varchivo1.close()
    shutil.copy('completonew.txt','completo.txt')

if quehacer=='C':
    varchivo2=open('completo.txt','r')
    vregistro2=varchivo2.readline().rstrip()
    encontrado=0
    vector1=[]*5
    sociobuscar=int(input('socio a buscar'))
    while vregistro2!='':
        vector=vregistro2.split(';')
        socio1=int(vector[0])
        if socio1==sociobuscar:
            encontrado=1
            print('los datos del socio son',vregistro2)
        vregistro2=varchivo2.readline().rstrip()
    if encontrado!=1:
        print('no se encontro el cliente')
    varchivo2.close()