from input import *

#MÁXIMO GENERAL
def calcular_maximo_huespedes(numero_huespedes : int, 
                                max_huespedes : int) -> int:
    
    if numero_huespedes > max_huespedes:
        max_huespedes = numero_huespedes
    
    return max_huespedes


#MÍNIMO
def calcular_minimo_dias(numero_dias : int,
                        minimo_dias : int,
                        bandera_dias : bool) -> int:
    
    if bandera_dias == True or numero_dias < minimo_dias:
        minimo_dias = numero_dias

        bandera_dias = False
    
    return minimo_dias

#MÁXIMO CONDICIONADO
def calcular_maximo_norte(estrellas : int,
                        ubicacion : str,
                        presupuesto : int,
                        presupuesto_maximo_norte : int) -> int:
    
    if estrellas == 5 and ubicacion == "norte":
        if presupuesto > presupuesto_maximo_norte:
            max_presupuesto = presupuesto

#ver nombre
    return max_presupuesto

#PORCENTAJE NO CONDICIONADO 
def calcular_porcentaje_vacaciones(contador_vacaciones : int,
                                cantidad_total_consultas : int) -> float:
    

    
    if cantidad_total_consultas > 0:
        promedio_vacaciones = (contador_vacaciones / cantidad_total_consultas) * 100
    else:
        promedio_vacaciones = 0
    
    return promedio_vacaciones

#PORCENTAJE CONDICIONADO
def calcular_porcentaje_categoria(contador_categoria : int, 
                                contador_usuarios_sur : int) -> float:
    
    if contador_usuarios_sur > 0:

        promedio_categoria = (contador_categoria / contador_usuarios_sur) * 100
    
    else:
        promedio_categoria = 0

    return promedio_categoria

#PROMEDIO GENERAL  
def calcular_promedio_presupuesto(cantidad_usuarios : int,
                                presupuesto_sumado : int) -> float:
    
    if cantidad_usuarios > 0:
        promedio = presupuesto_sumado / cantidad_usuarios
    
    else:
        promedio = 0
    
    return promedio


#PROMEDIO CONDICIONADO
def calcular_promedio_trabajo(acumulador_dias : int,
                            viajes_trabajo : int) -> float:
    
    if viajes_trabajo > 0:
        promedio_trabajo = acumulador_dias / viajes_trabajo
    
    else:
        promedio_trabajo = 0
    
    return promedio_trabajo


#GRÁFICO

linea_hotel_uno = 0
linea_hotel_dos = 0
linea_hotel_tres = 0
linea_hotel_cuatro = 0
linea_hotel_cinco = 0
    
def validar_contador (estrellas_validadas : int , contador : int , numero_estrella : int) -> int:
    if estrellas_validadas == numero_estrella:
        return contador + 1
    else:
        return contador
    


def grafico_cinco_columnas(linea_hotel_uno: int, 
                        linea_hotel_dos: int, 
                        linea_hotel_tres: int, 
                        linea_hotel_cuatro: int, 
                        linea_hotel_cinco: int):


    '''

    '''


    valor_maximo = linea_hotel_uno
    if linea_hotel_dos > valor_maximo:
        valor_maximo = linea_hotel_dos
    if linea_hotel_tres > valor_maximo:
        valor_maximo = linea_hotel_tres
    if linea_hotel_cuatro > valor_maximo:
        valor_maximo = linea_hotel_cuatro
    if linea_hotel_cinco > valor_maximo:
        valor_maximo = linea_hotel_cinco

    if valor_maximo == 0:
        return "No hay datos suficientes para mostrar el gráfico."


    mensaje_final = ""


    for i in range(valor_maximo, 0, -1):
        linea = ""

        if linea_hotel_uno >= i:
            linea += "█   "
        else:
            linea += "  "

        if linea_hotel_dos >= i:
            linea += "█   "
        else:
            linea += "  "

        if linea_hotel_tres >= i:
            linea += "█   "
        else:
            linea += "  "

        if linea_hotel_cuatro >= i:
            linea += "█   "
        else:
            linea += "  "

        if linea_hotel_cinco >= i:
            linea += "█   "
        else:
            linea += "  "

        mensaje_final += linea + "\n"

    return mensaje_final + "1⭐ 2⭐ 3⭐ 4⭐ 5⭐"
    


estrellas_validadas = validar_estrellas(validar_int(estrellas))

linea_hotel_uno = validar_contador(estrellas_validadas, linea_hotel_uno, 1)
linea_hotel_dos = validar_contador(estrellas_validadas, linea_hotel_dos, 2)
linea_hotel_tres = validar_contador(estrellas_validadas, linea_hotel_tres, 3)
linea_hotel_cuatro = validar_contador(estrellas_validadas, linea_hotel_cuatro, 4)
linea_hotel_cinco = validar_contador(estrellas_validadas, linea_hotel_cinco, 5)

