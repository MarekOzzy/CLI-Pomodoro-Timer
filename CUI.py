import sys
from rich.console import Console
from rich.live import Live
from rich.panel import Panel
from rich.progress import Progress, BarColumn, TextColumn
from rich.layout import Layout
from util import *

class Interface:
    def __init__(self):
        # Tworzymy obiekt konsoli w którym będziemy wyświetlać interfejs graficzny
        console = Console()
        pass

    # Naciśnij enter aby rozpocząć, lub podaj parametry jeśli nie podano ich jako flagę
    def start(self, focus_time=None, break_time=None):
        # Do dodania walidacja formatu
        if focus_time is None:
            focus_time = string_to_seconds(input("Enter focus time in either minutes:seconds or plain minutes: "))
        if break_time is None:
            break_time = string_to_seconds(input("Enter break time in either minutes:seconds or plain minutes"))
        input("Press enter to start")
        return focus_time, break_time

    # Ekran czekania
    def wait(self, type):
        pass

    # Ekran z dzwonkiem plus dźwięk
    def ring(self, type):
        pass

    # Egran końcowy
    def end(self):
        print('END')
        sys.exit()

    # Wznosi błąd. Służy aby poprosić użytkownika o ponowne wprowadzenie danych
    def error(self, e):
        input(f"Error: {e}")

    def critical_error(self, e):
        input(f"Error: {e}\nPress enter to close program")
        sys.exit()