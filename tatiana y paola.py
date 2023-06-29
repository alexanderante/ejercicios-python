
def calcular_costo_total(campanario_cafe, terraplaza_cafe, transporte_costo):
    costo_campanario = campanario_cafe * 2 + transporte_costo
    costo_terraplaza = terraplaza_cafe * 2

    if costo_campanario < costo_terraplaza:
        return "la mejor opcion es ir al centro comercial campanario. el costo total seria de {}.".format(costo_campanario)
    elif costo_terraplaza < costo_campanario:
        return "la mejor opción es ir a terraplaza. el costo total seria de {}.".format(costo_terraplaza)
    else:
        return "ambas opciones tienen el mismo costo total de {}.".format(costo_campanario)


campanario_cafe = 4000
terraplaza_cafe = 2 * campanario_cafe
transporte_costo = 1600

resultado = calcular_costo_total(campanario_cafe, terraplaza_cafe, transporte_costo)
print(resultado)
