from rich.console import Console
from rich.align import Align
from rich.padding import Padding
from rich.panel import Panel
import pyfiglet
import os

class Welcome:
    def __init__(self) -> None:
        self.console = Console()

    def send_welcome(self) -> None:
        figlet_text = pyfiglet.figlet_format("YOUTUBE-PARSER", font="bloody")
        panel = Panel(figlet_text, style="red")

        vertical_padding = (self.console.size.height - figlet_text.count("\n")) // 2
        padded_panel = Padding(panel, (vertical_padding, 0))
        aligned_panel = Align.center(padded_panel)

        self.console.print(aligned_panel)