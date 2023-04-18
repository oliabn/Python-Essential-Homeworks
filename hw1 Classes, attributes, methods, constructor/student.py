class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):
        if 0 <= item >= len(self.marks):
            return self.marks[item]
        else:
            raise IndexError("Incorrect index")

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0:
            raise TypeError("Incorrect index")

        if key >= len(self.marks):
            off = key + 1 - len(self.marks)
            self.marks.extend([None]*off)

        self.marks[key] = value

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError("Incorrect index")

        del self.marks[key]


s1 = Student("Nicola", [5, 5, 4])
s1[5] = 5
print(s1.marks)

del s1[3]
print(s1.marks)