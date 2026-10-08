from selenium.webdriver.common.by import By

# CREO LA CLASE LOGINPAGE
class LoginPage:


    def __init__(self, driver):
        self.driver = driver


        # LOCALIZADORES
        self.username = (By.ID, "user-name") #ESTRUCTURA DE DATOS: TUPLA. 
        self.password = (By.ID, "password")
        self.login_button = (By.ID, "login-button")


    def ingresar_Usuario(self, usuario):
        self.driver.find_element(
            *self.username
        ).send_keys(usuario)


    def ingresar_password(self, password):
        self.driver.find_element(
                    *self.password
        ).send_keys(password)


    def hacer_login(self, usuario, password ):
        self.ingresar_Usuario(usuario)
        self.ingresar_password(password)
        
        self.driver.find_element(
            *self.login_button
        ).click()