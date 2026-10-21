from selenium.webdriver.common.by import By




class CheckoutOverview:
    def __init__(self, driver):
        
                # Guardamos el driver
                self.driver = driver

                self.finish_button = (By.ID, 'finish')
                self.confirmacion = (By.CLASS_NAME, 'complete-header')


    def finalizar_compra(self):
            self.driver.find_element(
                    *self.finish_button
        )

    def obtener_confimacion(self):
        return self.driver.find_element(
               *self.confirmacion
        ).text