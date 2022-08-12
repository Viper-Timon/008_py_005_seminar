# 2. Создайте программу для игры в ""Крестики-нолики"".

import random
import os

os.system('cls')

a = [['*', '*', '*'],
     ['*', '*', '*'],
     ['*', '*', '*']]
p_list = ['x', 'o']
play_flag = random.randint(0, 1)

print(f'первыми ходят {p_list[play_flag]}-ки')

for step in range(9):
    m, n = 0, 0
    empt_flag=0

    for i in a:
        print(*i)

    while not(0<m<4) or not(0<n<4) or not(empt_flag==1)==1:
        m, n = map(int, input(f'Куда поставить {p_list[play_flag]}? ').split(' '))
               
        for i in range(len(a)):
            for j in range(len(a[i])):
                b = a[i]
                if i == m-1 and j == n-1 and b[j]=='*':
                    b[j] = p_list[play_flag]
                    a[i] = b
                    empt_flag=1
            
    os.system('cls')
        
    c = [k for lev_1 in a for k in lev_1]

    if c[0] == c[3] == c[6] == p_list[play_flag] \
        or c[1] == c[4] == c[7] == p_list[play_flag] \
        or c[2] == c[5] == c[8] == p_list[play_flag] \
        or c[0] == c[1] == c[2] == p_list[play_flag] \
        or c[3] == c[4] == c[5] == p_list[play_flag] \
        or c[6] == c[7] == c[8] == p_list[play_flag] \
        or c[0] == c[4] == c[8] == p_list[play_flag] \
        or c[2] == c[4] == c[6] == p_list[play_flag]:
        print(f'Победили {p_list[play_flag]}-ки')
        for i in a:
            print(*i)
        break
        
    elif step == 8:
        print('Ничья')
        for i in a:
            print(*i)

    
    if play_flag==0:play_flag=1
    else: play_flag=0

    