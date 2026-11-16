import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from pathlib import Path
import re
import base64
import pytest_html


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
    driver.save_screenshot()
    driver.quit()




def pytest_html_report_title(report):
    report.title = "Reporte de Automatizacion - Sauce Demo"



import pytest
import pytest_html

from pathlib import Path
import re
import base64


# Personalizar el título del reporte HTML
def pytest_html_report_title(report):
    report.title = "Reporte de Automatización - Sauce Demo"





import pytest
import re
import base64
from pathlib import Path


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    resultado = yield
    reporte = resultado.get_result()

    if reporte.when == "call" and reporte.failed:

        driver = item.funcargs.get("driver")

        if driver:
            carpeta = Path("reports/screenshots")
            carpeta.mkdir(parents=True, exist_ok=True)

            nombre = re.sub(
                r"[^a-zA-Z0-9_-]",
                "_",
                item.nodeid
            )

            ruta_captura = carpeta / f"{nombre}.png"

            captura = driver.save_screenshot(str(ruta_captura))

            if captura:
                imagen_base64 = base64.b64encode(
                    ruta_captura.read_bytes()
                ).decode("utf-8")

                extras = getattr(reporte, "extras", [])

                extras.append(
                    pytest_html.extras.png(
                        imagen_base64,
                        name="captura de error"
                    )
                )

                reporte.extras = extras  