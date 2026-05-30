from input import *
from print import *
from reglas import *
from estadisticas import *
from calculos_generales import *


def recomendar_hotel(estrellas : int,
                    presupuesto : int,
                    motivo_viaje : str,
                    ubicacion : str,
                    categoria : str,
                    numero_huespedes : int,
                    numero_dias : int,
                    check_in_elegido : str):
    
    if estrellas == 5:
        return recomendar_cinco_estrellas(presupuesto, motivo_viaje, ubicacion, numero_huespedes, check_in_elegido, hotel_uno= "Hotel uno", hotel_dos= "Hotel dos", hotel_tres="Hotel tres")
    
    if estrellas == 4:
        return recomendar_cuatro_estrellas(presupuesto, motivo_viaje, ubicacion, categoria, numero_huespedes, numero_dias, check_in_elegido, hotel_cuatro="Hotel cuatro", hotel_cinco="Hotel cinco")

    if estrellas == 3:
        return recomendar_tres_estrellas(presupuesto, motivo_viaje, ubicacion, categoria, numero_huespedes, numero_dias, check_in_elegido, hotel_seis="Hotel seis", hotel_siete="Hotel siete", hotel_ocho="Hotel ocho")
    
    if estrellas == 2:
        return recomendar_dos_estrellas(presupuesto, motivo_viaje, ubicacion, categoria, numero_huespedes, numero_dias, check_in_elegido, hotel_nueve="Hotel nueve", hotel_diez="Hotel diez")
    
    if estrellas == 1:
        return recomendar_una_estrella(presupuesto, motivo_viaje, ubicacion, numero_huespedes, numero_dias, check_in_elegido, hotel_once="Hotel once", hotel_doce="Hotel doce", hotel_trece="Hotel trece")

def ingresar_recomendacion () -> None:

    print("🛎️¡Bienvenido a nuestro sistema de recomendación hotelera!🛎️")
    print("Por favor complete los siguientes datos para iniciar la recomendación✍🏻: ")


    nombre = validar_str(pedir_str("Ingrese su nombre para la recomendación: "))
    print()
    mostrar_dato("El nombre ingresado es:", nombre)

    apellido = validar_str(pedir_str("Ingrese su apellido: "))
    print()
    mostrar_dato("El apellido ingresado es:", apellido)


    motivo_viaje = validar_motivo_viaje(pedir_str("Ingrese su motivo de viaje (trabajo/vacaciones): "), "trabajo", "vacaciones", None, "Error. Ingrese un motivo de viaje válido: ")
    print()
    mostrar_dato("El motivo de viaje ingresado es:", motivo_viaje)


    ubicacion = validar_motivo_viaje(pedir_str("Ingrese la ubicación del hotel (norte/sur/centro): "), "norte", "sur", "centro", "Error. Ingrese una ubicación válida: ")
    print()
    mostrar_dato("La ubicación ingresada es:", ubicacion)


    categoria = validar_motivo_viaje(pedir_str("Ingrese la categoría de hotel que desee (all inclusive, media pensión, solo alojamiento): "), "all inclusive", "media pension", "solo alojamiento", "Error. Ingrese una categoría válida: ")
    print()
    mostrar_dato("La categoría ingresada es:", categoria)


    estrellas = validar_estrellas(validar_int(pedir_int("Ingrese la cantidad de estrellas del hotel (1/5): ")))
    print()
    mostrar_dato("El número de estrellas ingresado es:", estrellas)


    presupuesto = validar_presupuesto(pedir_int("Ingrese su presupuesto de viaje: "))
    print()
    mostrar_dato("El presupuesto ingresado es:", presupuesto)


    numero_huespedes = validar_huespedes_dias(pedir_int("Ingrese la cantidad de huéspedes: "))
    print()
    mostrar_dato("La cantidad de huéspedes ingresada es:", numero_huespedes)


    numero_dias = validar_huespedes_dias(pedir_int("Ingrese la cantidad de días a hospedarse: "))
    print()
    mostrar_dato("La cantidad de días a hospedarse ingresados es de:", numero_dias)


    # if motivo_viaje == "trabajo":
    mostrar_menu_check_in()
    check_in_elegido = seleccionar_check_in("Ingrese el horario en que desee: ", "Error. Debe ingresar alguna de las dos opciones.")
    print()
    mostrar_dato("El check-in elegido es:", check_in_elegido)

    

    hotel_recomendado = recomendar_hotel(estrellas, presupuesto, motivo_viaje,ubicacion, categoria, numero_huespedes, numero_dias, check_in_elegido)

    mostrar_recomendacion(hotel_recomendado, nombre, apellido, presupuesto, estrellas, motivo_viaje, check_in_elegido)







ingresar_recomendacion()

