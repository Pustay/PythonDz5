# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc

def coding(txt):
    count = 1
    size = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            size = size + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        size = size + str(count) + txt[-1]
    return size
def decoding(txt):
    number = ''
    size = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            size = size + txt[i] * int(number)
            number = ''
    return size
mi_list = input("Введите текст: ")
print(f"Текст после кодировки: {coding(mi_list)}")
print(f"Текст после дешифровки: {decoding(coding(mi_list))}")