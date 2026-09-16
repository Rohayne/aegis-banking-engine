class LedgerRepository:
    def __init__(self):
        self.entries = []

    def save(self, entry):
        self.entries.append(entry)