import random

f = 1
while (f == 1):
    i = 0           # счетчик выхода из цикла
    l = 0           # счетчик удачных угадываний
    prs = int(0)    # коэфициент
    summ = 0        # переменная для суммироания процента из каждой итерации
    area = 100      # верхняя граница диапазона

    print("Введите по очереди 5 чисел от \"1\" до", area)
    while (i < 5):
        target = random.randint(1, 100)
        g = int(0)
        while (g == 0):
            try:
                a = int(input())
                if (a > area or a < 1):
                    print("Необходимо ввести число от \"1\" до", area)
                    g = 0
                else:
                    g = 1
            except:
                print("Необходимо1111 ввести число от \"1\" до", area)
                g = 0

        rp = 0
        i += 1
        # основная логика обработки вводимого числа
        if (target >= a):
            rp = target - a                     # находим разницу между загаданным и угаданным
            rez = (rp * 100 / area)             # приводим эту разницу к единой шкале относительно area
            itogo = 100 - rez                   # приводим к удобному проценту. Значение менее 80% - не принимается к вниманию ввиду высокой погрешности
        if (target < a):
            rp = a - target
            rez = (rp * 100 / area)
            itogo = 100 - rez
        if (target == a):
            l +=1               # считаем количество 100% совпадений
            prs += 5            # расчитываем коэфициент
        summ += itogo

        # Для отладки, вывод промежуточного результата:
        #print("=" * 40)
        print("itogo", itogo, "%")
        #print("l", l)
        #print("summ", summ)
        #print("=" * 40)

    percent = int(summ / 5 + prs)

    if (percent <= 50):
        pns = "крайне низкий"
    if (percent >= 50 and percent < 65):
        pns = "ниже среднестатистического"
    if (percent >= 65 and percent < 85):
        pns = "в пределах среднестатистического"
    if (percent >= 85 and percent < 90):
        pns = "высокий"
    if (percent >= 90 and percent < 100):
        pns = "крайне высокий"
    if (percent >= 100):
        pns = "Невероятный!"


    print("*" * 40)
    print("РЕЗУЛЬТАТ:")
    print("Колличество полных совпадений:", l)
    print("Уровень удачи:", str(pns) + "%")
    print("*" * 40)


    print("Сыграем еще раз? да/нет")
    y = input()
    if (y == "да"):
        f = 1
    if (y == "нет"):
        f = 0
    elif (y != "да" and y != "нет"):
        n = 1
        while (n == 1):
            print("Введите \"да\" или \"нет\"")
            y = input()
            if (y == "нет"):
                f = 0
                n = 0
            if (y == "да"):
                f = 1
                n = 0
print('=' * 40)
print("Спасибо за игру!")
print('=' * 40)
quit()

