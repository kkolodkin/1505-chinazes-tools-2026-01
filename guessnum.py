import random
while True:
    random_namber = random.randint(-101,101)
    attempt_count = 0
    print("Угадай число!")
    while True:
        user_number = int(input("Ввeдите число!: "))
        if user_number == random_namber:
            print(f"Вы угадали число!\nКоличество попыток: {attempt_count}\n ")
            user_answer = str(input("Хотите сыграть еще раз?:"))
            if user_answer == "Yes" or user_answer == "Y" or user_answer == "yes" or user_answer == "y":
                break
            else:
                exit()
        elif user_number > random_namber and -101 < user_number < 101:
            print("Ваше число больше загаданного числа!\nПовторите попытку!")
            attempt_count +=1
        elif user_number < random_namber and -101 < user_number < 101:
            print("Ваше число меньше загаданного числа!\nПовторите попытку!")
            attempt_count +=1
        else:
            print("Ваше число не входит в диапазон\nДиапазон считается от -100 до 100")
            
# Перепиши, чтобы это импортировалось как модуль. Дай нейронке для примера любой другой модуль из репы. А команда exit() полностью закрывает программу, чего нам не надо        
        
        
        
