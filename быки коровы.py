import random

def generate():
    digits = list('0123456789')
    random.shuffle(digits)
    if digits[0] == '0':
        digits[0], digits[4] = digits[4], digits[0]
    return ''.join(digits[:4])


def check(secret, guess):
    b = 0
    k = 0
    for i in range(4):
        if guess[i] == secret[i]:
            b += 1
        elif guess [i] in secret:
            k += 1
    return b, k



def play():
    print('Добро пожаловать в игру <Быки коровы>!')
    print('Компьютер загадал 4-значоне число сразными цифрами')
    print('Попробуйте его угададтью Удчи!\n')
    secret = generate()
    att = 0
    while True:
        guess = input('Введите 4-значное число: ')
        if len(guess) != 4 or not guess.isdigit() or len(set(guess)) != 4:
            print('Ты ошибка! Введите ровно 4 уникальные цифры.')
            continue
        att += 1
        b, k = check(secret, guess)
        print(f'{b} бык(а/ов) и {k} коров(ы)')
        if b == 4:
            print(f'\n Поздравляем! Вы угадали число {secret} за {att} попыток!')
if __name__ == '__main__':
    play()
