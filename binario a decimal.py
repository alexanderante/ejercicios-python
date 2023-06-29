numero_binario = input("ingrese un numero binario: ")
posicion = len(numero_binario) - 1
potencia = 0
numero_decimal = 0
while posicion >= 0:
   
    digito = int(numero_binario[posicion])
    
    numero_decimal += digito * 2**potencia
    
    posicion -= 1
    potencia += 1
print("el numero decimal equivalente es:", numero_decimal)
print(numero_binario, "(binario) = ", numero_decimal, "(decimal)")