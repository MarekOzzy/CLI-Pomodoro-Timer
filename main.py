import time
import argparse
from rich.console import Console
from rich.live import Live
from rich.panel import Panel
from rich.progress import Progress, BarColumn, TextColumn
from rich.layout import Layout

console = Console()

def get_args():
    # Funkcja zwraca elementy podane podczas uruchamiania programu
    parser = argparse.ArgumentParser()
    parser.add_argument('-f',
                        '--focus',
                        type=str, 
                        help='Focus time given in minutes')
    parser.add_argument('-b',
                        '--breaks',
                        type=str,
                        help='Breake time given in minutes')
    parser.add_argument('-c',
                        '--cycles',
                        type=int,
                        help='Number of focus cycles')
    args = parser.parse_args()

    focus_time = args.focus if args.focus else None
    break_time = args.breaks if args.breaks else None
    cycles = args.cycles if args.cycles else 0
    
    return focus_time, break_time, cycles

# Do usunięcia?
def actual_time():
    return time.strftime("%H:%M:%S", time.localtime())

def string_to_seconds(str):
    pass

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
        if focus_time is None:
            focus_time = int(input("Podaj czas skupienia (w minutach): "))
        if break_time is None:
            break_time = int(input("Podaj czas przerwy (w minutach): "))
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

def main():
    # Tworzymy obiekt klasy interface który przekażemy do obiektów klasy Timer
    interface = Interface()

    # Pobieramy argumenty
    focus_time, break_time, cycles = get_args()

    # Jeśli podano jako argument ilość cykli, to flaga = True
    if cycles != 0:
        Timer.flag = True

    # Okno startu. Sprawdzamy o jakie parametry będziemy pytać użytkownika jeśli nie podano flag
    focus_time, break_time = interface.start(focus_time, break_time)

    # Tworzymy obiekty Timer
    timer_focus = Timer(focus_time, type='focus', interface=interface)
    timer_break = Timer(break_time, type='break', interface=interface)

    
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