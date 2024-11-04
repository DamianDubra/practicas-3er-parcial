#realizar una funcion f_factorial para sacar el fatorial de un nuemro entero como parametro
def f_factorial(parametro):
    if parametro==0:
        factorial=1
    else:
        factorial=f_factorial((parametro-1))*parametro
    return factorial

numero=int(input('ingrese parametro'))
print(f_factorial(numero))