def recomendar_cinco_estrellas(
                            presupuesto : int, 
                            motivo_viaje : str,
                            ubicacion : str, 
                            numero_huespedes : int,
                            check_in_elegido : str,
                            hotel_uno : str,
                            hotel_dos: str,
                            hotel_tres : str
                            ) -> str:
    
    '''
    # ¿Qué hace?
        Filtra los datos ingresados por el usuario para una recomendación de hotel.
        
    # ¿Qué recibe?
        Una serie de int y str.

    # ¿Qué retorna?
        Un str. 
    '''

    hotel_recomendado = ""

    if presupuesto >= 300 and motivo_viaje == "vacaciones" and (ubicacion == "sur" or ubicacion == "norte"):
        hotel_recomendado = hotel_uno

    elif presupuesto >= 250 and numero_huespedes <= 5 and ubicacion == "norte":
        if motivo_viaje == "vacaciones" or (motivo_viaje == "trabajo" and check_in_elegido == "14"):
            hotel_recomendado = hotel_dos

    elif presupuesto >= 200 and motivo_viaje == "trabajo" and check_in_elegido == "20" and not (ubicacion == "norte" or ubicacion == "sur"):
        hotel_recomendado = hotel_tres

    return hotel_recomendado

def recomendar_cuatro_estrellas(
                            presupuesto : int, 
                            motivo_viaje : str,
                            ubicacion : str,
                            categoria : str,
                            numero_huespedes : int,
                            numero_dias : int,
                            check_in_elegido : str,
                            hotel_cuatro : str,
                            hotel_cinco : str
                            ) -> str:

    '''
    # ¿Qué hace?
        Filtra los datos ingresados por el usuario para una recomendación de hotel.
        
    # ¿Qué recibe?
        Una serie de int y str.

    # ¿Qué retorna?
        Un str. 
    '''

    hotel_recomendado = ""

    if presupuesto >= 180 and ubicacion == "centro" and categoria == "all inclusive" and numero_huespedes >= 3 and numero_huespedes <= 15 and numero_dias <= 10:
        if motivo_viaje == "vacaciones" or (motivo_viaje == "trabajo" and check_in_elegido == "20"):
            hotel_recomendado = hotel_cuatro

    elif presupuesto >= 160 and motivo_viaje == "vacaciones" and (ubicacion == "sur" or ubicacion == "centro") and categoria == "solo alojamiento" and numero_dias >= 7 and numero_dias <= 15:
        hotel_recomendado = hotel_cinco

    return hotel_recomendado

def recomendar_tres_estrellas(
                            presupuesto : int, 
                            motivo_viaje : str,
                            ubicacion : str,
                            categoria : str,
                            numero_huespedes : int,
                            numero_dias : int,
                            check_in_elegido : str,
                            hotel_seis : str,
                            hotel_siete : str,
                            hotel_ocho : str
                            ) -> str:
    

    '''
    # ¿Qué hace?
        Filtra los datos ingresados por el usuario para una recomendación de hotel.
        
    # ¿Qué recibe?
        Una serie de int y str.

    # ¿Qué retorna?
        Un str. 
    '''

    hotel_recomendado = ""

    if presupuesto >= 150 and motivo_viaje == "vacaciones" and (ubicacion == "sur" or ubicacion == "norte") and categoria == "media pension" and numero_huespedes <= 10 and numero_dias >= 7 and numero_dias <= 10:
        hotel_recomendado = hotel_seis

    elif presupuesto >= 100 and ubicacion == "norte" and categoria == "media pension" and numero_dias <= 15:
        if motivo_viaje == "vacaciones" or (motivo_viaje == "trabajo" and check_in_elegido == "14"):
            hotel_recomendado = hotel_siete
        
    elif presupuesto >= 50 and motivo_viaje == "trabajo" and check_in_elegido == "14" and ubicacion == "centro" and categoria == "solo alojamiento" and numero_huespedes <= 8:
        hotel_recomendado = hotel_ocho

    return hotel_recomendado

def recomendar_dos_estrellas(
                            presupuesto : int, 
                            motivo_viaje : str,
                            ubicacion : str,
                            categoria : str,
                            numero_huespedes : int,
                            numero_dias : int,
                            check_in_elegido : str, 
                            hotel_nueve : str,
                            hotel_diez : str
                            ) -> str:
    
    '''
    # ¿Qué hace?
        Filtra los datos ingresados por el usuario para una recomendación de hotel.
        
    # ¿Qué recibe?
        Una serie de int y str.

    # ¿Qué retorna?
        Un str. 
    '''

    hotel_recomendado = ""

    if presupuesto >= 45 and motivo_viaje == "vacaciones" and (ubicacion == "norte" or ubicacion == "sur") and categoria == "media pension" and numero_huespedes >= 2 and numero_dias >= 3 and numero_dias <= 12:
        hotel_recomendado = hotel_nueve

    elif presupuesto >= 40 and motivo_viaje == "trabajo" and check_in_elegido == "20" and (ubicacion == "norte" or ubicacion == "centro") and categoria == "solo alojamiento" and numero_huespedes >= 15 and numero_dias >= 5:
        hotel_recomendado = hotel_diez

    return hotel_recomendado

def recomendar_una_estrella(
                            presupuesto : int, 
                            motivo_viaje : str,
                            ubicacion : str,
                            numero_huespedes : int,
                            numero_dias : int,
                            check_in_elegido : str,
                            hotel_once : str,
                            hotel_doce : str,
                            hotel_trece : str
                            ) -> str:
    
    '''
    # ¿Qué hace?
        Filtra los datos ingresados por el usuario para una recomendación de hotel.
        
    # ¿Qué recibe?
        Una serie de int y str.

    # ¿Qué retorna?
        Un str. 
    '''

    hotel_recomendado = ""

    if presupuesto >= 30 and motivo_viaje == "vacaciones" and (ubicacion == "sur" or ubicacion == "norte") and numero_huespedes <=10:
        hotel_recomendado = hotel_once

    elif presupuesto >= 25 and ubicacion == "norte" and numero_huespedes >= 5 and numero_dias >= 10:
        if motivo_viaje == "vacaciones" or (motivo_viaje == "trabajo" and check_in_elegido == "20"):
            hotel_recomendado = hotel_doce

    elif presupuesto >= 20 and motivo_viaje == "trabajo" and check_in_elegido == "14" and (ubicacion == "norte" or ubicacion == "centro") and numero_huespedes <= 3 and numero_dias >= 7: 
        hotel_recomendado = hotel_trece

    return hotel_recomendado