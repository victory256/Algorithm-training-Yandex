""" Описание задачи:
Даны числа a, b, c, d, e, f. Решите систему линейных уравнений

a*x + b*y = e,

c*x + d*y = f

Формат ввода: Вводятся 6 вещественных чисел - коэффициенты уравнений.

Формат вывода: Вывод программы зависит от вида решения этой системы.
0) Если система не имеет решений, то программа должна вывести единственное число 0.
1) Если система имеет бесконечно много решений, каждое из которых имеет вид y=kx+b,
то программа должна вывести число 1, а затем значения k и b.
2) Если система имеет единственное решение (x0,y0), то программа должна вывести число 2,
а затем значения x0 и y0.
3) Если система имеет бесконечно много решений вида x=x0, y — любое, то программа
должна вывести число 3, а затем значение x0.
4) Если система имеет бесконечно много решений вида y=y0, x — любое, то программа
должна вывести число 4, а затем значение y0.
5) Если любая пара чисел (x,y) является решением, то программа должна вывести число 5.
6) Числа x0 и y0 будут проверяться с точностью до пяти знаков после точки.
"""


def system_of_equation(a: float, b: float, c: float, d: float, e: float, f: float) -> str:
    """
    Функция system_of_equation выводит решение СЛУ в зависимости от вида решения.

    Example :
     :>>> system_of_equation(1, 0, 0, 1, 3, 3) -> 2 3 3

     :>>> system_of_equation(1, 1, 2, 2, 1, 2) -> 1 -1 1

     :>>> system_of_equation(0, 2, 0, 4, 1, 2) -> 4 0.5

    :param a: вещественное число, коэффициент СЛУ
    :param b: вещественное число, коэффициент СЛУ
    :param c: вещественное число, коэффициент СЛУ
    :param d: вещественное число, коэффициент СЛУ
    :param e: вещественное число, коэффициент СЛУ
    :param f: вещественное число, коэффициент СЛУ
    :return: решение СЛУ
    """
    det = a * d - c * b
    if det != 0:
        return '2 ' + "{:.5f}".format((e * d - b * f) / det) + ' ' + "{:.5f}".format((a * f - c * e) / det)
    elif a == 0 and b == 0 and c == 0 and d == 0 and e == 0 and f == 0:
        return '5'
    elif a == 0 and c == 0 and b != 0 and abs(b * f - d * e) <= 0.000001:
        return '4 ' + "{:.5f}".format(e / b)
    elif a == 0 and c == 0 and d != 0 and abs(b * f - d * e) <= 0.000001:
        return '4 ' + "{:.5f}".format(f / d)
    elif a != 0 and b == 0 and d == 0 and abs(a * f - c * e) <= 0.000001:
        return '3 ' + "{:.5f}".format(e / a)
    elif c != 0 and b == 0 and d == 0 and abs(a * f - c * e) <= 0.000001:
        return '3 ' + "{:.5f}".format(f / c)
    elif b != 0 and abs(a * d - c * b) <= 0.000001 and abs(a * f - c * e) <= 0.000001 and abs(
            b * f - d * e) <= 0.000001:
        return '1 ' + "{:.5f}".format(-a / b) + ' ' + "{:.5f}".format(e / b)
    elif d != 0 and abs(a * d - c * b) <= 0.000001 and abs(a * f - c * e) <= 0.000001 and abs(
            b * f - d * e) <= 0.000001:
        return '1 ' + "{:.5f}".format(-c / d) + ' ' + "{:.5f}".format(f / d)
    else:
        return '0'


a_input = float(input())
b_input = float(input())
c_input = float(input())
d_input = float(input())
e_input = float(input())
f_input = float(input())
print(system_of_equation(a_input, b_input, c_input, d_input, e_input, f_input))
