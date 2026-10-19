from selenium.webdriver.common.by import By


class InventoryPage:
    """
    Page Object de la página de inventario.

    Contiene:
    - Localizadores de los elementos.
    - Acciones relacionadas con los productos.
    - Acciones relacionadas con el carrito.
    """

    def __init__(self, driver):

        # Guardamos el driver
        self.driver = driver

        # -------------------------------------------------
        # LOCALIZADORES
        # -------------------------------------------------

        # Logo "Swag Labs"
        self.logo = (
            By.CLASS_NAME,
            "app_logo"
        )

        # Título "Products"
        self.page_title = (
            By.CLASS_NAME,
            "title"
        )

        # Lista de productos
        self.productos = (
            By.CLASS_NAME,
            "inventory_item"
        )

        # Botón del menú
        self.menu_button = (
            By.ID,
            "react-burger-menu-btn"
        )

        # Filtro de productos
        self.filter_dropdown = (
            By.CLASS_NAME,
            "product_sort_container"
        )

        # Link del carrito
        self.cart_link = (
            By.CLASS_NAME,
            "shopping_cart_link"
        )

        # Contador del carrito
        self.cart_badge = (
            By.CLASS_NAME,
            "shopping_cart_badge"
        )

    # -----------------------------------------------------
    # INFORMACIÓN DE LA PÁGINA
    # -----------------------------------------------------

    def obtener_logo(self):
        """
        Devuelve el texto del logo.
        """

        return self.driver.find_element(
            *self.logo
        ).text

    def obtener_titulo(self):
        """
        Devuelve el título de la sección.
        """

        return self.driver.find_element(
            *self.page_title
        ).text

    # -----------------------------------------------------
    # PRODUCTOS
    # -----------------------------------------------------

    def obtener_productos(self):
        """
        Devuelve todos los productos encontrados.
        """

        return self.driver.find_elements(
            *self.productos
        )

    def obtener_primer_producto(self):
        """
        Devuelve el primer producto de la lista.
        """

        productos = self.obtener_productos()

        return productos[0]

    def obtener_nombre_primer_producto(self):
        """
        Obtiene el nombre del primer producto.
        """

        primer_producto = self.obtener_primer_producto()

        return primer_producto.find_element(
            By.CLASS_NAME,
            "inventory_item_name"
        ).text

    # -----------------------------------------------------
    # AGREGAR PRODUCTO
    # -----------------------------------------------------

    def agregar_primer_producto(self):
        """
        Agrega el primer producto al carrito.

        Devuelve el botón para poder comprobar
        posteriormente que cambió a "Remove".
        """

        # Obtener primer producto
        primer_producto = self.obtener_primer_producto()

        # Buscar botón dentro del producto
        boton = primer_producto.find_element(
            By.TAG_NAME,
            "button"
        )

        # Hacer click
        boton.click()

        # Devolver botón
        return boton

    # -----------------------------------------------------
    # ELEMENTOS DE INTERFAZ
    # -----------------------------------------------------

    def menu_visible(self):
        """
        Comprueba si el botón del menú está visible.
        """

        return self.driver.find_element(
            *self.menu_button
        ).is_displayed()

    def filtro_visible(self):
        """
        Comprueba si el filtro está visible.
        """

        return self.driver.find_element(
            *self.filter_dropdown
        ).is_displayed()

    # -----------------------------------------------------
    # CARRITO
    # -----------------------------------------------------

    def obtener_contador_carrito(self):
        """
        Devuelve el número mostrado en el carrito.
        """

        return self.driver.find_element(
            *self.cart_badge
        ).text

    def abrir_carrito(self):
        """
        Hace click en el carrito.
        """

        self.driver.find_element(
            *self.cart_link
        ).click()