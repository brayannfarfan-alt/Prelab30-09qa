import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# @pytest.fixture define una función setup/teardown reutilizable para los tests
@pytest.fixture
def driver():
    # ChromeDriverManager().install() descarga e instala automáticamente la versión
    # del ChromeDriver correspondiente a tu navegador Chrome instalado
    service = Service(ChromeDriverManager().install())
    
    # Creamos un objeto de opciones para configurar el comportamiento inicial del navegador
    options = webdriver.ChromeOptions()
    # Le indicamos a Chrome que se abra maximizado en toda la pantalla
    options.add_argument("--start-maximized")
    
    # Instanciamos el navegador Chrome pasando el servicio y las opciones
    # Nota: No se agrega implicitly_wait para manejar la sincronización manualmente
    driver = webdriver.Chrome(service=service, options=options)
    
    # 'yield' entrega la instancia del navegador (driver) al test que lo haya solicitado
    # El test se ejecuta en este punto.
    yield driver
    
    # TEARDOWN: Todo el código después del 'yield' se ejecuta al finalizar el test
    # .quit() cierra todas las ventanas del navegador y finaliza el proceso del driver
    driver.quit()