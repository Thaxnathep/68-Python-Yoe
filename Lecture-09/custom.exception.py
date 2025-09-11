class NegativeMumberError(Exception):
    def __int__(self, value):
        self.value = value
        super().__init__(f'Invalid input: {value} is a negative number')

def Check(num):
    if