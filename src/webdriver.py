from selenium import webdriver
from rich.console import Console
from colorama import Back, Style
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from src.parse_webdriver import ParseWebdriver

class Webdriver:
    def __init__(self, url, options_array, num) -> None:
        self.url = url
        self.num = num
        self.options_array = options_array

        self.options = webdriver.ChromeOptions()
        self.driver = None
        self.console = Console()
    def create_webdriver_service(self) -> None:
        [(lambda option: self.options.add_argument(option))(option) for option in self.options_array]
        self.driver = webdriver.Chrome(options=self.options)

    def launch_webdriver_driver(self) -> None:
        try:
            self.driver.get(self.url)
            WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.TAG_NAME, "body")))

            ParseWebdriver(driver=self.driver, console=self.console, num=self.num).launch_webdriver_process()
            self.console.input("[bold white on red]Press enter to exit...[/bold white on red]")
        except Exception:
            self.console.print_exception()
        finally:
            self.driver.close()
            self.driver.quit()
    
    def launch_webdriver_process(self) -> None:
        self.create_webdriver_service()
        self.launch_webdriver_driver()