"""Task 2
Створіть 2 класи мови, наприклад, англійська та іспанська.
В обох класів має бути метод greeting(). Обидва створюють різні привітання.
Створіть два відповідні об'єкти з двох класів вище та викличте дії цих двох
об'єктів в одній функції (функція hello_friend).
"""


class Language:
    """Base class for greeting class in different languages."""

    @classmethod
    def greeting(cls, name):
        raise NotImplementedError('greeting() must be overwritten in child classes\n'
                                  'name = cls._verify_name(name)\n'
                                  'print(f"<Hello in some lang.> {name}")')

    @staticmethod
    def _verify_name(name):
        if type(name) != str:
            raise TypeError("The name must be str.")
        if len(name.split()) > 1:
            raise ValueError("The name must consist of only one First name.")
        for char in name:
            if not char.isalpha():
                raise TypeError("The name must consist of only alphabetic characters.")
        return name.title()
