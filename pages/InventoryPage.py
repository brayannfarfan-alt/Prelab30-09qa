from selenium.webdriver.common.by import By




class InventoryPage:


    def __init__(self, driver):
        self.driver = driver


    # locatores

        self.logo = (By.CLASS_NAME, 'app_logo')



    def obtener_logo( self ):
        """
            Devuelve el texto del logo
        """
        return self.driver.find_element(
            *self.logo
        ).text

       


    # def obtener_logos(self):
    #     return self.driver.find_element(
    #         *self.logo
    #     )