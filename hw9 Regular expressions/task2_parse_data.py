"""Task2
Написати функцію, яка за допомогою регулярних виразів з файлу
витягує дані про дату народження, телефон та електронну адресу.
Дані потрібно записати до іншого файлу.
"""

import re


def get_birth_date(text):
    if re.search(r'\d{2}[-.]\d{2}[-.]\d{4}', text):
        return re.findall(r'\d{2}[-.]\d{2}[-.]\d{4}', text)[0]


def get_phone(text):
    if re.search(r'(?:[+]\s?\d{1,3})?(?:\s?\d{3})?\s?\d{6}', text):
        return re.findall(r'(?:[+]\s?\d{1,3})?(?:\s?\d{3})?\s?\d{6}', text)[0].strip()


def get_email(text):
    if re.search(r'\w+@\w+\.\w+', text):
        return re.findall(r'\w+@\w+\.\w+', text)[0]


def parse_file(file_name: str) -> list:
    """Returns a list of tuples with date
    of birth, phone, email from each line in the file """

    with open(file_name, 'r') as file:
        data = []
        for text in file:
            data.append((get_birth_date(text),
                         get_phone(text),
                         get_email(text)))

    return data


def write_to_file(file_name: str, data: list):
    with open(file_name, 'w') as file:
        for line in data:
            string = ' '.join(str(elem) for elem in line) + '\n'
            file.write(string)


data = parse_file('data_task2')
for person_info in data:
    print(person_info)

write_to_file('recorded_data_task2', data)
