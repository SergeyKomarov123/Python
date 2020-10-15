import random

print("Как тебя зовут?")
userName = input()
print(userName + "," " игра заключается в угадывании цифры которую загадывает программа. Начнем?")
print("Да/Нет")
b = input()
if (b == "да" or b == "нет"):
    z = 1
else:
    z = 0

while (z == 0):
    print("Необходимо ввести \"да\" или \"нет\"")
    b = input()
    if (b == "да" or b == "нет"):
        z = 1

if (b == "нет"):
    print("Ну как хочешь...")
    quit()

if (b == "да"):
    print("Необходимо установить верхнюю границу выше которого числа загадываться не будут. Для этого введем любое число:")
    try:
        s = int(input())
    except:
        a = 0
        while (a == 0):
            try:
                print('Необходимо ввести число')
                s = int(input())
                a = 1
            except:
                a = 0

    v = 0
    while (v == 0):
        print('=' * 40)
        print("Угадай какое число загадно от 1 до " + str(s) + "?")
        print("Чтобы остановить игру необходимо ввести \"-1\"")
        print('=' * 40)
        try:
            c = int(input())
        except:
            f = 0
            while (f == 0):
                try:
                    c = int(input('Необходимо ввести число    '))
                    f = 1
                except:
                    f = 0

        t = random.randint(1, s)
        i = int(0)
        k = "Отличный результат!"
        stop = int(-1)

        if (c == stop):
            print('=' * 40)
            print("Спасибо за игру! Пока", userName + "!")
            print('=' * 40)
            quit()

        if (c != t):
            while (c != t):
                print("Мимо! Попробуй еще раз")
                try:
                    c = int(input())
                except:
                    f = 0
                    while (f == 0):
                        try:
                            print ('Необходимо ввести число')
                            c = int(input())
                            f = 1
                        except:
                            f = 0
                if (c == stop):
                    print('=' * 40)
                    print("Спасибо за игру! Пока", userName + "!")
                    print('=' * 40)
                    quit()
                i += 1
                if (i > 3):
                    k = "Ну ты и везунчик!"
                elif (1 < i < 3):
                    k = "Неплохо!"
                elif (i == 1):
                    k = "Хороший результат!"
        if (c == t):
            print('=' * 40)
            print("Угадано с", i + 1, "попытки!", k)
            print('=' * 40)

        print("Сыграем еще раз? да/нет")
        b = input()
        if (b == "да"):
            f = 0
            v = 0
        if (b == "нет"):
            f = 0
            v = 1
        elif (b != "да" and b != "нет"):
            f = 1
            while (f == 1):
                print("Введи \"да\" или \"нет\"")
                b = input()
                if (b == "да"):
                    f = 0
                    v = 0
                if (b == "нет"):
                    f = 0
                    v = 1
    print('=' * 40)
    print("Спасибо за игру! Пока", userName + "!")
    print('=' * 40)
    quit()


