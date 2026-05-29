from main import *
from input import *

def mostrar_dato(mensaje : str
                , dato) -> None:
    
    print(f"{mensaje}: {dato}")

def mostrar_recomendacion(hotel_recomendado : str,
                        nombre : str,
                        apellido : str,
                        presupuesto : int,
                        estrellas : int,
                        motivo_viaje : str,
                        check_in_elegido : str):

    print()
    print(f"Hola {nombre} {apellido}ðŸ‘‹ðŸ»")

    if hotel_recomendado != "":
        print(f"Â¡El {hotel_recomendado} ðŸ¨ es ideal para ti esta semana!")
        print(f"Aunque hay opciones mÃ¡s econÃ³micas, es el que mejor se ajusta a tu presupuesto de ðŸ’¸{presupuesto}.")
        print(f"Tiene una reseÃ±a de {estrellas} estrellasâ­.")

        if motivo_viaje == "trabajo":
            print("Este hotel cuenta con un espacio de coworking integradoðŸ’».")
            print("EstÃ¡ a solo 15 minutos de la zona de oficinasðŸ¢, ideal para tu trabajo.")
            print(f"Tu tipo de check-in es {check_in_elegido}, lo que te ahorrarÃ¡ tiempo de trasladoðŸš—.")

        elif motivo_viaje == "vacaciones":
            print("Este cuenta con piscinaðŸ‘™ y restauranteðŸ¥.")
            print("Se encuentra en el corazÃ³n de la zona turÃ­sticaðŸ“, ideal para tus vacacionesðŸ–ï¸.")
            print("Lo que te permitirÃ¡ explorar la ciudad sin preocupaciones de trasladoðŸš—.")

    else:
        print("Lamentablemente no encontramos hoteles que se ajusten exactamente a tus condicionesðŸ˜¥.")
        print("Te invitamos a revisar tu presupuesto, ubicaciÃ³n o preferencias de viaje para ampliar las opciones disponiblesðŸ¤—.")

    print()

def mostrar_menu_check_in():
    print(('''
    Check in disponibles:

    -Express: 14hs
    -Regular: 20hs

    '''))



