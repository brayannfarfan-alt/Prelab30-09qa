import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




from pages.LoginPage import LoginPage



# import time #MALA PRACTICA....


@pytest.fixture(scope='module')
def driver():
    service = Service(ChromeDriverManager().install())
    options = Options()

     # Evita algunos avisos/intervenciones de Chrome
    #  https://www.selenium.dev/documentation/webdriver/drivers/options/
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-infobars")



    driver = webdriver.Chrome(service=service, options=options)


    driver.implicitly_wait(10)

    yield driver 

    driver.quit()



def test_01_login(driver):

    # CREAR UN OBJETO
    login = LoginPage(driver)

    # login.ingresar_password()

    driver.get("https://www.saucedemo.com/")

    login.hacer_login("standard_user","secret_sauce")

    WebDriverWait(driver,10).until(
        EC.url_contains('inventory.html')
    )

    assert "/inventory.html" in driver.current_url , "ERROR: No se redirigió a /inventory.html"
