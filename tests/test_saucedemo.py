import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.LoginPage import LoginPage
from pages.InventoryPage import InventoryPage
from pages.CartPage import CartPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    yield driver

    driver.quit()


@pytest.fixture
def login_exitoso(driver):
    login = LoginPage(driver)
    login.hacer_login("standard_user", "secret_sauce")

    WebDriverWait(driver, 10).until(
        EC.url_contains("inventory.html")
    )

    return driver


def test_login_exitoso(driver):
    login = LoginPage(driver)
    login.hacer_login("standard_user", "secret_sauce")

    WebDriverWait(driver, 10).until(
        EC.url_contains("inventory.html")
    )

    assert "inventory.html" in driver.current_url


def test_login_incorrecto(driver):
    login = LoginPage(driver)
    login.hacer_login("usuario_incorrecto", "clave_incorrecta")

    error = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "error-message-container")
        )
    )

    assert error.is_displayed()


def test_titulo_inventario(login_exitoso):
    inventario = InventoryPage(login_exitoso)

    assert inventario.obtener_titulo() == "Products"


def test_logo_inventario(login_exitoso):
    inventario = InventoryPage(login_exitoso)

    assert inventario.obtener_logo() == "Swag Labs"


def test_productos_visibles(login_exitoso):
    inventario = InventoryPage(login_exitoso)

    productos = inventario.obtener_productos()

    assert len(productos) > 0


def test_menu_visible(login_exitoso):
    inventario = InventoryPage(login_exitoso)

    assert inventario.menu_visible()


def test_filtro_visible(login_exitoso):
    inventario = InventoryPage(login_exitoso)

    assert inventario.filtro_visible()


def test_agregar_producto_al_carrito(login_exitoso):
    inventario = InventoryPage(login_exitoso)

    boton = inventario.agregar_primer_producto()

    WebDriverWait(login_exitoso, 10).until(
        lambda driver: boton.text == "Remove"
    )

    assert boton.text == "Remove"
    assert inventario.obtener_contador_carrito() == "1"


def test_producto_en_carrito(login_exitoso):
    inventario = InventoryPage(login_exitoso)

    nombre_producto = inventario.obtener_nombre_primer_producto()

    inventario.agregar_primer_producto()
    inventario.abrir_carrito()

    WebDriverWait(login_exitoso, 10).until(
        EC.url_contains("cart.html")
    )

    carrito = CartPage(login_exitoso)

    assert carrito.obtener_nombre_producto() == nombre_producto