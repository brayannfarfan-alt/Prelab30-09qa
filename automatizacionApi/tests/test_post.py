import pytest
from metodos_http import obtener_publicaciones, crear_publicacion , eliminar_publicacion ,obtener_endpoint_inexistente
from utils.helpers import logger
from validaciones import validacion

def test_obtener_publicaciones():
    logger.info("Inicianado la peticion GET")
    respuesta = obtener_publicaciones()

    #validar http
    # assert respuesta.status_code == 200
    validacion(respuesta,200)

    # validar estructura

    datos = respuesta.json()
    # print(type(datos))
    assert isinstance(datos,dict)

    assert "id" in datos
    assert "title" in datos
    assert "body" in datos


    assert datos["id"] == 1



def test_crear_publicacion():
    respuesta =  crear_publicacion()


    # assert respuesta.status_code == 201
    validacion(respuesta,201)

    datos = respuesta.json()


    assert datos["title"] == "Mi primera vez creando una publicacion"
    assert datos["body"] == "estoy aprendiendo APIS CON PYTHON Y REQUESTS"
    assert datos["userId"] == 1



def test_eliminar_publicacion():
    respuesta = eliminar_publicacion()


    validacion(respuesta, 200)

    datos = respuesta.json()

    assert isinstance(datos,dict)


def test_obtener_endpoint_inexistente():
    respuesta = obtener_endpoint_inexistente()

    validacion(respuesta,404)




