"""Task1
Перепишіть домашнє завдання попереднього уроку
(сервіс для скорочення посилань), щоб у нього була
основна частина, яка відповідала би за логіку роботи та
надавала внутрішній, і модуль представлення,
який відповідав би за взаємодію з користувачем. При заміні
останнього на інший, який взаємодіє з користувачем в інший
спосіб, програма має продовжувати коректно працювати.
"""

from task1_1_links_internal_interface import *

HELP = ("\033[36mEnter: \n1 to create a new link"
        "\n2 to get the link by name,"
        "\n3 to see all links, "
        "\n4 to exit: \033[0m")

while True:
    step = input(HELP)
    print()

    match step:
        case '4':
            exit()

        case "3":
            print_all_links()

        case "1":
            add_link()

        case "2":
            print_link()

        case _:
            print("Choose step -> 1, 2, 3 or 4: ")
