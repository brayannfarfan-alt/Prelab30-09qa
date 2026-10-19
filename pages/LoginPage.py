from selenium.webdriver.common.by import By


class LoginPage:
    """
    Page Object de la página de Login.
    
    Aquí se encuentran:
    - Los localizadores de los elementos.
    - Las acciones relacionadas con el login.
    """

    def __init__(self, driver):
        # Guardamos el driver para poder utilizar Selenium
        self.driver = driver

        # -------------------------------------------------
        # LOCALIZADORES
        # -------------------------------------------------

        self.username = (By.ID, "user-name")

        self.password = (By.ID, "password")

        self.login_button = (By.ID, "login-button")

    # -----------------------------------------------------
    # ACCIONES
    # -----------------------------------------------------

    def ingresar_usuario(self, usuario):
        """Escribe el usuario en el campo correspondiente."""

        self.driver.find_element(
            *self.username
        ).send_keys(usuario)

    def ingresar_password(self, password):
        """Escribe la contraseña."""

        self.driver.find_element(
            *self.password
        ).send_keys(password)

    def hacer_login(self, usuario, password):
        """
        Realiza el proceso completo de login.
        """

        self.ingresar_usuario(usuario)

        self.ingresar_password(password)

        self.driver.find_element(
            *self.login_button
        ).click()