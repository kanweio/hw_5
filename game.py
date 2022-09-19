import os
from envparse import env
from lottery import stavka
env.read_envfile('settings.env')
money = int(os.getenv('MY_MONEY'))

gain = 0
lost = 0
total = 0

while True:
    commands = input('введите ставку или exit для выхода').split()
    if commands[0] == 'exit':
        print(
            f'программа завершена\nоставшаяся сумма: {money} денег потеряно: {lost} денег заработано: {gain} разница: {total}')
        break
    if not 1 <= int(commands[0]) <= 30:
        print('неправильный слот для ставки\nподсказка: слот должен быть целым числом от 1 до 30')
        continue
    if int(commands[1]) > money or int(commands[1]) <= 0:
        print('неправильная сумма для ставки\nподсказка: сумма ставки должна быть целым положительным числом не '
              'больше доступного числа денег\n' + f'доступная сумма:{money}')
        continue
    result = stavka(int(commands[0]), int(commands[1]))
    if result < 0:
        lost += result
    else:
        gain += result
    total += result
    money += result
    if money == 0:
        print('вы проиграли деньги')
        break