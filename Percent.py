import random

print("=" * 60)
print("Тест на уровень интуиции")   
print("Программа будет по-очереди загадывать числовые значения.")
print("Цель: постараться угадать загаданные числа.")

playGame = bool(True)

#f = 1
while (playGame):
    i = int(0)          # счетчик выхода из внутреннего цикла 
    l = 0           # счетчик удачных угадываний
    prs = int(0)    # коэфициент
    summ = 0        # переменная для суммироания процента из каждой итерации
    area = int(10)     # верхняя граница диапазона
    iter = int(10)       # колличество повторов

    print("=" * 60)
    print("Введите по очереди " + str(iter) +  " чисел в диапазоне от \"1\" до", area)
    
    for i in range(iter):
        target = random.randint(1, area)
        g = int(0)
        while (g == 0):
            try:
                digit = int(input())
                if (digit > area or digit < 1):
                    print("Необходимо ввести число от \"1\" до", area)
                    g = 0
                else:
                    g = 1
            except:
                print("Необходимо ввести число от \"1\" до", area)
                g = 0
        
        rp = 0
        i += 1
        rp = abs(target - digit)                    # находим разницу между загаданным и угаданным
        rez = (rp * 100 / area)             # приводим эту разницу к единой шкале относительно area
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
    ball = summ + prs
    lp = (iter / 100 * l) * 100 #процент угадывания

    if (percent <= 50):
        pns = "крайне низкий"
    if (percent >= 50 and percent < 60):
        pns = "ниже среднего"
    if (percent >= 60 and percent < 80):
        pns = "в пределах среднестатистического"
    if (percent >= 80 and percent < 90):
        pns = "выше среднего"
    if (percent >= 90 and percent < 100):
        pns = "высокий"
    if (percent >= 100):
        pns = "очень высокий"
    if (lp >= 70):
        pns = "запредельный"
    if(lp >= 100):
    	 pns = "забыли отключить чит мод?"
    
    print("*" * 60)
    print("РЕЗУЛЬТАТ:")
    print("Колличество полных совпадений:", l)
    print("Уровень вашей интуиции:", str(pns))
    print("Начислено всего очков:", ball)
    print("*" * 60)
    if (input("Enter - играть еще, 0 - выход   ") == "0"):
	    playGame = False
    
   
print('=' * 40)
print("Спасибо за игру!")
print('=' * 40)
quit()

