from selenium.webdriver.common.by import By


class CheckoutPage:


    def __init__(self, driver):
    
            # Guardamos el driver
            self.driver = driver

            self.first_name = (
                  By.ID, 'first-name'
            )
            self.last_name = (
                  By.ID, 'last-name'
            )
            self.postal_code = (
                  By.ID, 'postal-code'
            )
            self.continue_button = (
                  By.ID, 'continue'
            )

    def ingesar_nombre(self, nombre):
          self.driver.find_element(
                *self.first_name
        ).send_keys(nombre)

    def ingesar_apellido(self,apellido):
          self.driver.find_element(
                *self.last_name
        ).send_keys(apellido)
          
    def ingesar_codigo_postal(self, codigo_postal): 
          self.driver.find_element(
                *self.postal_code
        ).send_keys(codigo_postal)


    def completar_datos(self, nombre, apellido,codigo_postal ):
          self.ingesar_nombre(nombre)
          self.ingesar_apellido(apellido)
          self.ingesar_codigo_postal(codigo_postal)


    def continuar(self):
        self.driver.find_element(
            *self.continue_button
        ).click()