class TranspositionTable:

    def __init__(self):
        self.table = {}

    def lookup(self, key):
        return self.table.get(key, None)

    def store(self, key, value):
        self.table[key] = value
