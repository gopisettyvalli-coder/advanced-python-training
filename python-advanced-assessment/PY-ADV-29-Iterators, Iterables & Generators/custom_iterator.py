class MyNumbers:

    def __init__(self):
        self.number = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.number <= 5:
            value = self.number
            self.number += 1
            return value
        else:
            raise StopIteration

numbers = MyNumbers()

for number in numbers:
    print(number)