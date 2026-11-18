



def validacion(respuesta,status_code):
    assert respuesta.status_code == status_code,(
        f"Se esperaba el codido http:{status_code},"
        f"peeero, se recibió {respuesta.status_code}"
    )