import sys
from util import *
from rich.console import Console
from rich import print
from rich.layout import Layout
from rich.align import Align
from rich.panel import Panel
from rich.live import Live

class Interface:
    def __init__(self):
        self.console = Console()
        self.live = Live(refresh_per_second=5, screen=True)

    def start(self, focus_time=None, break_time=None):
        """
        Rozpoczyna sesję Pomodoro.
        Naciśnij enter aby rozpocząć, lub podaj parametry jeśli nie podano ich jako flagę.
        Podaj długość czasu skupienia i przerwy jeśli nie zostały podane.
        """


        start_layout = Layout()
        start_layout.split_column(
            Layout(Align.center("[purple]WELCOME TO CLI POMODORO TIMER![/]", vertical="bottom")),
            Layout(Align.center("[purple]PRESS ENTER TO START[/]", vertical="top"))
        )

        start_panel = Panel(
                start_layout,
                title="Pomodoro Timer",
                title_align="right",
                border_style="green on red",
                expand=True,
                height=self.console.height,
                width=self.console.width
            )  

        with self.live:
            self.live.update(start_panel) 
            input()  

        return focus_time, break_time

    def wait(self, time, type):
        """Ekran czekania."""
        pass

    def ring(self, type):
        """Ekran z informacją o zakończeniu."""
        pass

    def end(self):
        """Ekran końcowy."""
        sys.exit()

    def error(self, e):
        """Służy aby poprosić użytkownika o ponowne wprowadzenie danych w wypadku wystąpienia błędu."""
        input(f"Error: {e}")

    def critical_error(self, e):
        """Zamyka program w przypadku błędu krytycznego."""
        input(f"Error: {e}\nPress enter to close program")
        sys.exit()