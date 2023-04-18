"""Task4
Опишіть два класи Base та його спадкоємця Child з методами method(),
який виводить на консоль фрази відповідно "Hello from Base" та
"Hello from Child", using classmethod (@classmethod) decorator.
"""


class Base:

    @classmethod
    def hello(cls):
        print(f'Hello from {cls.__name__}')


class Child(Base):
    pass


# test
if __name__ == '__main__':
    base = Base()
    child = Child()

    base.hello()
    child.hello()
