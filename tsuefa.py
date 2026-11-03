# Камень-ножницы-бумага
import random

def parse(command): # человеческая команда в номер выбора
    if command == "к":
        return 1
    elif command == "н":
        return 2
    elif command == "б":
        return 3
    elif command == "в":
        return 4
    else:
        return 0
        
# 1 - камень, 2 - ножницы, 3 - бумага
# камень > ножницы > бумага > камень
# 1-2 / 2-3 / 3-1
# 2-1 / 3-2 / 1-3

def battle(a, b): # расчет исхода битвы
    if a == b:
        return 0
    elif (a == 1 and b == 2) or (a == 2 and b == 3) or (a == 3 and b == 1):
        return 1
    elif (a == 2 and b == 1) or (a == 3 and b == 2) or (a == 1 and b == 3):
        return 2

def tsuefa(): # главный цикл
    while True:
        user_input = parse(input("Введите свой выбор ([к]амень, [н]ожницы, [б]умага, [в]ыход): "))
        if user_input == 0:
            print("Неверный ввод")
        else:
            if user_input == 4:
                break
            else:
                bot_input = random.randint(1, 3)
                win = battle(user_input, bot_input)
                if win == 0:
                    print("Ничья.")
                elif win == 1:
                    print("Вы победили!")
                elif win == 2:
                    print("Вы проиграли...")

# tsuefa()
# ^^^^^^^^ раскомментировать для дебага
