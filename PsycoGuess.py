import random


psyZ = [0]
psyO = [0]
psyT = [0]
usersnumbs = []

while True:
    if not len(usersnumbs)>0:
        print('Загадайте двухзначное число (больше 10!)')
    else:
        print('Загадайте двухзначное число (больше 10!) Уже загадывали -'+str(usersnumbs))

    def call_extrs():
        # psyZ Загадывает только чётные числа
        psyzanswer = random.randrange(10, 100, 2)
        psyZ.append(psyzanswer)

        # psyO Загадывает только нечётные числа
        psyoanswer = random.randrange(10 // 2, 100 // 2) * 2 + 1
        psyO.append(psyoanswer)

        # psyT Загадывает только десятки
        psytanswer = random.randrange(10, 100, 10)
        while psytanswer == psyzanswer:
            psytanswer = random.randrange(10, 100, 10)
            # print('Совпадение!')
        psyT.append(psytanswer)
        print(f'Догадки экстрасенсов: Zero - {psyzanswer}, One - {psyoanswer}, Two - {psytanswer}')
        users_number = input('Введите двухзначное загаданное число (больше 10): ')
        while True:
            if users_number.isdigit() == False or not 3 > len(users_number) > 1 or int(users_number[0])==0:
                users_number = input('Введите двухзначное(!) загаданное число(!) больше 10(!): ')
            else:
                usersnumbs.append(users_number)
                break

        if int(users_number) == psyzanswer:
            psyZ[0] += 1
            psyT[0] -= 1
            psyO[0] -= 1
        elif int(users_number) == psyoanswer:
            psyZ[0] -= 1
            psyT[0] -= 1
            psyO[0] += 1
        elif int(users_number) == psytanswer:
            psyZ[0] -= 1
            psyT[0] += 1
            psyO[0] -= 1
        else:
            psyZ[0] -= 1
            psyT[0] -= 1
            psyO[0] -= 1
        print(f'* * * РЕЗУЛЬТАТЫ * * *\n'
              f'Достоверность Zero: {str(psyZ[0])}, история догадок - {str(psyZ[1::])}\n'
              f'Достоверность One: {str(psyO[0])}, история догадок - {str(psyO[1::])}\n'
              f'Достоверность Two: {str(psyT[0])}, история догадок - {str(psyT[1::])}\n'
              f'* * * * * * * * * * * *')

    call_extrs()
