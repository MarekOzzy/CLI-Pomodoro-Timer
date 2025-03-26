import sys
from time import sleep
from util import *
from rich.console import Console
from rich.progress import Progress
from rich.layout import Layout
from rich.align import Align
from rich.panel import Panel
from rich.live import Live
import asyncio

class Interface:
    def __init__(self):
        self.console = Console()
        self.live = Live(refresh_per_second=5, screen=True)

    def create_panel(self, 
                     layout, 
                     title="[green on red]POMODORO TIMER[/]", 
                     title_align="left", 
                     border_style="red",
                     ):
        """Tworzy obiekt panel, który pozwoli na dynamiczne zmienianie wielkości okna"""
        return Panel(
            layout,
            title=title,
            title_align=title_align,
            border_style=border_style,
            expand=True,
            height=self.console.height,
            width=self.console.width
        )

    def wait_for_enter(self):
        input()
        self.waiting_for_input = False

    def start(self):
        """Rozpoczyna sesję Pomodoro. Naciśnij enter aby rozpocząć"""
        layout = Layout()
        layout.split_column(
            Layout(Align.center("[green]WELCOME TO CLI POMODORO TIMER![/green]", vertical="bottom")),
            Layout(Align.center("[red]PRESS ENTER TO START[/]", vertical="top"))
        )


        # STARA WERSJA KODU BEZ TRHEADINGU
        # with self.live:
        #     self.live.update(self.create_panel(layout=layout,border_style="black on red"))
        #     input()

    def wait(self, time, type):
        """Ekran czekania."""
        progress = Progress()
        if type == 'focus':
            task = progress.add_task("time left: ", total=time)
        
            wait_layout = Layout()

            wait_layout.split_column(
                Layout(Align.center("[red]FOCUS[/red]", vertical="bottom")),
                Layout(Align.center(progress, vertical="top"))
            )
            wait_panel = Panel(
                wait_layout,
                title="[green on red]POMODORO TIMER[/]",
                title_align="right",
                border_style="red",
                expand=True,
                height=self.console.height,
                width=self.console.width
            )
            
        else:
            task = progress.add_task("time left: ", total=time)
        
            wait_layout = Layout()

            wait_layout.split_column(
                Layout(Align.center("[red]BREAK[/red]", vertical="bottom")),
                Layout(Align.center(progress, vertical="top"))
            )
            wait_panel = Panel(
                wait_layout,
                title="[green on red]POMODORO TIMER[/]",
                title_align="right",
                border_style="red",
                expand=True,
                height=self.console.height,
                width=self.console.width
            )   

        with self.live:
            for _ in range(time):
                self.live.update(wait_panel)
                progress.update(task, advance=1)
                sleep(1)

    def ring(self, type):
        """Ekran z informacją o zakończeniu."""
        if type == 'focus':        
            wait_layout = Layout()

            wait_layout.split_column(
                Layout(Align.center("[red]FOCUS[/red]", vertical="bottom")),
                Layout(Align.center("", vertical="top"))
            )
            wait_panel = Panel(
                wait_layout,
                title="[green on red]POMODORO TIMER[/]",
                title_align="right",
                border_style="red",
                expand=True,
                height=self.console.height,
                width=self.console.width
            )
            
        else:        
            wait_layout = Layout()

            wait_layout.split_column(
                Layout(Align.center("[red]BREAK[/red]", vertical="bottom")),
                Layout(Align.center("", vertical="top"))
            )
            wait_panel = Panel(
                wait_layout,
                title="[green on red]POMODORO TIMER[/]",
                title_align="right",
                border_style="red",
                expand=True,
                height=self.console.height,
                width=self.console.width
            )   

        with self.live:
            self.live.update(wait_panel)

    def end(self):
        """Ekran końcowy."""
        sys.exit()

    def error(self, e):
        """Służy aby poprosić użytkownika o ponowne wprowadzenie danych w wypadku wystąpienia błędu."""
        error_layout = Layout()
        error_layout.split_column(
            Layout(Align.center(f"ERROR: {e}", vertical= "middle"))
        )
        error_panel = Panel(
            error_layout,
            title='ERROR',
            title_align='center',
            border_style=" black on red",
            subtitle='ERROR',
            expand=True,
            height=self.console.height,
            width=self.console.width
        )
        
        with self.live:
            self.live.update(error_panel)
        input()

    def critical_error(self, e):
        """Zamyka program w przypadku błędu krytycznego."""
        critical_error_layout = Layout()
        critical_error_layout.split_column(
            Layout(Align.center(f"ERROR: {e}", vertical= "middle"))
        )
        critical_error_panel = Panel(
            critical_error_layout,
            title='[black on purple]CRITICAL ERROR[/]',
            title_align='center',
            border_style=" purple on red",
            subtitle='[black on purple]CRITICAL ERROR[/]',
            expand=True,
            height=self.console.height,
            width=self.console.width
        )
        
        with self.live:
            self.live.update(critical_error_panel)
        input()
        sys.exit()