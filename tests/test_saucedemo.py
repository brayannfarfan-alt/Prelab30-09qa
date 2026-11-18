import pytest
from pathlib import Path
import csv 
import json
# import glob
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data.datos import datos_login

from pages.LoginPage import LoginPage
# from pages.InventoryPage import InventoryPage

from utils.helpers import logger

RUTA_CSV = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "usuarios.csv"
)

def leeer_datos_csv():
    datos = []
    with open(RUTA_CSV, mode='r', encoding='utf-8', newline='') as archivo:
        leer = csv.DictReader(archivo)

        for fila in leer :
            usuario = fila['usuario']
            password = fila['password']

            datos.append((usuario,password))
    return datos

RUTA_JSON = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "usuarios.json"
)


def leeer_datos_json():
    datos = []
    with open(RUTA_CSV, mode='r', encoding='utf-8', newline='') as archivo:
        leer = json.load(archivo)

        for fila in leer :
            usuario = fila['usuario']
            password = fila['password']

            datos.append((usuario,password))
    return datos





@pytest.mark.parametrize("usuario,password", datos_login)
def test_01_login(driver,usuario,password):
    logger.info("Iniciando login con usuario: %s")
    # CREAR UN OBJETO
    login = LoginPage(driver)

    # login.ingresar_password()

    driver.get("https://www.saucedemo.com/")
    logger.info("Completando credenciales.....")

    login.hacer_login(usuario, password)
    
    WebDriverWait(driver,10).until(
        EC.url_contains('inventory.html')
    )
    logger.info("verificando redireccion exitosa")
    assert "/inventory.html" in driver.current_url , "ERROR: No se redirigió a /inventory.html"



# def test_logo_inventario( driver ):

#     login = LoginPage(driver)
#     inventory = InventoryPage(driver)

#     driver.get("https://www.saucedemo.com/")

#     login.hacer_login("standard_user","secret_sauce")

#     assert inventory.obtener_logo() == 'Swag Labs'

#     # inventario_texto = inventory.obtener_logo()

#     # assert inventario_texto == 'Swag Labs'
