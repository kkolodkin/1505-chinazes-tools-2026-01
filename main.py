import test
import pokemon


def print_menu():
    print(
'''
============================
Menu options

1. Run Test Module
2. Who's That Pokémon?
3. Exit
============================
''')


print("Hello! Welcome to Chinazes Tools!")

while True:
    print_menu()
    user_choice = input("Select a menu option number: ")
    print()

    if user_choice == "1":
        test.run()
    elif user_choice == "2":
        pokemon.run()
    elif user_choice == "3":
        print("Bye!")
        break
    else:
        print("Invalid choice. Try again.")