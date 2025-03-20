import time
import argparse
import sys
from rich.console import Console
from rich.live import Live
from rich.panel import Panel
from rich.progress import Progress, BarColumn, TextColumn
from rich.layout import Layout



def get_args(interface):
    # Funkcja zwraca elementy podane podczas uruchamiania programu
    parser = argparse.ArgumentParser()
    parser.add_argument('-f',
                        '--focus',
                        type=str, 
                        help='Focus time given in format minutes:seconds')
    parser.add_argument('-b',
                        '--breaks',
                        type=str,
                        help='Break time given in format minutes:seconds')
    parser.add_argument('-c',
                        '--cycles',
                        type=int,
                        help='Number of focus cycles')
    args = parser.parse_args()
    try:
        focus_time = string_to_seconds(args.focus)
        break_time = string_to_seconds(args.breaks)
    except Exception as e:
        interface.end(e)
    
    cycles = args.cycles if args.cycles else 0

    return focus_time, break_time, cycles

# Do usunięcia?
def actual_time():
    return time.strftime("%H:%M:%S", time.localtime())

def string_to_seconds(str):
    # Function converting either "minutes:seconds" format or plain minutes to seconds
    if ':' in str:
        tabela = str.split(':')
        minuty = int(tabela[0])
        sekundy = int(tabela[1])
        if sekundy >= 60 or sekundy < 0:
            raise ValueError("Incorrect format. Seconds must be between 0 and 59")
        total = minuty * 60 + sekundy
    else:
        try:
            minuty = int(str)
            total = minuty * 60
        except ValueError:
            raise ValueError("Incorrect format. Use either minutes:seconds or plain minutes")
    return total

class Timer:
    performed_cycles = 0
    # Jeśli nie podano ilości cykli jako argument to flaga = False, a program będzie wykonywał się w nieskończoność
    flag = False

    def __init__(self, time, type, interface):
        self.time = time
        self.type = type
        self.interface = interface

    def waiting(self):

        time.sleep(1)

    def ringing(self):
        if self.type == 'focus':
            if Timer.flag:
                Timer.performed_cycles += 1
            print('DRYNNN KONIEC POMODORO, POCZATEK PRZERWY')
        if self.type == 'break': 
            print("DRYNNN KONIEC PRZERWY, WRACAJ DO PRACY")

class Interface:
    def __init__(self):
        pass

    # Naciśnij enter aby rozpocząć, lub podaj parametry jeśli nie podano ich jako flagę
    def start(self, focus_time=None, break_time=None):
        # Do dodania walidacja formatu
        if focus_time is None:
            focus_time = int(input("Enter focus time in either minutes:seconds or plain minutes: "))
        if break_time is None:
            break_time = int(input("Enter break time in either minutes:seconds or plain minutes"))
        input("Naciśnij enter aby rozpocząć")
        return focus_time, break_time

    # Ekran czekania
    def wait(self, type):
        pass

    # Ekran z dzwonkiem plus dźwięk
    def ring(self, type):
        pass

    # Egran końcowy
    def end(self):
        pass

    # Wznosi błąd. Służy aby poprosić użytkownika o ponowne wprowadzenie danych
    def error(self, e):
        pass

    def critical_error(self, e):
        pass

def main():
    # Tworzymy obiekt konsoli w którym będziemy wyświetlać interfejs graficzny
    console = Console()

    # Tworzymy obiekt klasy interface który przekażemy do obiektów klasy Timer
    interface = Interface()

    # Pobieramy argumenty
    try:
        focus_time, break_time, cycles = get_args(interface)
    except Exception as e:
        interface.critical_error(e)

    # Okno startu. Sprawdzamy o jakie parametry będziemy pytać użytkownika jeśli nie podano flag
    focus_time, break_time = interface.start(focus_time, break_time)

    # Tworzymy obiekty Timer
    timer_focus = Timer(focus_time, type='focus', interface=interface)
    timer_break = Timer(break_time, type='break', interface=interface)

    # Jeśli podano jako argument ilość cykli, to flaga = True
    if cycles != 0:
        Timer.flag = True

    while True:
        timer_focus.waiting()
        timer_focus.ringing()
        # Jeśli nie podano ilości cykli to flaga == False a petla będzie się wykonywać w nieskończoność
        if Timer.flag == True:
            # Jeśli flaga jest False, to sprawdzamy czy wykonała się zadana ilość cykli 
            if Timer.performed_cycles >= cycles:
                break
        timer_break.waiting()
        timer_break.ringing()
        continue
    interface.end()

if __name__ == '__main__':
    main()