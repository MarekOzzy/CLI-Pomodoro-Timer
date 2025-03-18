import time
import argparse

def get_args():
    # Funkcja zwraca elementy podane podczas uruchamiania programu
    parser = argparse.ArgumentParser()
    parser.add_argument('-f',
                        '--focus',
                        type=int, 
                        help='Focus time given in minutes')
    parser.add_argument('-b',
                        '--breaks',
                        type=int,
                        help='Breake time given in minutes')
    parser.add_argument('-c',
                        '--cycles',
                        type=int,
                        help='Number of focus cycles')
    args = parser.parse_args()

    if args.focus is not None:
        focus_time = args.focus
    else:
        focus_time = 25

    if args.breaks is not None:
        break_time = args.breaks
    else:
        break_time = 5

    if args.cycles is not None:
        cycles = args.cycles
    else:
        cycles = 0
    
    return focus_time, break_time, cycles

def actual_time():
    return time.strftime("%H:%M:%S", time.localtime())

class Timer:
    performed_cycles = 0
    # Jeśli nie podano ilości cykli jako argument to flaga = False, a program będzie wykonywał się w nieskończoność
    flag = False

    def __init__(self, time, type):
        self.time = time
        self.type = type

    def waiting(self):
        time.sleep(1)

    def ringing(self):
        if self.type == 'focus':
            if Timer.flag:
                Timer.performed_cycles += 1
            print('DRYNNN KONIEC POMODORO, POCZATEK PRZERWY')
        if self.type == 'break': 
            print("DRYNNN KONIEC PRZERWY, WRACAJ DO PRACY")

def main():
    # Pobieramy argumenty
    focus_time, break_time, cycles = get_args()
    # Jeśli podano jako argument ilość cykli, to flaga = True
    if cycles != 0:
        Timer.flag = True

    # Tworzymy obiekty Timer
    timer_focus = Timer(focus_time, type = 'focus')
    timer_break = Timer(break_time, type = 'break')

    input('Naciśnij enter aby rozpocząć')
    while True:
        timer_focus.waiting()
        timer_focus.ringing()
        # Jeśli flaga jest False, to sprawdzamy czy wykonała się zadana ilość cykli 
        if Timer.flag == True:
            if Timer.performed_cycles >= cycles:
                break
        timer_break.waiting()
        timer_break.ringing()
        continue
    input('Koniec Programu, naciśnij dowolny klawisz aby zamknąć program')

main()