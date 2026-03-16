import time

class Timer:

    def __init__(self, limit):
        self.limit = limit
        self.start = None

    def begin(self):
        self.start = time.time()

    def expired(self):
        return (time.time() - self.start) > self.limit
