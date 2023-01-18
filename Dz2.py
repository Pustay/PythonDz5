# Создайте программу для игры в 'Крестики-нолики'
# НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом

import random
from tkinter import *
root = Tk() # Создаю окно с заголовком
root.title('Крестики-нолики')
game_run = True    
field = []          # в массиве храним состояние поля
cross = 0     # Подсчитываем количество крестиков на поле, максимально 5
def game():     # поле и переменные обнуляются
    for row in range(3):
        for col in range(3):
            field[row][col]['text'] = ' '
            field[row][col]['background'] = 'lavender'
    global game_run
    game_run = True
    global cross
    cross = 0
def click(row, col):        # ставим крестик и считаем
    if game_run and field[row][col]['text'] == ' ':
        field[row][col]['text'] = 'X'
        global cross
        cross += 1
        check_win('X')      # проверка на победу
        if game_run and cross < 5:
            bot_move()
            check_win('O')  # проверка на победу
def check_win(win):
    for x in range(3):
        check(field[x][0], field[x][1], field[x][2], win)
        check(field[0][x], field[1][x], field[2][x], win)
    check(field[0][0], field[1][1], field[2][2], win)
    check(field[2][0], field[1][1], field[0][2], win)
def check(a, b, c, win):
    if a['text'] == win and b['text'] == win and c['text'] == win:
        a['background'] = b['background'] = c['background'] = 'pink'
        global game_run
        game_run = False
def can_win(a, b, c, win):   # проверка на победу
    res = False
    if a['text'] == win and b['text'] == win and c['text'] == ' ':
        c['text'] = 'O'
        res = True
    if a['text'] == win and b['text'] == ' ' and c['text'] == win:
        b['text'] = 'O'
        res = True
    if a['text'] == ' ' and b['text'] == win and c['text'] == win:
        a['text'] = 'O'
        res = True
    return res
def bot_move():
    for x in range(3):
        if can_win(field[x][0], field[x][1], field[x][2], 'O'):
            return
        if can_win(field[0][x], field[1][x], field[2][x], 'O'):
            return
    if can_win(field[0][0], field[1][1], field[2][2], 'O'):
        return
    if can_win(field[2][0], field[1][1], field[0][2], 'O'):
        return
    while True:  # случ. образом перебираются поля, пока не выпадет свободное
        row = random.randint(0, 1)
        col = random.randint(0, 1)
        if field[row][col]['text'] == ' ':
            field[row][col]['text'] = 'O'
            break
for row in range(3):  # создаем поле кнопок
    line = []
    for col in range(3):
        button = Button(text=' ', width=6, height=3,
                        font=('misty rose', 28, 'bold'),
                        background='medium purple',
                        command=lambda row=row, col=col: click(row, col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    field.append(line)
new_button = Button(text='Новая игра', command=game)
new_button.grid(row=3, column=0, columnspan=3, sticky='nsew')
root.mainloop()