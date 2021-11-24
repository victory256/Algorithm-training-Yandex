""" Описание задачи:
Напишите программу, которая по изображению поля для игры в «Крестики-нолики» определит,
могла ли такая ситуация возникнуть в результате игры с соблюдением всех правил.
Напомним, что игра в «Крестики-нолики» ведется на поле 3*3. Два игрока ходят по очереди.
Первый ставит крестик, а второй – нолик. Ставить крестик и нолик разрешается в
любую еще не занятую клетку поля. Когда один из игроков поставит три своих знака
в одной горизонтали, вертикали или диагонали, или когда все клетки поля окажутся заняты,
игра заканчивается.

Формат ввода:
Вводится три строки по три числа в каждой, описывающих игровое поле.
Число 0 обозначает пустую клетку, 1 – крестик, 2 – нолик.
Числа в строке разделяются пробелами.

Формат вывода:
Требуется вывести слово YES, если указанная ситуация могла возникнуть
в ходе игры, и NO в противном случае.
"""


def noughts_crosses(field: list) -> str:
    """
    Функция noughts_crosses определяет возможна ли ситуация field во время игры

    Example :
     :>>> noughts_crosses([[1, 1, 1,
                           [1, 1, 1]
                           [1, 1, 1]]) -> NO

     :>>> noughts_crosses([[2, 1, 1,
                           [1, 1, 2]
                           [2, 2, 1]]) -> YES

     :>>> noughts_crosses([[1, 1, 1,
                           [2, 0, 2]
                           [0, 0, 0]]) -> YES

     :>>> noughts_crosses([[0, 0, 0,
                           [0, 1, 0]
                           [0, 0, 0]]) -> YES

    :param field: поле игры
    :return: {YES, NO} являются ли вершинами параллелограмма
    """
    # print(field)
    kol_1_line = 0
    kol_2_line = 0
    kol_1 = 0
    kol_2 = 0
    for i in range(3):
        # кол-во единиц и двоек на поле
        kol_1 = kol_1 + len([k for k in field[i] if k == 1])
        kol_2 = kol_2 + len([k for k in field[i] if k == 2])
        # кол-во вычеркнутых строк
        if len(set(field[i])) == 1:
            if field[i][0] == 1:
                kol_1_line = kol_1_line + 1
            if field[i][0] == 2:
                kol_2_line = kol_2_line + 1
        # кол-во вычеркнутых столбцов
        if len({field[0][i], field[1][i], field[2][i]}) == 1:
            if field[0][i] == 1:
                kol_1_line = kol_1_line + 1
            if field[0][i] == 2:
                kol_2_line = kol_2_line + 1
    # проверка главной диагонали
    if len({field[0][0], field[1][1], field[2][2]}) == 1:
        if field[1][1] == 1:
            kol_1_line = kol_1_line + 1
        if field[1][1] == 2:
            kol_2_line = kol_2_line + 1
    # проверка побочной диагонали
    if len({field[2][0], field[1][1], field[2][0]}) == 1:
        if field[1][1] == 1:
            kol_1_line = kol_1_line + 1
        if field[1][1] == 2:
            kol_2_line = kol_2_line + 1
    # print(kol_1_line, kol_2_line, kol_1, kol_2)
    if (kol_1 - kol_2 == 1 and kol_1_line <= 2 and kol_2_line == 0) or (
            kol_1 - kol_2 == 0 and kol_1_line == 0 and kol_2_line <= 1):
        return 'YES'
    else:
        return 'NO'


field_input = []
for _ in range(3):
    field_input.append(list(map(int, input().split())))
print(noughts_crosses(field_input))
