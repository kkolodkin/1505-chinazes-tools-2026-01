RU = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
EN = "abcdefghijklmnopqrtsuvwxyz"

def encrypt(text, n): # текст и сдвиг
    table = {}
    for i in (RU, RU.upper(), EN, EN.upper()):
        k = n % len(i)
        table.update(str.maketrans(i, i[k:] + i[:k]))
    return text.translate(table)

def decrypt(text, n):
    return encrypt(text, -n) # все гениальное факинг просто
