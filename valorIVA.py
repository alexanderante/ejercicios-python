#Calcule el  valor  del  IVA 19% y el descuento de un producto ingresado por teclado

precio = int(input(" ingrese valor del producto: "))
iva = precio * 0.19
descuento = precio * 0.2
precio_total = precio + iva - descuento

print ("valor del iva (19%):", iva)
print ("descuento:", descuento)
print ("precio total con iva y descuento:", precio_total)
