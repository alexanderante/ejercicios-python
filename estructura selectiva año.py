
def es_bisiesto(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
        return True
    else:
        return False


anio = int(input("ingrese un año: "))

if es_bisiesto(anio):
    print("el año {} es bisiesto.".format(anio))
else:
    print("el año {} no es bisiesto.".format(anio))
