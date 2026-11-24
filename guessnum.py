import random

def play_guess_game():
    print("=== ИГРА УГАДАЙ ЧИСЛО ===")
    while True:
        random_number = random.randint(-100, 100)
        attempt_count = 0
        while True:
            try:
                user_number = int(input("Введите число: "))
            except ValueError:
                print("Пожалуйста, введите целое число.")
                continue

            attempt_count += 1

            if user_number < random_number:
                print("Ваше число меньше загаданного, попробуйте еще раз!")
            elif user_number > random_number:
                print("Ваше число больше загаданного, попробуйте еще раз!")
            else:
                print(f"Поздравляю! Вы угадали число {random_number}! Количество попыток: {attempt_count}")
                answer = input("Хотите попробовать сначала? (Y/N): ").strip().lower()
                if answer != 'y':
                    return
                break

def run():
    print("=== ИГРА УГАДАЙ ЧИСЛО ===")
    while True:
        print("1. Играть в игру")
        print("2. Выйти из игры")
        choice = input("Выберите вариант: ").strip()
        if choice == '1':
            play_guess_game()
        elif choice == '2':
            print("Выход из игры...")
            break
        else:
            print("Неверный ввод. Введите Y или N.")
