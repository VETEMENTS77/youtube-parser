from rich.panel import Panel
from rich.console import Console

class Channel:
    def __init__(self, name, subs, videos) -> None:
        self.name = name
        self.subs = subs
        self.videos = videos

class Channels:
    def __init__(self, num) -> None:
        self.channel_list = []

        self.num = num
        self.console = Console()

    def add_channel(self, channel: Channel) -> None:
        self.channel_list.append(channel)

    def return_channel_list(self) -> list:
        string = []

        [(lambda channel: string.append(f"{channel.name} | {channel.subs} | {channel.videos}"))(channel) for channel in self.channel_list]

        self.console.print(
            Panel(
            "\n".join(string),
            title=f"[blue]page: {self.num} | channels: {int(len(string))}[/blue]",
            title_align="center",
            border_style="red",
            highlight=True,
            style="green"
        ))
