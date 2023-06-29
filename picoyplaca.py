
p = input ("introducir numero de placa " )
if len (p) == 6:
    try:
        X= int (p[5])
    except:
        x = int(p[4])

if x == 1 or x == 2:
    print ("viernes")

elif x == 3 or x == 4:
    print ("lunes")

elif x == 5 or x == 6:
    print ("martes")

elif x == 7 or x == 8:
    print ("miercoles")

elif x == 9 or x == 0:
    print ("jueves")

else:
    print ("no tiene pico y placa")
    