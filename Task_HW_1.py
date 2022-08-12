# 1. Создайте программу для игры с конфетами
# человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?

#     a) Добавьте игру против бота

#     b) (доп) Подумайте как наделить бота ""интеллектом""


import random as rnd
import os

cand_num = 2021
n = 0
play_list = ['SkyNET']
play_list.append(str(input('Введите свой nickname -> ')))
os.system('cls')
print(f'Против вас играет {play_list[0]}')
#p_flag = rnd.randint(0, 1)
p_flag = 0

print(f'Начинает игрок {play_list[p_flag]}')

while cand_num > 0:
    print(f'\nОстаток конфет {cand_num} шт.')
    count = 0  # счетчик попыток игрока

    if p_flag == 0:

        n = cand_num % 29
        if n == 0:
            n = rnd.randint(1, 28)

        cand_num = cand_num - n
        print(f'Игрок {play_list[p_flag]} берет {n} конфет')
        p_flag = 1

    else:
        while not(0 < n < 29) == True:
            n = int(input('Введите кол-во конфет от 1 до 28\n'))
            count += 1
            if count == 10:
                n = cand_num % 29
                if n == 0:
                    n = rnd.randint(1, 28)
                print(
                    f'Игрок {play_list[not(p_flag)]} помогает игроку {play_list[p_flag]}\nи забирает {n} конфет')

            cand_num = cand_num - n
        p_flag = 0

    if cand_num == 0:
        print(f'Победил игрок {play_list[not(p_flag)]}')
    n = 0
