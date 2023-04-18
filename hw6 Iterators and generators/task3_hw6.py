"""Task3 hw6
Напишіть ітератор, який повертає елементи заданого
списку у зворотному порядку (аналог reversed).
"""


class ReverseIter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.idx = len(self.iterable)

    def __iter__(self):
        return self

    def __next__(self):
        self.idx -= 1
        if self.idx >= 0:
            return self.iterable[self.idx]
        else:
            raise StopIteration()


# test
if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5]
    rev = ReverseIter(lst)

    print(next(rev))
    print(next(rev))
    print(next(rev))
    print(next(rev))
    print(next(rev))
    # print(next(rev)) # -> StopIter
