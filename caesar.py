RU = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
EN = "abcdefghijklmnopqrtsuvwxyz"
DIGITS = "0123456789"
def encrypt(text, n):
    table = {}
    for i in (RU, RU.upper(), EN, EN.upper(), DIGITS):
        k = n % len(i)
        table.update(str.maketrans(i, i[k:] + i[:k]))
    return text.translate(table)

def decrypt(text, n):
    return encrypt(text, -n)

def run():
    com = input("Выберите режим ([ш]ифрование/[д]ешифрование): ")
    orig = input("Введите текст сообщения: ")
    n = int(input("Введите сдвиг: "))
    if com == 'ш':
        print(encrypt(orig, n))
    elif com == 'д':
        print(decrypt(orig, n))
    else:
        print("Неизвестная команда")

# в соседнем файле результат выполнения, не понимаю, в чем ошибка
