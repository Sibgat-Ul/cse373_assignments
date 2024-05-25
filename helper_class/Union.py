class Union:
    def __init__(self, val1, val2=None):
        self.val1 = val1
        self.val2 = val2

    def __getattr__(self):
        return self.val1 if self.val1 is not None else self.val2
