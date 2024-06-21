# Aquí escribimos el decorador y los generadores de tiquetes"""

def generador_perfumeria():
    # Generamos turnos para el departamento de perfumeria
    turno = 0

    while turno >= 0:
        turno += 1
        yield f"P-{turno}"


def generador_farmacia():
    # Generamos turnos para el departamento de farmacia
    turno = 0

    while turno >= 0:
        turno += 1
        yield f"F-{turno}"


def generador_cosmeticos():
    # Generamos turnos para el departamento de cosmeticos
    turno = 0

    while turno >= 0:
        turno += 1
        yield f"C-{turno}"


def mensaje_turno(msg_turno):
    # Agregamos un mensaje al principio y al final del turno generado
    # usando un decorador
    def turno_generado():
        return f"""
            Su turno es:
            {msg_turno}
            Aguarde y sera atendido
        """

    return turno_generado


