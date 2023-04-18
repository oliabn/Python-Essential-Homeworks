"""Task5
Використовуючи код завдання 2 надрукуйте у терміналі інформацію,
яка міститься у класах Contact та UpdateContact та їх екземплярах.
Видаліть атрибут job, і знову надрукуйте стан класів та їх екземплярів.
Порівняйте їх. Зробіть відповідні висновки.
"""
# In terminal

"""
python
from task2_2_updateContact import UpdateContact, Contact

# Info about classes
UpdateContact.__doc__
Contact.__doc__

dir(UpdateContact)
dir(Contact)
UpdateContact.__base__

# info about instance of the UpdateContact, Contact
contact_1 = UpdateContact('Katy', 55555555, 'Hessel', 30, 'katy@gmail.com', 'menager')
contact_2 = Contact('Eleonora', 33333333, 'Giorgi')

contact_1.__dict__ 
contact_2.__dict__ 

contact_1 = UpdateContact('Katy', 55555555, 'Hessel', 30, 'katy@gmail.com', 'menager')
contact_1.job
delattr(contact_1, 'job')
contact_1.__dict__
UpdateContact.__dict__
"""