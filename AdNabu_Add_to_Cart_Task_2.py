from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AdNabuEcommerceAutomation:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 15)

    def open_website(self, url):
        self.driver.get(url)

    def login_website(self, enter_password):


        password_box = self.wait.until(
            EC.visibility_of_element_located((By.ID, "password"))
        )

        password_box.clear()
        password_box.send_keys(enter_password)


        enter_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//button[@type="submit"]')
            )
        )

        enter_button.click()

    def search_product(self, product_name):


        search_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//details-modal//summary")
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            search_button
        )


        search_box = self.wait.until(
            EC.visibility_of_element_located(
                (By.ID, "Search-In-Modal")
            )
        )

        search_box.clear()
        search_box.send_keys(product_name)
        search_box.send_keys(Keys.RETURN)

    def select_product(self):


        target_product = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//div[@id="product-grid"]/ul/li[3]')
            )
        )

        target_product.click()

    def add_product_to_cart(self):


        add_to_cart_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.NAME, "add")
            )
        )

        add_to_cart_button.click()

    def verify_product_added(self):


        cart_count = self.wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "cart-count-bubble")
            )
        )

        print("Test Case Passed: Product added to cart successfully")

    def close_browser(self):
        input("Press Enter to close browser...")
        self.driver.quit()


if __name__ == "__main__":

    test = AdNabuEcommerceAutomation()

    try:
        # Open website
        test.open_website(
            "https://adnabu-store-assignment1.myshopify.com"
        )

        # Login with password
        test.login_website("AdNabuQA")

        # Search product
        test.search_product("snowboard")

        # Select product
        test.select_product()

        # Add to cart
        test.add_product_to_cart()

        # Verify product added
        test.verify_product_added()

    except Exception as e:
        print(f"Test Failed - failed due to : {e}")

    finally:
        test.close_browser()