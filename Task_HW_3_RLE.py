# 3. Реализуйте RLE алгоритм:
# реализуйте модуль сжатия и восстановления данных.

def f_rle(txt):
    txt_out = ''
    count_rep = 1

    for i in range(len(txt)):
        if i == len(txt)-1:
            count_rep += 0
            txt_out += str(count_rep)+txt[i]
        elif txt[i] == txt[i+1]:
            count_rep += 1
        else:
            txt_out += str(count_rep)+txt[i]
            count_rep = 1

    count_uniq = 0
    txt_out_comp = ''
    txt_mult = ''

    for i in range(len(txt_out)-1):
        if txt_out[i].isdigit() == True:
            if txt_out[i] != '1':
                if count_uniq < 0:
                    txt_out_comp += str(count_uniq)+txt_mult
                    count_uniq = 0
                    txt_mult = ''
                txt_out_comp += txt_out[i]+txt_out[i+1]

            elif i == len(txt_out)-2:
                if count_uniq < 0:
                    count_uniq -= 1
                    txt_mult += txt_out[i+1]
                    txt_out_comp += str(count_uniq)+txt_mult
                    count_uniq = 0
                    txt_mult = ''

            elif txt_out[i] == '1':
                count_uniq -= 1
                txt_mult += txt_out[i+1]
    return txt_out_comp

def rle_ext(txt):
    txt_out = ''
    for i in range(len(txt)):
        if txt[i] == '-':
            dif = i+2
            txt_out += txt[dif:dif+int(txt[i+1])]
        else:
            if (txt[i].isdigit() == True) \
                    and (txt[i-1] != '-'):
                txt_out += int(txt[i])*txt[i+1]

    return txt_out

text_1 = 'abcabcaaaabbbcddddabcabcabcaaaaaaa'
text_2 = f_rle(text_1)
text_3 = rle_ext(text_2)

print(text_1)
print(text_2)
print(text_3)
