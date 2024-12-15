from src.webdriver import Webdriver
from src.hoc.welcome import Welcome
from fake_useragent import UserAgent
from rich.console import Console
import os

if __name__ == "__main__":
    Welcome().send_welcome()

    url = Console().input("[bold white on red]Enter the url: [/bold white on red]")
    num = Console().input("[bold white on red]Enter the number of channels (the parser may find more): [/bold white on red]")

    if os.name == 'nt':
       os.system('cls')
    else:
        os.system('clear')

    Webdriver(
        url=url,
        num= int(num),
        options_array=[
            "--disable-blink-features=AutomationControlled",
            f"user-agent={UserAgent().random}",
            "--start-maximized",
            "--log-level=3",
            "--mute-audio",
            "--headless"
        ]
    ).launch_webdriver_process()