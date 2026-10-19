import pytest
from pathlib import Path
# import glob
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data.datos import datos_login

from pages.LoginPage import LoginPage
# from pages.InventoryPage import InventoryPage

RUTA_CSV = (
    Path(__file__).resolve()
    / "data"
    / "usuarios.csv"
)

def leeer_datos_csv():

    open()


# RUTA_JSON = (
#     Path(__file__).resolve().parents[1]
#     / "data"
#     / "usuarios.json"
# )









@pytest.mark.parametrize("usuario,password", datos_login)
def test_01_login(driver,usuario,password):

    # CREAR UN OBJETO
    login = LoginPage(driver)

    # login.ingresar_password()

    driver.get("https://www.saucedemo.com/")

    login.hacer_login(usuario, password)
    
    WebDriverWait(driver,10).until(
        EC.url_contains('inventory.html')
    )

    assert "/inventory.html" in driver.current_url , "ERROR: No se redirigió a /inventory.html"



# def test_logo_inventario( driver ):

#     login = LoginPage(driver)
#     inventory = InventoryPage(driver)

#     driver.get("https://www.saucedemo.com/")

#     login.hacer_login("standard_user","secret_sauce")

#     assert inventory.obtener_logo() == 'Swag Labs'

#     # inventario_texto = inventory.obtener_logo()

#     # assert inventario_texto == 'Swag Labs'
