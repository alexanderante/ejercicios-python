# Elabore un  programa me muestre en  pantalla el  tipo de  dato  que el usuario  ha ingresado, por  ejemplo si  ingresa Juan el  deberá decir 
# que es texto, en caso  que ingrese 2018 deberá decir que es  entero 

valor = input("ingresa un valor: ")

if valor.isdigit():
    print("el valor ingresado es de tipo entero.")
else:
    print("el valor ingresado es de tipo texto.")

