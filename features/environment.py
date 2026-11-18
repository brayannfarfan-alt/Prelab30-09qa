from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options




def before_scenario( context , scenario):
    service = Service(ChromeDriverManager().install())
    options = Options()

    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-infobars")



    context.driver = webdriver.Chrome(service=service, options=options)
    context.driver.implicitly_wait(10)


def after_scenario( context, scenario ):
    context.driver.quit()