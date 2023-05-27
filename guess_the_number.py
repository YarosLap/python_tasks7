import random

def game(pmax,n):
    print("Угадайте число от 1 до ",n, " за ",pmax," попыток")
    a = random.randint(1,n)
    b = -1
    p = 1
    while a != b:
        b = int(input("Ваш вариант = "))
        p = p + 1
        if b<a:
            print("больше")
        elif b>a:
            print("меньше")
        else:
            print("угадали с ",p," попытки")
    if p <= pmax:
        print("Вы прошли уровень!")
        rez = 1
    else:
        print("Вы проиграли. Играем снова этот уровень.")
        rez = 0
    return rez

print("Игра угадай число")

print("Уровень 1")
win = 0
while win == 0:
    win = game(4,10)

print("Уровень 2")
win = 0
while win == 0:
    win = game(7,100)

print("Уровень 3")
win = 0
while win == 0:
    win = game(10,1000)
print("Игра окончена")
