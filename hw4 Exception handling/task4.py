"""Task4
Опишіть свій клас винятку. Напишіть функцію, яка викидатиме цей виняток,
якщо користувач введе певне значення, і перехопіть цей виняток під
час виклику функції.
"""


class ExceptionSendData(Exception):
    """Data sending exceptions"""
    pass


class SendData:
    def send_data(self, data):
        if not self._has_connection():
            raise ExceptionSendData("No connection")

    @staticmethod
    def _has_connection():
        return False


if __name__ == '__main__':
    send_info = SendData()

    try:
        send_info.send_data('data')
    except ExceptionSendData as err:
        print("Data wasn't sent")
        print(err)
