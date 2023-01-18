# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит заданное количество конфет.
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента 
# достаются сделавшему последний ход.

# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'

# Человек против человека

#from random import randint
#def input_dat(name):
#    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
#    while x < 1 or x > 28:
#        x = int(input(f"{name}, введите корректное количество конфет: "))
#    return x
#def p_print(name, y, counter, check):
#    print(f"Ходил {name}, он взял {y}, теперь у него {counter}. Осталось на столе {check} конфет.")
#player1 = input("Введите имя первого игрока: ")
#player2 = input("Введите имя второго игрока: ")
#check = int(input("Введите количество конфет на столе: "))
#turn = randint(0, 1)  
#if turn:
#    print(f"Первый ходит {player1}")
#else:
#    print(f"Первый ходит {player2}")
#counter1 = 0
#counter2 = 0
#while check > 28:
#    if turn:
#        y = input_dat(player1)
#        counter1 += y
#        check -= y
#        turn = False
#        p_print(player1, y, counter1, check)
#    else:
#        y = input_dat(player2)
#        counter2 += y
#        check -= y
#        turn = True
#        p_print(player2, y, counter2, check)
#if turn:
#    print(f"Выиграл {player1}")
#else:
#    print(f"Выиграл {player2}")

# Человек против бота (Вариант а)

#from random import randint
#def input_dat(name):
#    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
#    while x < 1 or x > 28:
#        x = int(input(f"{name}, введите корректное количество конфет: "))
#    return x
#def p_print(name, y, counter, check):
#    print(f"Ходил {name}, он взял {y}, теперь у него {counter}. Осталось на столе {check} конфет.")
#player1 = input("Введите своё имя: ")
#player2 = "Bot"
#check = int(input("Введите количество конфет на столе: "))
#turn = randint(0, 1)
#if turn:
#    print(f"Первый ходит {player1}")
#else:
#    print(f"Первый ходит {player2}")
#counter1 = 0
#counter2 = 0
#while check > 28:
#    if turn:
#        y = input_dat(player1)
#        counter1 += y
#        check -= y
#        turn = False
#        p_print(player1, y, counter1, check)
#    else:
#        y = randint(1, 29)
#        counter2 += y
#        check -= y
#        turn = True
#        p_print(player2, y, counter2, check)
#if turn:
#    print(f"Выиграл {player1}")
#else:
#    print(f"Выиграл {player2}")

# Человек против бота (Вариант б)

from random import randint
def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x
def p_print(name, y, counter, check):
    print(f"Ходил {name}, он взял {y}, теперь у него {counter}. Осталось на столе {check} конфет.")
def bot_intel(check):
    y = randint(1, 29)
    while check-y <= 28 and check > 29:
        y = randint(1, 29)
    return y
player1 = input("Введите своё имя: ")
player2 = "Bot"
check = int(input("Введите количество конфет на столе: "))
turn = randint(0, 1) 
if turn:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")
counter1 = 0
counter2 = 0
while check > 28:
    if turn:
        y = input_dat(player1)
        counter1 += y
        check -= y
        turn = False
        p_print(player1, y, counter1, check)
    else:
        y = bot_intel(check)
        counter2 += y
        check -= y
        turn = True
        p_print(player2, y, counter2, check)
if turn:
    print(f"Выиграл {player2}")
else:
    print(f"Выиграл {player1}")