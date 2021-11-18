""" Описание задачи:
Решите в целых числах уравнение: sqrt(a*x+b)=c
a, b, c – данные целые числа:
найдите все решения или сообщите, что решений в целых числах нет.
Формат ввода: Вводятся три числа a, b и c по одному в строке.
Формат вывода: Программа должна вывести все решения уравнения
в порядке возрастания, либо NO SOLUTION (заглавными буквами), если решений нет.
Если решений бесконечно много, вывести MANY SOLUTIONS.
"""


def equation_with_root(a: int, b: int, c: int) -> str:
    """
    Функция equation_with_root вычисляет корень иррационального уравнения
    или сообщает, что их много или нет.

    Example :
     :>>> equation_with_root(1, 0, 0) -> 0

     :>>> equation_with_root(1, 2, 3) -> 7

     :>>> equation_with_root(1, 2, -3) -> NO SOLUTION

    :param a: целое число
    :param b: целое число
    :param c: целое число
    :return: {число, No Solution, Many Solution},решение уравнения
    """
    if c < 0 or (a == 0 and (c * c - b) != 0):
        return 'NO SOLUTION'
    else:
        if a == 0 and (c * c - b) == 0:
            return 'MANY SOLUTIONS'
        else:
            if (c * c - b) % a:
                return 'NO SOLUTION'
            else:
                return str(int((c * c - b) / a))


a_input = int(input())
b_input = int(input())
c_input = int(input())
print(equation_with_root(a_input, b_input, c_input))
