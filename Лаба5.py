from random import randint

def go_robot(s):
    if s == 5 or s > 8:
        return s - randint(1, 3)
    if s <= 4:
        return 1
    if 6 <= s <= 8:
        return 5


def proverka(x, s):
    return x.isdigit() and s - int(x) > 0 and 1 <= int(x) <= 3


def go_player(s):
    while True:
        x = input('Сколько камней вы хотите убрать: ')
        if proverka(x, s):
            return int(x)
        print('Введите соответствующее число')


s = randint(4, 30)
print(f'Всего {s} камней')
answer = input('Вы хотите делать ход первым? (+/-)\n')
if answer == '+':
    while True:
        print(f'Ваш ход')
        Hod_igroka = go_player(s)
        s -= Hod_igroka
        print(f'Осталось {s} камней')
        if s == 1:
            exit('Победил игрок')
        print(f'Ходит робот')
        s = go_robot(s)
        print(f'Осталось {s} камней')
        if s == 1:
            exit('Победил робот')
else:
    while True:
        print(f'Ходит робот')
        s = go_robot(s)
        print(f'Осталось {s} камней')
        if s == 1:
            exit('Победил робот')
        print(f'Ваш ход')
        Hod_igroka = go_player(s)
        s -= Hod_igroka
        print(f'Осталось {s} камней')
        if s == 1:
            exit('Победил игрок')
