
def verificar_numero(numero):
    if numero.is_integer():
        print("el numero {} es entero.".format(numero))
    else:
        print("el numero {} es real.".format(numero))


numero = float(input("ingrese un numero: "))
verificar_numero(numero)
