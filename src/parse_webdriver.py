from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from rich.console import Console
from src.hoc.window import Window
from src.hoc.channels import Channel, Channels
from rich.progress import track
from datetime import datetime

class ParseWebdriver:
    def __init__(self, driver, console, num) -> None:
        self.driver: Chrome = driver
        self.console: Console = console
        self.channels = None

        self.num = num
        self.content_section = []
        self.channel_href_list = []
        self.output = []

    def launch_webdriver_parse_contents(self) -> None:
        try:
            WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.TAG_NAME, "body")))

            ytd_app = self.driver.find_element(By.TAG_NAME, "ytd-app").find_element(By.ID, "contents")
            self.content_section = ytd_app.find_elements(By.ID, "content-section")
        except Exception:
            self.console.print_exception()
        finally:
            pass

    def launch_webdriver_parse_link(self) -> None:
        try:
            for content in track(self.content_section, description="Processing"):
                href = content.find_element(By.ID, "main-link").get_attribute("href")

                if href not in self.channel_href_list:
                    self.channel_href_list.append(href)
                    Window(driver=self.driver, url=href, console=self.console, function=self.launch_webdriver_find_info).change_window()

        except Exception:
            self.console.print_exception()
        finally:
            pass

    def launch_webdriver_find_info(self) -> None:
        try:
            info_contents = self.driver.find_element(By.TAG_NAME, "yt-content-metadata-view-model").text
            channel_info = str("".join(str(info_contents).split("\n"))).split("•")

            channel = Channel(channel_info[0], channel_info[1], channel_info[2])
            self.channels.add_channel(channel=channel)
        except Exception:
            pass

    def create_output_logs(self) -> None:
        with open(f'output/log[{" ".join(datetime.utcnow().strftime("%Y-%m-%d %H-%M-%S").split(" "))}].txt', "w", encoding="utf-8") as file:
            string = []
            [(lambda channel: string.append(f"{channel.name} | {channel.subs} | {channel.videos}"))(channel) for channel in self.output]

            file.write("\n".join(string))

    def launch_webdriver_process(self) -> None:
        i = 1
        while len(self.channel_href_list) < self.num:
            self.channels = Channels(i, self.output)

            self.launch_webdriver_parse_contents()
            self.launch_webdriver_parse_link()

            self.channels.return_channel_list()

            WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.TAG_NAME, "body")))
            [(lambda _: self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN))(i) for i in range(1, 20)]
            WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.TAG_NAME, "body")))

            i += 1

        self.create_output_logs()
