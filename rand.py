import random

def rand():
    floor = int(input("Введите минимальное число: "))
    ceiling = int(input("Введите максимальное число: "))
    for i in range(1, int(input("Введите количество чисел: ")) + 1):
        print(random.randint(floor, (ceiling)))

rand()
