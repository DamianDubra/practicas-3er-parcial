import shutil
vclientes=open('cliente.txt','r')
vecto=[]*4

shutil.copy('cliente.txt','clienteBup.txt')
nrocli=int(input('ingrese cliente'))

varchivonuevo=open('cieltnenew.txt','w')
vregistar=vclientes.readline()
while vregistar!='':
    vecto=vregistar.split(';')
    vnumerosocio=int(vecto[0])
    if vnumerosocio!=nrocli:
        varchivonuevo.write(vregistar)
    else:
        print('se elimino el socio')
    vregistar=vclientes.readline()
varchivonuevo.close()
vclientes.close()
shutil.copy('cieltnenew.txt','cliente.txt')
