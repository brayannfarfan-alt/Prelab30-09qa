@login
Feature: Inicio de sesión saucedemo

    Background: 
        Given que estoy en la pagina de login

    @smoke
    Scenario: Login 
        When ingreso las siguientes credenciales:
            | usuario       | password     |
            | standard_user | secret_sauce |
        Then debo visualizar la pagina de productos

    @regression
    Scenario: Login con usuario incorrecto

        When ingreso el usuario "<usuario>"
        And ingreso la contraseña "<password>"
        And presiono el boton Login
        Then debo visualizar un mensaje de error


        Example:
            | usuario              | password       |
            | usuario_incorrecto   | secret_sauce   |
            | standard_user        | clave_incorrecta |
            | usuario_prueba       | clave_prueba   |