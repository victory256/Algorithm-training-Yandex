""" Описание задачи:
За многие годы заточения узник замка Иф проделал в стене прямоугольное отверстие размером D × E.
Замок Иф сложен из кирпичей, размером A × B × C. Определите, сможет ли узник
выбрасывать кирпичи в море через это отверстие, если стороны кирпича должны быть
параллельны сторонам отверстия.

Формат ввода: Программа получает на вход числа A, B, C, D, E.

Формат вывода: Программа должна вывести слово YES или NO.
"""


def prisoner(a: int, b: int, c: int, d: int, e: int) -> str:
    """
    Функция prisoner определяет получится YES или NO, выбрасывать кирпичи через
    проделанное отверстие.

    Example :
     :>>> prisoner(1, 1, 1, 1, 1) -> YES

     :>>> prisoner(2, 2, 2, 1, 1) -> NO

    :param a: 1 размер кирпича
    :param b: 2 размер кирпича
    :param c: 3 размер кирпича
    :param d: 1 размер отверстия
    :param e: 2 размер отверстия
    :return: YES или NO, получится ли выбрасывать кирпичи через проделанное отверстие
    """
    d, e = min(d, e), max(d, e)
    x = sorted([a, b, c])
    a, b, c = x[0], x[1], x[2]
    if a <= d and b <= e:
        return 'YES'
    else:
        return 'NO'


a_input = int(input())
b_input = int(input())
c_input = int(input())
d_input = int(input())
e_input = int(input())
print(prisoner(a_input, b_input, c_input, d_input, e_input))
