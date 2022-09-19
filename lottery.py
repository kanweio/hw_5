from random import choice
lst = [i for i in range(1, 31)]
def stavka(lot, amount):
    win_lot = choice(lst)
    if lot == win_lot:
        print(f'выигранно {amount * 2}$ :)')
        return amount * 2
    print(f'проигранно {amount}$')
    return -amount
if __name__ == '__main__':
    print(lst)