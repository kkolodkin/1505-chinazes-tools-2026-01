import random
randomnumber = random.randint(-101,101)
countlose = 0
print('Угадай число')
while True:
    usernumber = int(input('Введи число:'))
    if usernumber == randomnumber:
        print(f"Ты угадал число!\nЭто было {randomnumber}\n Ты использовал:{countlose} попыток ")
        break
    elif usernumber > randomnumber and usernumber in range(-101,101):
        print("Это число меньше")
        countlose +=1
    elif usernumber < randomnumber and usernumber in range(-101,101):
        print("Это число больше")
        countlose +=1
    else:
        print("Ваше число не входит в данный диапозон")
    
    
    
    

