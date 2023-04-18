"""Task4
Використовуючи код з завдання 2, створити 2 екземпляри обох класів.
Використати функції isinstance() – для перевірки екземплярів класу
(за яким класом створені) та issubclass() – для перевірки і
визначення класу-нащадка.
"""

from task2_2_updateContact import UpdateContact, Contact

# create contacts

contact_1 = UpdateContact('Katy', 55555555, 'Hessel', 30, 'katy@gmail.com', 'menager')
contact_2 = Contact('Eleonora', 33333333, 'Giorgi')

print("     Use isinstance()")
print("Is contact_1 the instance of the UpdateContact", isinstance(contact_1, UpdateContact))
print("Is contact_1 the instance of the Contact:", isinstance(contact_1, Contact))
print()
print("Is contact_2 the instance of the UpdateContact", isinstance(contact_2, UpdateContact))
print("Is contact_2 the instance of the Contact:", isinstance(contact_2, Contact))
print('__________\n')

print("     Use issubclass()")
print("Whether a UpdateContact is the subclass of the Contact:", issubclass(UpdateContact, Contact))
print("Whether the Contact is the subclass of the Object:", issubclass(Contact, object))
