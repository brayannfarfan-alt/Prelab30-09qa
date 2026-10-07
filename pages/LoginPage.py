from selenium.webdriver.common.by import By

class LoginPage:


    def __init__(self, driver):
        self.driver = driver



        self.username = (By.ID, "user-name")
        self.password = (By.ID, "password")
        self.login_button = (By.ID, "login-button")


    def ingresar_Usuario(self, usuario):


    def ingresar_password(self, password):