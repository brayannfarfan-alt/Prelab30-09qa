import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


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
