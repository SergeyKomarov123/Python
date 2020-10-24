import random

def getIntInput(min, max, message):      # функция для обработки вводимого значения
    ret = -1
    while(ret > max or ret < down):
        print(message)
        dig = input()
        if (dig.isdigit()):
            ret = int(dig)
    return ret

def getResult(percent):                   # функция вывода описания результата
    if (percent <= 50):
        pns = "крайне низкий"
    elif (percent >= 50 and percent < 60):
        pns = "ниже среднего"
    elif (percent >= 60 and percent < 80):
        pns = "в пределах среднестатистического"
    elif (percent >= 80 and percent < 90):
        pns = "выше среднего"
    elif (percent >= 90 and percent < 100):
        pns = "высокий"
    elif (percent >= 100):
        pns = "очень высокий"
    elif (lp >= 70):
        pns = "запредельный"
    elif(lp >= 100):
    	 pns = "забыли отключить чит мод?"
    return pns

def topResultRW(x):                                 # функция записывающая имя игрока и рекорд
    try:
        f = open("TOP.dat", "r")
        m = int(f.readline())
        f.close()
    except FileNotFoundError:
        print("Файла не существует")
    if (x > m):
        a = input("Введите имя _")
        f = open("TOP.dat", "w")
        f.write(str(ball) + "\n")
        f.write(str(a))
        f.close()
        m = int(x)
    return m

def retUser():                                         # функция возвращающая имя игрока которому принадлежит последний рекорд
    f = open("TOP.dat", "r")
    m = f.readline()
    m = f.readline()
    f.close()
    return m

print("=" * 60)
print("Тест на уровень интуиции")   
print("Программа будет по-очереди загадывать числовые значения.")
print("Цель: постараться угадать загаданные числа.")

playGame = bool(True)
while (playGame):

    i = int(0)          # счетчик выхода из внутреннего цикла
    l = 0           # счетчик удачных угадываний
    prs = int(0)    # коэфициент
    summ = int(0)        # переменная для суммироания процента из каждой итерации
    down = int(1)   # нижняя граница диапазона
    upper = int(10)     # верхняя граница диапазона
    iter = int(10)       # колличество повторов
    print("=" * 60)
    print("Введите по очереди " + str(iter) +  " чисел в диапазоне от \"1\" до", upper)

    for i in range(iter):
        target = random.randint(down, upper)
        digit = getIntInput(down, upper, f"Введите число от {down} до {upper}")

        i += 1
        rp = abs(int(target - digit))                    # находим разницу между загаданным и угаданным
        rez = (rp * 100 / upper)             # приводим эту разницу к единой шкале относительно area
        itogo = 100 - rez
        if (target == digit):
            l +=1               # считаем количество 100% совпадений
            prs += 5            # расчитываем коэфициент
        summ += itogo

        print("Загаданое число:", target, "Ваш ответ:", digit)
        u = iter - i
        if (u != 0):
        	print("Осталось шагов:", u)

    percent = int(summ / iter + prs)
    ball = int(summ + prs)
    #lp = (iter / 100 * l) * 100 #процент угадывания
    pns = getResult(percent)
    trrw = int(topResultRW(ball))
    userName = retUser()

    print("*" * 60)
    print("РЕЗУЛЬТАТ:")
    print("Колличество полных совпадений:", l)
    print("Уровень вашей интуиции:", str(pns))
    print("Ваш результат:", str(ball), "баллов")
    print(f"Игрок с лучшим результатом за все время:", userName, "-", str(trrw), "баллов")
    print("*" * 60)
    if (input("Enter - играть еще, 0 - выход   ") == "0"):
	    playGame = False
    
print('=' * 40)
print("Спасибо за игру!")
print('=' * 40)
quit()

