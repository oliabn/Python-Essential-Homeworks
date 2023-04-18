"""
Створити клас Contact з полями surname, name, age, mob_phone, email.
Додати методи get_contact, sent_message. Створити клас-нащадок
UpdateContact з полями surname, name, age, mob_phone, email, job.
Додати методи get_message. Створити екземпляри класів та дослідити
стан об'єктів за допомогою атрибутів: __dict__, __base__, __bases__.
Роздрукувати інформацію на екрані.
"""


class Contact:
    """Class UpdateContact with param: name, phone (number), surname, age, email
    To store phone contacts and SMS, getting/sending sms"""

    def __init__(self, name: str, phone: int, surname='', age=None, email=''):
        self.name = name
        self.phone = phone
        self.surname = surname
        self.age = age
        self.email = email
        self.sent_sms = []

    def __str__(self):
        return (f'{self.name}, {self.surname}: {self.phone}' if self.surname
                else f'{self.name}: {self.phone}')

    def __repr__(self):
        return (f'{self.__name__}: {self.name}, {self.surname} - {self.phone}' if self.surname
                else f'{self.__name__}: {self.name} - {self.phone}')

    def get_contact(self) -> 'Contact':
        return self

    def _add_sent_sms(self, msg: str, contact: 'Contact'):
        key = (f'from me to {contact.name} {contact.surname}'
               if contact.surname
               else f'from me to {contact.name}')
        self.sent_sms.append({str(key): msg})

    def send_sms(self, msg: str, contact: 'Contact'):
        self._add_sent_sms(msg, contact)
        print(f'The message <{msg}> was sent to {contact.name} {contact.surname}'
              if contact.surname
              else f'The message <{msg}> was sent to {contact.name}')


if __name__ == '__main__':
    # create contacts
    contact_1 = Contact('Leslie', 11111111)
    contact_2 = Contact('Katy', 55555555, 'Hessel', 30, 'katy@gmail.com')
    contact_3 = Contact('Eleonora', 33333333, 'Giorgi')

    print('     Getting contacts')
    print(contact_1.get_contact())
    print(contact_2.get_contact())
    print()

    print('     Sending sms')
    contact_1.send_sms("Yo, what’s up?", contact_2)
    contact_2.send_sms("G'day", contact_1)
    contact_2.send_sms("Sure", contact_3)
    print()

    print('     Sent_sms list of contact_1 and contact_2')
    print(contact_1.sent_sms)
    print(contact_2.sent_sms)
    print()

    print('     contact_1, contact_2, and contact_3 attributes')
    print(contact_1.__dict__)
    print(contact_2.__dict__)
    print(contact_3.__dict__)
    print()

    print('     Parent and parents tuple of UpdateContact')
    print('Contact.__base__', Contact.__base__)
    print('Contact.__bases__', Contact.__bases__)
