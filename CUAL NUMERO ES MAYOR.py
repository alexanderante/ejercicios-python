
numero1 = float(input("ingresar el primer numero: "))
numero2 = float(input("ingresar el segundo numero: "))

if numero1 > numero2:
    print("el primer numero", numero1, "es mayor que el segundo numero", numero2)
elif numero1 < numero2:
    print("el segundo numero", numero2, "es mayor que el primer numero", numero1)
else:
    print("ambos numeros son iguales:", numero1, "=", numero2)
