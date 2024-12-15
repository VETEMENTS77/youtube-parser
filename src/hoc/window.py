from selenium.webdriver import Chrome
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from rich.console import Console
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Window:
    def __init__(self, driver, url, console, function) -> None:
        self.driver: Chrome = driver
        self.url = url
        self.console: Console = console
        self.function = function

    def change_window(self) -> None:
        try:
            self.driver.execute_script(f"window.open('{self.url}');")
            self.driver.switch_to.window(self.driver.window_handles[1])

            WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.TAG_NAME, "body")))
            self.function()

            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

        except Exception:
            self.console.print_exception()
        finally:
            pass