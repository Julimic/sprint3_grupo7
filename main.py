from reglas import *
from input import *
from print import *
from hoteles import *

def recomendar_hotel(estrellas : int,
                    presupuesto : int,
                    motivo_viaje : str,
                    ubicacion : str,
                    categoria : str,
                    numero_huespedes : int,
                    numero_dias : int,
                    check_in_elegido : int):
    
    if estrellas == 5:
        return recomendar_cinco_estrellas(presupuesto, motivo_viaje, ubicacion, numero_huespedes, check_in_elegido)
    
    if estrellas == 4:
        return recomendar_cuatro_estrellas(presupuesto, motivo_viaje, ubicacion, categoria, numero_huespedes, numero_dias, check_in_elegido)

    if estrellas == 3:
        return recomendar_tres_estrellas(presupuesto, motivo_viaje, ubicacion, categoria, numero_huespedes, numero_dias, check_in_elegido)
    
    if estrellas == 2:
        return recomendar_dos_estrellas(presupuesto, motivo_viaje, ubicacion, categoria, numero_huespedes, numero_dias, check_in_elegido)
    
    if estrellas == 1:
        return recomendar_una_estrella(presupuesto, motivo_viaje, ubicacion, numero_huespedes, numero_dias, check_in_elegido)

def iniciar_recomendacion ():

    print("🛎️¡Bienvenido a nuestro sistema de recomendación hotelera!🛎️")
    print("Por favor complete los siguientes datos para iniciar la recomendación✍🏻: ")


    nombre = validar_str(pedir_str("Ingrese su nombre para la recomendación: "))
    mostrar_dato("El nombre ingresado es:", nombre)

    apellido = validar_str(pedir_str("Ingrese su apellido: "))
    mostrar_dato("El apellido ingresado es:", apellido)


    motivo_viaje = validar_motivo_viaje(pedir_str("Ingrese su motivo de viaje (trabajo/vacaciones): "), "trabajo", "vacaciones", None, "Error. Ingrese un motivo de viaje válido: ")
    mostrar_dato("El motivo de viaje ingresado es:", motivo_viaje)


    ubicacion = validar_motivo_viaje(pedir_str("Ingrese la ubicación del hotel (norte/sur/centro): "), "norte", "sur", "centro", "Error. Ingrese una ubicación válida: ")
    mostrar_dato("La ubicación ingresada es:", ubicacion)


    categoria = validar_motivo_viaje(pedir_str("Ingrese la categoría de hotel que desee (all inclusive, media pensión, solo alojamiento): "), "all inclusive", "media pension", "solo alojamiento", "Error. Ingrese una categoría válida: ")
    mostrar_dato("La categoría ingresada es:", categoria)

    estrellas = validar_estrellas(validar_int(pedir_int("Ingrese la cantidad de estrellas del hotel (1/5): ")))
    mostrar_dato("El número de estrellas ingresado es:", estrellas)

    presupuesto = validar_presupuesto(pedir_int("Ingrese su presupuesto de viaje: "))
    mostrar_dato("El presupuesto ingresado es:", presupuesto)


    numero_huespedes = validar_huespedes_dias(pedir_int("Ingrese la cantidad de huéspedes: "))
    mostrar_dato("La cantidad de huéspedes ingresada es:", numero_huespedes)


    numero_dias = validar_huespedes_dias(pedir_int("Ingrese la cantidad de días a hospedarse: "))
    mostrar_dato("La cantidad de días a hospedarse ingresados es de:", numero_dias)


    mostrar_menu_check_in()
    check_in_elegido = seleccionar_check_in("Ingrese el horario en que desee:", "Error. Debe ingresar alguna de las dos opciones.")
    mostrar_dato("El check-in elegido es:", check_in_elegido)



    hotel_recomendado = recomendar_hotel(estrellas, presupuesto, motivo_viaje,ubicacion, categoria, numero_huespedes, numero_dias, check_in_elegido)

    return hotel_recomendado

