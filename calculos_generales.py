hotel_1_es = 0
hotel_2_es = 0
hotel_3_es = 0
hotel_4_es = 0
hotel_5_es = 0

def grafico_cinco_columnas(hotel_1_es: int, hotel_2_es: int, hotel_3_es: int, hotel_4_es: int, hotel_5_es: int):

    '''
    
    '''

    valor_maximo = hotel_1_es
    if hotel_2_es > valor_maximo:
        valor_maximo = hotel_2_es
    if hotel_3_es > valor_maximo:
        valor_maximo = hotel_3_es
    if hotel_4_es > valor_maximo:
        valor_maximo = hotel_4_es
    if hotel_5_es > valor_maximo:
        valor_maximo = hotel_5_es
    
    if valor_maximo == 0:
        return "No hay datos suficientes para mostrar el gráfico."

    mensaje_final = ""

    for i in range(valor_maximo, 0, -1):
        linea = ""
        
        if hotel_1_es >= i:
            linea += "█ "
        else:
            linea += "  "
            
        if hotel_2_es >= i:
            linea += "█ "
        else:
            linea += "  "
            
        if hotel_3_es >= i:
            linea += "█ "
        else:
            linea += "  "
            
        if hotel_4_es >= i:
            linea += "█ "
        else:
            linea += "  "
            
        if hotel_5_es >= i:
            linea += "█ "
        else:
            linea += "  "
        
        mensaje_final += linea + "\n"
    
    return mensaje_final + "1⭐ 2⭐ 3⭐ 4⭐ 5⭐"

if estrellas == 1:
    hotel_1_es += 1
        
elif estrellas == 2:
    hotel_2_es += 1
        
elif estrellas == 3:
    hotel_3_es += 1
        
elif estrellas == 4:
    hotel_4_es += 1
        
elif estrellas == 5:
    hotel_5_es += 1
