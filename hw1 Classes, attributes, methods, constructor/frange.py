class FRange:
    def __init__(self, start=0.0, stop=0.0, step=1.0):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        self.value = self.start - self.step     # щоб почати вертати з першого а не з (першого + шаг)
        return self

    def __next__(self):
        if self.value + self.step < self.stop:  # щоб без включно останнього було
            self.value += self.step
            return self.value
        else:
            raise StopIteration


fr = FRange(0, 2, 0.5)
for x in fr:
    print(x)

# print(next(fr))
# print(next(fr))
# print(next(fr))
# print(next(fr))

