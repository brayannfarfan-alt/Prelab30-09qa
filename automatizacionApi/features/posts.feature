@api @posts
Feature: Gestion de Posts en JSONPlaceholder
    Background:
        Given que el servicio de Posts esta disponible

    @smoke
    Scenario: Consultar un post existente por ID
        When consulto el post con id "1"
        Then  el codigo de estado de la respuesta debe ser 200
        And el campo "id" de la repsuesta debe ser 1
        And la respuesta debe contener el campo "title"


    Scenario: Crear un nuevo posts exitosamente
        When envio una peticion para crear un post  con los datos:
            | title       | body  | user_id |
            | Prueba behave |Automatizacion APIS | 1
        

