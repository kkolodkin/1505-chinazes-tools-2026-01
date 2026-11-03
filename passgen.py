import secrets
import string

SPECIAL = "!@#\"$%^&*()_=-_+{}:|\\<>?,./;'[]`~"
MIN = 1
MAX = 100

def passgen(len, digits, special, upper):
    chars = string.ascii_lowercase
    if digits:
        chars += string.digits
    if special:
        chars += SPECIAL
    if upper:
        chars += string.ascii_uppercase

    return "".join(secrets.choice(chars) for _ in range(len))

def run():
    while True:
        userlen = input("Введите длину пароля от 1 до 100: ")
        if userlen.isdigit() and MIN <= int(userlen) <= MAX:
            len = int(userlen)
            break
        print("Неверная длина")

    digits = input("Использовать цифры? (д/н): ") == 'д'
    special = input("Использовать спецсимволы? (д/н): ") == 'д'
    upper = input("Использовать заглавные буквы? (д/н): ") == 'д'

    print("Пароль:", passgen(len, digits, special, upper))
