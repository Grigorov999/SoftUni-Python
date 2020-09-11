class sequence_repeat:
    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.number > 0:
            current_char = self.sequence[self.index]
            self.number -= 1
            self.index += 1
            if self.index == len(self.sequence):
                self.index = 0
            return current_char
        raise StopIteration()
