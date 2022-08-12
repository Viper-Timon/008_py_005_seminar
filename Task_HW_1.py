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

min_st = 1  # мин ход - для универсальности решения
max_st = 28  # макс ход - для универсальности решения
cand_num = 2021  # для универсальности решения
n = 0
play_list = ['SkyNET']
play_list.append(str(input('Введите свой nickname -> ')))
os.system('cls')
print(f'Против вас играет {play_list[0]}')
p_flag = rnd.randint(0, 1)
p_flag = 1  # test

print(f'Начинает игрок {play_list[p_flag]}')

while cand_num > 0:
    print(f'\nОстаток конфет {cand_num} шт.')
    count = 0  # счетчик попыток игрока

    if p_flag == 0:
        n = cand_num % (max_st+1)
        if n == 0 or (min_st < n > max_st): 
            n = rnd.randint(min_st, max_st)

        print(f'Игрок {play_list[p_flag]} берет {n} конфет')
        p_flag = 1

    else:
        while not((min_st-1) < n < (max_st + 1)):

            n = int(input(f'Заберите от {min_st} до {max_st} конфет\n'))
            count += 1

            if count == 10:
                n = cand_num % (max_st+1)
                if n == 0 or (min_st < n > max_st):
                    n = rnd.randint(min_st, max_st)
                print(
                    f'Игрок {play_list[not(p_flag)]} ' +
                    f'помогает игроку {play_list[p_flag]}\nи подсказывает, что нужно забрать {n} конфет')

        p_flag = 0

    cand_num = cand_num - n
    n = 0

    if cand_num < max_st:
        max_st = cand_num

    if cand_num == 0:
        print(f'Победил игрок {play_list[not(p_flag)]}')
