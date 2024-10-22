import random

a = random.randint(1, 3)
s = random.randint(4, 30)


def game(s, a):
    try:
        while True:
            print(f'Количество камней = {s}')
            if s == 3:
                print("Ваш ход: Введите количество камней которое хотите забрать")
                n = int(input())
                if n < 0 or n > 3:
                    return "Вы можете ввести число от 1 до 3"
                s -= n
                if s == 0:
                    print(f'Количество камней = {s}')
                    return "Вы вышли за пределы"
                if s == 1:
                    print(f'Количество камней = {s}')
                    return "Победа игрока"
                if s == 2:
                    s -= 1
                    print(f'Количество камней = {s}')
                    return "Победа компьютера"
            if s == 2:
                print("Ваш ход: Введите количество камней которое хотите забрать")
                n = int(input())
                if n < 0 or n > 3:
                    return "Вы можете ввести число от 1 до 3"
                s -= n
                if s < 1:
                    print(f'Количество камней = {s}')
                    return "Вы вышли за пределы"
                if s == 1:
                    print(f'Количество камней = {s}')
                    return "Победа игрока"
            print("Ваш ход: Введите количество камней которое хотите забрать")
            n = int(input())
            if n < 0 or n > 3:
                return "Вы можете ввести число от 1 до 3"
            s -= n
            if s == 1:
                print(f'Количество камней = {s}')
                return "Победа игрока"
            if s == 2:
                s -= 1
                print(f'Количество камней = {s}')
                return "Победа компьютера"
            if s == 3:
                s -= 2
                print(f'Количество камней = {s}')
                return "Победа компьютера"
            if s == 4:
                s -= 3
                print(f'Количество камней = {s}')
                return "Победа компьютера"
            s -= a
    except ValueError:
        return "Вы можете вводить цифры от 1 до 3"


print(game(s, a))
