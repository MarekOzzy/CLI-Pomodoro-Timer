import time

class Waiting_time:
    def __init__(self, time, type):
        self.time = time
        self.type = type

    def actual_time(sel):
        return time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())

    def waiting(self):
        pass

    def ringing(self):
        pass

if __name__ == "__main__":
    przerwa = Waiting_time(10, 'przerwa')
    print(przerwa.actual_time())