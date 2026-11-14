import guessnum
def main_menu():
    while True:
        print("ГЛАВНОЕ_МЕНЮ=============")
        print("1.Играть в 'Угадай число'")
        print("2.Выйти из приложения")
        choice = int(input("Введите номер варианта: "))
        if choice == 1:
            guessnum.play_guess_game()
        elif choice == 2:
            print("Осуществлен выход")
            break
        elif choice != 1 or choice != 2:
            print("Введите 1 или 2")
if __name__ == "__main__ ":
    main_menu()
