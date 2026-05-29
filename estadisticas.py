#contadores
cantidad_total_consultas = 0
contador_recomendacion = 0

contador_vacaciones = 0
viajes_trabajo = 0

cantidad_usuarios = 0

contador_categoria = 0
contador_usuarios_sur = 0

#acumuladores
acumulador_dias = 0
presupuesto_sumado = 0


presupuesto_maximo_5_norte = 0
max_presupuesto_5_norte = 0

max_huespedes = 0
minimo_dias = 0

bandera_dias = True



        contador_recomendacion += 1
        cantidad_usuarios += 1
        presupuesto_sumado += presupuesto

        #función    MÁXIMO GRAL
        if numero_huespedes > max_huespedes:
            max_huespedes = numero_huespedes

        #función    PROMEDIO GRAL
        if cantidad_usuarios > 0:
            promedio_presupuesto = presupuesto_sumado // cantidad_usuarios
        
        #MÍNIMO
        if bandera_dias == True or numero_dias < minimo_dias:
            minimo_dias = numero_dias
            bandera_dias = False
        
        #MÁX CONDICIONADO   
        if estrellas == 5 and ubicacion == "norte":
            if presupuesto > presupuesto_maximo_5_norte:
                max_presupuesto_5_norte = presupuesto
                nombre_max_5_norte = nombre  

    #función    PORCENTAJE NO CONDICIONADO
    if motivo_viaje == "vacaciones":
            contador_vacaciones += 1

#    PORCENTAJE NO CONDICIONADO
    if cantidad_total_consultas > 0:
        promedio_vacaciones = (contador_vacaciones / cantidad_total_consultas) * 100

    #función    PORCENTAJE CONDICIONADO
    if categoria == "all inclusive" and ubicacion == "sur": 
        contador_categoria += 1
        contador_usuarios_sur += 1
        promedio_categoria = (contador_categoria / contador_usuarios_sur) * 100


        #promedio condicionado
    if viajes_trabajo > 0:
        promedio_trabajo = acumulador_dias / viajes_trabajo
        print(f"El promedio de días de estadía para viajes de trabajo fue de: {promedio_trabajo} días💼")
    else:
        print("No se registraron viajes de trabajo para calcular el promedio.")