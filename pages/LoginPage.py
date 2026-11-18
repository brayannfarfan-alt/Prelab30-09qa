from selenium.webdriver.common.by import By


apellido = "" 



# CREO LA CLASE LOGINPAGE
class LoginPage:


    def __init__(self, driver):
        self.driver = driver


        # LOCALIZADORES
        self.username = (By.ID, "user-name") #ESTRUCTURA DE DATOS: TUPLA. 
        self.password = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.CSS_SELECTOR , "[data-test='error']")
        # login_button = 'login_button'

    def ingresar_Usuario(self, usuario):
        self.driver.find_element(
            *self.username
        ).send_keys(usuario)


    def ingresar_password(self, password):
        self.driver.find_element(
                    *self.password
        ).send_keys(password)

    def presionar_login(self):
        self.driver.find_element(
            *self.login_button
        ).click()

    def hacer_login(self, usuario, password ):
        self.ingresar_Usuario(usuario)
        self.ingresar_password(password)
        
        self.driver.find_element(
            *self.login_button
            # By.ID => como buscar , que buscar
        ).click()

    def obtener_mensaje_error(self):
        return self.driver.find_element(*self.error_message).text









