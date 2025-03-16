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
                        '--break',
                        type=int,
                        help='Breake time given in minutes')
    parser.add_argument('-c',
                        '--cycles',
                        type=int,
                        help='Number of focus cycles')
    args = parser.parse_args()

    if args.f is not None:
        focus_time = args.f
    else:
        focus_time = 25

    if args.b is not None:
        break_time = args.b
    else:
        break_time = 5

    cycles = args.c

    return focus_time, break_time, cycles

def actual_time():
    return time.strftime("%H:%M:%S", time.localtime())

class Timer:
    performed_cycles = None

    def __init__(self, time, type):
        self.time = time
        self.type = type

    def waiting(self):
        pass

    def ringing(self):
        if self.type == 'focus':
            Timer.performed_cycles += 1
            print('DRYNNN KONIEC POMODORO, POCZATEK PRZERWY')
        else: 
            print("DRYNNN KONIEC PRZERWY, WRACAJ DO PRACY")
        


def main():
    focus_time, break_time, cycles = get_args()
    Timer.performed_cycles = cycles

    timer_focus = Timer(focus_time, type = 'focus')
    timer_break = Timer(break_time, type = 'break')

    while True:
        if cycles:
            timer_focus.waiting()
            timer_focus.ringing()
            if Timer.performed_cycles is not None and Timer.performed_cycles >= cycles:
                break
            timer_break.waiting()
            timer_break.ringing()
        continue

main()