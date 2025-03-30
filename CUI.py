import sys
import threading
from time import sleep
from rich.console import Console
from rich.progress import Progress, BarColumn, TimeRemainingColumn
from rich.layout import Layout
from rich.align import Align
from rich.panel import Panel
from rich.live import Live
from util import *

class Interface:
    def __init__(self):
        self.console = Console()
        self.live = Live(refresh_per_second=5, screen=True)

    def create_panel(self, 
                     layout, 
                     border_style,
                     style='none',
                     subtitle=f"[red on black]{current_time()}[/]",
                     title="[green on black] POMODORO TIMER [/]",
                     title_align="center",
                     ):
        """Tworzy obiekt panel, który pozwoli na dynamiczne zmienianie wielkości okna"""
        return Panel(
            layout,
            title=title,
            title_align=title_align,
            border_style=border_style,
            style=style,
            subtitle=subtitle,
            subtitle_align="center",
            expand=True,
            height=self.console.height,
            width=self.console.width
        )

    def wait_for_enter(self):
        """Funkcja która służy do "Czekania na enter" """
        input()
        self.waiting_for_input = False

    def start(self):
        """Rozpoczyna sesję Pomodoro. Naciśnij enter aby rozpocząć"""
        layout = Layout()
        layout.split_column(
            Layout(Align.center("[green]WELCOME TO CLI POMODORO TIMER![/green]", vertical="bottom")),
            Layout(Align.center("[red]PRESS ENTER TO START[/]", vertical="top"))
        )

        with self.live:
            self.waiting_for_input = True
            # Uruchamiamy wątek który czeka aż użytkownik zmieni flagę na False
            input_thread = threading.Thread(target=self.wait_for_enter)
            input_thread.start()
            
            while self.waiting_for_input:
                self.live.update(self.create_panel(
                    layout=layout,
                    border_style='black on red',
                    subtitle=f"[red on black] {current_time()} [/]"
                ))
                sleep(0.2)

    def wait(self, time, type):
        """Ekran czekania."""
        bar_width = int(self.console.width * 0.4)
        progress = Progress(
            "[bold red]{task.percentage:>3.0f}% ",
            BarColumn(
                bar_width=bar_width,
                style="red",
                complete_style="green bold",
                finished_style="green bold",
                pulse_style="green"
            ),
            "[bold green]{task.fields[time_left]}[/]",  # Add custom field for time display
            expand=False,
            transient=True
        )
        
        task = progress.add_task(
            f"[bold yellow]{type.upper()} TIME REMAINING[/]", 
            total=time,
            completed=0,
            time_left="00:00"  # Initialize custom field
        )
        
        layout = Layout()
        layout.split_column(
            Layout(Align.center(f"[red]{type.upper()}TIME[/]", vertical="bottom")),
            Layout(Align.center(progress, vertical="top"))
        )
        
        with self.live:
            for i in range(time):
                remaining = time - i
                minutes = remaining // 60
                seconds = remaining % 60
                time_str = f"{minutes:02d}:{seconds:02d}"
                
                # Aktualizacja szerokości paska przy każdej iteracji
                progress.columns[1].bar_width = int(self.console.width * 0.4)
                progress.update(task, advance=1, time_left=time_str)
                self.live.update(self.create_panel(
                    layout,
                    title='[green]POMODORO TIMER[/]' if type == "focus" else '[red]POMODORO TIMER[/]',
                    border_style='bold red' if type == "focus" else 'bold green',
                    subtitle=f"[red]{current_time()}[/]" if type == "focus" else f"[green]{current_time()}[/]" 
                ))
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