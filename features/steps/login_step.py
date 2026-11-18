from behave import given, when, then


from pages.LoginPage import LoginPage
from pages.InventoryPage import InventoryPage

@given("que estoy en la pagina de login")
def step_abrir_login(context):


    context.driver.get("https://www.saucedemo.com/")
    context.login_page = LoginPage(context.driver)

@when('ingreso el usuario "{usuario}"')
def step_ingresar_usuario(context, usuario):

    context.login_page.ingresar_Usuario(usuario)

@when('ingreso la contraseña "{password}"')
def step_ingresar_password(context, password):

    context.login_page.ingresar_password(password)

@when("ingreso las siguientes credenciales:")
def step_ingresar_credenciales(context):

    credenciales = context.table[0]

    usuario = credenciales["usuario"]
    password = credenciales["password"]

    context.login_page.hacer_login(usuario, password)


@when("presiono el boton Login")
def step_presionar_login(context):

    context.login_page.presionar_login()

@then("debo visualizar la pagina de productos")
def step_validar_productos(context):

    context.inventory_page = InventoryPage(context.driver)


    assert "inventory.html" in context.driver.current_url
    assert context.inventory_page.obtener_logo() == "Swag Labs"

@then("debo visualizar un mensaje de error")
def step_validar_error(context):

    mensaje = context.login_page.obtener_mensaje_error()

    assert mensaje in "Epic sadface: Username and password do not match any user in this service"


