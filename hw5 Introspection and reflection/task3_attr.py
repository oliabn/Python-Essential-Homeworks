"""Task3
Використовуючи код з завдання 2, використати функції hasattr(), getattr(),
setattr(), delattr(). Застосувати ці функції до кожного з атрибутів класів,
подивитися до чого це призводить.
"""

from task2_2_updateContact import UpdateContact

# create contacts
contact_1 = UpdateContact('Leslie', 11111111, 'Jordan')
contact_2 = UpdateContact('Katy', 55555555, 'Hessel', 30, 'katy@gmail.com', 'menager')

print('     Set email for contact_1')
if hasattr(contact_1, 'email'):    # якщо у contact_1 є атрибут email
    setattr(contact_1, 'email', 'leslie@gmail.com')    # встановити атрибут email=leslie@gmail.com'
    print(getattr(contact_1, "email"))  # отримати атрибут email
print("________________\n")

print('     Get and del job for contact_2 and set it again')
if hasattr(contact_2, 'job'):    # якщо у contact_2 є атрибут job
    print('job:', getattr(contact_2, "job"))  # отримати атрибут job
    delattr(contact_2, 'job')   # видалити атрибут job
    print("hasattr(contact_2, 'job'): ", hasattr(contact_2, 'job'))  # тепер немає job

    try:
        print('job:', getattr(contact_2, "job"))  # отримати (видалений) атрибут job -> AttributeError
    except AttributeError as err:
        print(err)

    setattr(contact_2, 'job', 'Financial manager')  # знову встановити job
    print('job:', getattr(contact_2, "job"))   # отримати атрибут job
