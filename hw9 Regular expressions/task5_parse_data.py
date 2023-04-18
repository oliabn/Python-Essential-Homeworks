"""Task5
З клавіатури вводиться рядок, в якому є інформація про
прізвище, ім'я, дату народження, електронну адресу та
відгук про курси учня. Написати функцію, яка,
використовуючи регулярні вирази, витягне дані з рядка
і поверне словник.
"""

import re


def get_name(text):
    """Return name and surname from str like these: 'name: Rick Goulding', 'name: Rick'"""
    if re.search(r'name: (?P<name>[a-zA-Z]+(?: [a-zA-Z]+)?)', text):
        return re.search(r'name: (?P<name>[a-zA-Z]+(?: [a-zA-Z]+)?)', text)[1]


def get_date(text):
    """Return date from str like these: 'date: 07.03.2005' or 'date: 07-03-2005'"""
    if re.search(r'date: (?P<date>\d{2}[-.]\d{2}[-.]\d{4})', text):
        return re.search(r'date: (?P<date>\d{2}[-.]\d{2}[-.]\d{4})', text)[1]


def get_email(text):
    """Return email from str like it: 'email: kevin@outlook.com'"""
    if re.search(r'email: (?P<email>\w+@\w+\.\w+)', text):
        return re.search(r'email: (?P<email>\w+@\w+\.\w+)', text)[1]


def get_phone(text):
    """Return phone number from str like these: 'tel: +49 059 173496', 'tel: 173496,'
    'tel: 059 173496', 'tel: 059173496', 'tel: +49089123456'"""

    if re.search(r'tel[.]{0,1}: (?P<phone>(?:[+]\s?\d{1,3})?(?:\s?\d{3})?\s?\d{6})', text):
        return re.search(r'tel[.]{0,1}: (?P<phone>(?:[+]\s?\d{1,3})?(?:\s?\d{3})?\s?\d{6})', text)[1]


def get_response(text):
    """Return response from str like these: 'resp: I liked everything',
     'resp.: I liked everything', 'response: I liked everything'"""

    if re.search(r'(?:resp[.]?|response): (?P<response>.+)', text):
        return re.search(r'(?:resp[.]?|response): (?P<response>.+)', text)[1]


def parse_text(text):
    """Get name, date, email, phone, and response from text.
    Return dict with them.
    Template of the text:
    'name: Rick Goulding, date: 07.03.2005, tel: +1 059 173496,
    'email: kevin@outlook.com, resp: Great course. I liked everything' """

    return {'name': get_name(text),
            'date': get_date(text),
            'email': get_email(text),
            'phone': get_phone(text),
            'response': get_response(text)}


template = "name: Rick Goulding, date: 07.03.2005, tel: +49 059 173496, " \
           "email: goulding@outlook.com, resp: Great course. I liked everything"

# print(parse_text(template))
print(f'Template of text:\n{template}')
text = input("Enter the information according to the template above:\n")
print(parse_text(text))
