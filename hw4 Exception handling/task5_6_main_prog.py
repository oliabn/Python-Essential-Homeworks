"""Task5
Створіть програму спортивного комплексу, у якій передбачене меню:
1 - перелік видів спорту, 2 - команда тренерів, 3 - розклад тренувань,
4 - вартість тренування. Дані зберігати у словниках.
Також передбачити пошук по прізвищу тренера, яке вводиться з клавіатури
у відповідному пункті меню. Якщо ключ не буде знайдений, створити
відповідний клас-Exception, який буде викликатися в обробнику виключень.
"""

from datetime import time

from task5_5_sport import Sport
from task5_1_schedule import Schedule
from task5_4_coach import Coach

HELP = "\nEnter 1 to see the list of disciplines\n" \
       "2 to see the teams of coaches\n" \
       "3 to see the schedule\n" \
       "4 to see the coast\n" \
       "5 to find a coach by surname\n" \
       "<q> for exit\n\n" \
       "-> "


class ExceptionCoachNotFound(Exception):
    """Exception when the coach wasn't found"""
    pass


club_info = {
    'tennis': Sport('tennis',
                    Schedule({'mon': time(17), 'thu': time(19)}),
                    100,
                    [Coach('Leslie', 'Mckinney'), Coach('Kevin', 'Force')]),
    'basketball': Sport('basketball',
                        Schedule({'sat': time(18), 'tue': time(19)}),
                        100,
                        [Coach('Nolan', 'Gibney')]),
    'football': Sport('football',
                      Schedule({'wed': time(17), 'fri': time(17)}),
                      100,
                      [Coach('Terry', 'Pratchett'), Coach('Lui', 'Moris')]),
}


def find_coach(surname):
    for sport in club_info.values():
        if sport.find_coach(surname):
            return f'{sport.find_coach(surname)}: {sport.discipline}'
    raise ExceptionCoachNotFound("The coach wasn't found")


def coach_search():
    try:
        surname = input("Enter coach surname: ").strip().title()
        print(find_coach(surname))

    except ExceptionCoachNotFound as err:
        print(err)


# menu
while True:
    step = input(HELP)
    match step:
        case '1':
            for sport in club_info.values():
                print(sport.discipline)
        case '2':
            for sport in club_info.values():
                print(sport.discipline, sport.coaches_team)
        case '3':
            for sport in club_info.values():
                print(sport.discipline)
                print(sport.schedule)
        case '4':
            for sport in club_info.values():
                print(f'{sport.discipline}: {sport.cost}$')
        case '5':
            coach_search()
        case 'q' | '<q>':
            exit()
        case _:
            print('Choose a step from the menu from 1 to 5')
