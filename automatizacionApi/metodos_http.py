import requests



URL= 'https://jsonplaceholder.typicode.com/posts'

def obtener_publicaciones():
    return requests.get(f"{URL}/1")



def crear_publicacion():
    datos ={
        "title": "Mi primera vez creando una publicacion",
        "body": "estoy aprendiendo APIS CON PYTHON Y REQUESTS",
        "userId": 1
    }

    respuesta = requests.post(URL,json=datos)


    return respuesta




def eliminar_publicacion():
    return requests.delete(f"{URL}/1")


def obtener_endpoint_inexistente():
    return requests.get(f"{URL}/endpoint_inexistente")