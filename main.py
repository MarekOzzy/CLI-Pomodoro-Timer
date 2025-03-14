import time

def actual_time():
    return time.strftime("%H:%M:%S", time.localtime())

class Waiting_time:
    def __init__(self, time, type):
        self.time = time
        self.type = type

    def waiting(self):
        pass

    def ringing(self):
        pass

if __name__ == "__main__":
    print(actual_time())