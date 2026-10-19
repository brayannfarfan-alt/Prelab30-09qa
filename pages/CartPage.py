from selenium.webdriver.common.by import By


class CartPage:
    """
    Page Object de la página del carrito.
    """

    def __init__(self, driver):

        # Guardamos el driver
        self.driver = driver

        # -------------------------------------------------
        # LOCALIZADORES
        # -------------------------------------------------

        self.producto = (
            By.CLASS_NAME,
            "inventory_item_name"
        )

    # -----------------------------------------------------
    # PRODUCTOS
    # -----------------------------------------------------

    def obtener_nombre_producto(self):
        """
        Devuelve el nombre del producto
        que aparece en el carrito.
        """

        return self.driver.find_element(
            *self.producto
        ).text