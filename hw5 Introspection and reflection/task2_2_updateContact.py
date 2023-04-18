"""
Створити клас Contact з полями surname, name, age, mob_phone, email.
Додати методи get_contact, sent_message. Створити клас-нащадок
UpdateContact з полями surname, name, age, mob_phone, email, job.
Додати методи get_message. Створити екземпляри класів та дослідити
стан об'єктів за допомогою атрибутів: __dict__, __base__, __bases__.
Роздрукувати інформацію на екрані.
"""

from task2_1_contact import Contact


class UpdateContact(Contact):
    """Class UpdateContact with param: name, phone (number), surname, age, email, job
    To store phone contacts and SMS, getting/sending SMS"""

    def __init__(self, name: str, phone: int, surname='', age=None, email='', job=''):
        super().__init__(name, phone, surname, age, email)
        self.job = job
        self.gotten_sms = []

    def _add_gotten_sms(self, msg: str, contact: 'Contact'):
        key = (f'from {contact.name} {contact.surname}'
               if contact.surname
               else f'from {contact.name}')
        self.gotten_sms.append({str(key): msg})

    def get_sms(self, msg: str, contact: 'Contact'):
        self._add_gotten_sms(msg, contact)
        print(f'The message <{msg}> was got from {contact.name} {contact.surname}'
              if contact.surname
              else f'The message <{msg}> was got from {contact.name}')


if __name__ == '__main__':
    # create contacts
    contact_1 = UpdateContact('Leslie', 11111111, 'Jordan')
    contact_2 = UpdateContact('Katy', 55555555, 'Hessel', 30, 'katy@gmail.com', 'menager')
    contact_3 = UpdateContact('Eleonora', 33333333, 'Giorgi')

    print('     Sending and getting messages')
    contact_1.send_sms("Yo, what’s up?", contact_2)
    contact_2.get_sms("Yo, what’s up?", contact_1)
    print()

    contact_1.send_sms("G'day", contact_3)
    contact_3.get_sms("G'day", contact_1)
    print()

    contact_2.send_sms("Sure", contact_3)
    contact_3.get_sms("Sure", contact_2)
    print()

    print('     Gotten_sms list of contact_3')
    print(contact_3.gotten_sms)
    print()

    print('     contact_1, contact_2, and contact_3 attributes')
    print(contact_1.__dict__)
    print(contact_2.__dict__)
    print(contact_3.__dict__)
    print()

    print('     Parent and parents tuple of UpdateContact')
    print('UpdateContact.__base__', UpdateContact.__base__)
    print('UpdateContact.__bases__', UpdateContact.__bases__)
