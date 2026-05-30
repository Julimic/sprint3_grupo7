def mostrar_dato(mensaje : str
                , dato) -> None:
    
    print(f"{mensaje} {dato}")


def mostrar_menu_check_in():
    print("""
Check in disponibles:

- Express: 14hs
- Regular: 20hs
""")


def mostrar_recomendacion(hotel_recomendado : str,
                        nombre : str,
                        apellido : str,
                        presupuesto : int,
                        estrellas : int,
                        motivo_viaje : str,
                        check_in_elegido : str) -> str | None:

    print()
    print(f"Hola {nombre} {apellido}👋🏻")

    if hotel_recomendado != "":
        print(f"¡El {hotel_recomendado} 🏨 es ideal para ti esta semana!")
        print(f"Aunque hay opciones más económicas, es el que mejor se ajusta a tu presupuesto de 💸{presupuesto}.")
        print(f"Tiene una reseña de {estrellas} estrellas⭐.")

        if motivo_viaje == "trabajo":
            print("Este hotel cuenta con un espacio de coworking integrado💻.")
            print("Está a solo 15 minutos de la zona de oficinas🏢, ideal para tu trabajo.")
            print(f"Tu tipo de check-in es {check_in_elegido}, lo que te ahorrará tiempo de traslado🚗.")
        
        elif motivo_viaje == "vacaciones":
            print("Este cuenta con piscina👙 y restaurante🥐.")
            print("Se encuentra en el corazón de la zona turística📍, ideal para tus vacaciones🏖️.")
            print("Lo que te permitirá explorar la ciudad sin preocupaciones de traslado🚗.")

    else:
        print("Lamentablemente no encontramos hoteles que se ajusten exactamente a tus condiciones😥.")
        print("Te invitamos a revisar tu presupuesto, ubicación o preferencias de viaje para ampliar las opciones disponibles🤗.")

    print()




