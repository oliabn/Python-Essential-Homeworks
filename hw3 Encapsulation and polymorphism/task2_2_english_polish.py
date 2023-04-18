"""Task 2
Створіть 2 класи мови, наприклад, англійська та іспанська.
В обох класів має бути метод greeting(). Обидва створюють різні привітання.
Створіть два відповідні об'єкти з двох класів вище та викличте дії цих двох
об'єктів в одній функції (функція hello_friend).
"""

from task2_1_language import Language


class English(Language):
    """Class of greeting in English."""

    @classmethod
    def greeting(cls, name):
        name = cls._verify_name(name)
        print(f"Hello {name}")


class Polish(Language):
    """Class of greeting in Polish"""

    @classmethod
    def greeting(cls, name):
        name = cls._verify_name(name)
        print(f"Cześć {name}")


def hello_friend(name):
    english = English()
    polish = Polish()

    english.greeting(name)
    polish.greeting(name)


if __name__ == '__main__':
    hello_friend('katy')
