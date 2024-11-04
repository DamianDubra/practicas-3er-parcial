#crear una funcion recursva de serio de fi
def f_fibonacci(paarmetro):
    if paarmetro == 1 or paarmetro ==2 :
        resultado=1
    else:
        resultado=f_fibonacci(paarmetro-2)+f_fibonacci(paarmetro-1)

    return resultado

numero=int(input('numeor'))
print(f_fibonacci(numero))