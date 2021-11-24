""" Описание задачи:
Решить в целых числах уравнение ( ax + b ) : ( cx + d ) = 0

Формат ввода:
Вводятся 4 числа: a, b, c и d; c и d не равны нулю одновременно.

Формат вывода:
Необходимо вывести все целочисленные решения, если их число конечно, “NO” (без кавычек),
если целочисленных решений нет, и “INF” (без кавычек), если их бесконечно много.
"""


def complex_equation(a: int, b: int, c: int, d: int) -> str:
    """
    Функция complex_equation вычисляет целочисленноы корень дробно-рационального
    уравнения или сообщает, что их много или нет.

    Example :
     :>>> complex_equation(1, 1, 2, 2) -> NO

     :>>> complex_equation(2, -4, 7, 1) -> 2

     :>>> complex_equation(35, 14, 11, -3) -> NO

    :param a: целое число
    :param b: целое число
    :param c: целое число
    :param d: целое число
    :return: {число, NO, INF},решение уравнения
    """
    if a == 0 and b == 0:
        return 'INF'
    elif a == 0 and b != 0:
        return 'NO'
    elif b % a != 0:
        return 'NO'
    elif c != 0 and d != 0 and a / c == b / d:
        return 'NO'
    else:
        return str(int(-b / a))


a_input = int(input())
b_input = int(input())
c_input = int(input())
d_input = int(input())
print(complex_equation(a_input, b_input, c_input, d_input))
