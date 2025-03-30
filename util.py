import time 
import argparse

def get_args(interface):
    # Funkcja zwraca elementy podane podczas uruchamiania programu
    parser = argparse.ArgumentParser()
    parser.add_argument('-f',
                        '--focus',
                        type=str, 
                        help='Focus time given in format minutes:seconds or plain minutes')
    parser.add_argument('-b',
                        '--breaks',
                        type=str,
                        help='Break time given in format minutes:seconds or plain minutes')
    parser.add_argument('-c',
                        '--cycles',
                        type=int,
                        help='Number of focus cycles')
    args = parser.parse_args()
    try:
        focus_time = string_to_seconds(args.focus) if args.focus else 1500
        break_time = string_to_seconds(args.breaks) if args.breaks else 300
    except Exception as e:
        interface.critical_error(e)
    
    cycles = args.cycles if args.cycles else 0
    # Dodać sprawdzenie czy podana wartość jest dodatnia
    try:
        int(cycles)
    except Exception as e:
        interface.critical_error(e)

    return focus_time, break_time, cycles

def current_time():
    return time.strftime("%H:%M:%S")

def string_to_seconds(str):
    # Dodać walidację tego czy podano wartości dodatnie
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