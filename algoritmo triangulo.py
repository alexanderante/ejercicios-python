
import math

lado1 = float(input("ingrese la longitud del lado 1 del triangulo: "))
lado2 = float(input("ingrese la longitud del lado 2 del triangulo: "))
lado3 = float(input("ingrese la longitud del lado 3 del triangulo: "))

semiperimetro = (lado1 + lado2 + lado3) / 2
area = math.sqrt(semiperimetro * (semiperimetro - lado1) * (semiperimetro - lado2) * (semiperimetro - lado3))

print("el area del triangulo es:", area)
