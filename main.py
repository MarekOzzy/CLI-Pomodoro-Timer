import time
from CUI import Interface
from util import *


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
        self.interface.ring(self.type)
        if self.type == 'focus':
            Timer.performed_cycles += 1



def main():

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