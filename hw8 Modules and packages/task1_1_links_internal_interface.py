"""Task1
Перепишіть домашнє завдання попереднього уроку
(сервіс для скорочення посилань), щоб у нього була
основна частина, яка відповідала би за логіку роботи та
надавала внутрішній, і модуль представлення,
який відповідав би за взаємодію з користувачем. При заміні
останнього на інший, який взаємодіє з користувачем в інший
спосіб, програма має продовжувати коректно працювати.
"""

import shelve

links = {}


def write_link_to_db(link, link_name):
    with shelve.open('links_db') as new_link:
        new_link[link_name] = link


def read_links_from_db():
    with shelve.open('links_db') as links_in_db:
        for link_name, link in links_in_db.items():
            links[link_name] = link


def is_it_new(link, name):
    if link in links.values():
        print("This link already exists")

    if name in links:
        print("This name already used")

    return not (link in links.values() or name in links)


def add_link():
    while True:
        link = input("Enter the link: ").strip()
        link_name = input("Enter the link name: ").strip()
        if is_it_new(link, link_name):
            links[link_name] = link
            print("The link was added")
            write_link_to_db(link, link_name)
            break
        print("Try again")


def print_link():
    name = input("Enter the link name: ")
    if name in links:
        print(f"Your link -> \033[34m{links[name]}\033[0m")
    else:
        print("There is no link with that name")


def print_all_links():
    for link_name, link in links.items():
        print(f'{link_name}: {link}')
    print()


read_links_from_db()
