import random

print("Как тебя зовут?")
userName = input()
print(userName + "," " давай сыграем в игру угадай число?")
b = input("да/нет:     ")
if (b == "да" or b == "нет"):
    f = 1
else:
    f = 0

while (f == 0):
    print("Я не понял твой ответ. Введи да или нет")
    b = input()
    if (b == "да" or b == "нет"):
        f = 1

if (b == "нет"):
    print("Ну и зря, здесь нельзя проиграть!", userName + "," " может все таки попробуем?")
    b = input("да/нет:     ")
    if (b == "да" or b == "нет"):
        f = 1
    else:
        f = 0
while (f == 0):
    print("Я не понял твой ответ. Введи да или нет")
    b = input()
    if (b == "да" or b == "нет"):
        f = 1

if (b == "нет"):
    print("Ну как хочешь")
    quit()

if (b == "да"):
    print("Угадай какое число от 1 до 5 загадано?")
    try:
        c = int(input())
    except:
        f = 0
        while (f == 0):
            try:
                c = int(input('Вместо числа введена строка! Необходимо ввести число    '))
                f = 1
            except:
                c = print('Я так не играю...')
                exit()


t = random.randint(1, 5)
i = int(0)
k = "Отличный результат!"
t = random.randint(1, 5)
i = int(0)

if (c != t):
    while (c != t):
        print("Мимо! Попробуй еще раз")
        c = int(input())
        i += 1
        if (i > 3):
            k = "Ну ты и везунчик!"
        elif (1 < i < 3):
            k = "Неплохо!"
        elif (i == 1):
            k = "Хороший результат!"
if (c == t):
    print('-' * 40)
    print("Угадано с", i + 1, "попытки!", k)
    print('-' * 40)

print("Сыграем еще раз?")
b = input("да/нет:      ")
if (b == "да" or b == "нет"):
    f = 1
else:
    f = 0
while (f == 0):
    print("Я не понял твой ответ. Введи да или нет")
    b = input()
    if (b == "да" or b == "нет"):
        f = 1

if (b == "нет"):
    print("Пока", userName + "!")
    quit()

if (b == "да"):
    print("Угадай какое число от 1 до 5 загадано?")
    try:
        c = int(input())
    except:
        f = 0
        while (f == 0):
            try:
                c = int(input('Вместо числа введена строка! Необходимо ввести число    '))
                f = 1
            except:
                c = print('Я так не играю...')
                exit()

t = random.randint(1, 5)
i = int(0)
k = "Отличный результат!"
t = random.randint(1, 5)
i = int(0)

if (c != t):
    while (c != t):
        print("Мимо! Попробуй еще раз")
        c = int(input())
        i += 1
        if (i > 3):
            k = "Ну ты и везунчик!"
        elif (1 < i < 3):
            k = "Неплохо!"
        elif (i == 1):
            k = "Хороший результат!"
if (c == t):
    print('-' * 40)
    print("Угадано с", i + 1, "попытки!", k)
    print('-' * 40)
print("Спасибо за игру!")
