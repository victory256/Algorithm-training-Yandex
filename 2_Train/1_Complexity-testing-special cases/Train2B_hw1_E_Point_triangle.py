""" Описание задачи:
На координатной плоскости расположены равнобедренный прямоугольный треугольник ABC с
длиной катета d и точка X. Катеты треугольника лежат на осях координат, а вершины расположены
в точках: A (0,0), B (d,0), C (0,d).
Напишите программу, которая определяет взаимное расположение точки X и треугольника.
Если точка X расположена внутри или на сторонах треугольника, выведите 0.
Если же точка находится вне треугольника, выведите номер ближайшей к ней вершины.

Формат ввода:
Сначала вводится натуральное число d (не превосходящее 1000), а затем координаты
точки X – два целых числа из диапазона от - 1000 до 1000.

Формат вывода:
Если точка лежит внутри, на стороне треугольника или совпадает с одной из вершин,
то выведите число 0. Если точка лежит вне треугольника, то выведите номер вершины треугольника,
к которой она расположена ближе всего (1 – к вершине A, 2 – к B, 3 – к C).
Если точка расположена на одинаковом расстоянии от двух вершин, выведите ту вершину,
номер которой меньше.
"""


def point_triangle(d: int, x1: int, x2: int) -> int:
    """
    Функция point_triangle вычисляет ближайшую вершину треугольника для точки (x1,x2)

    Example :
     :>>> point_triangle(5, 1, 1) -> 0
     Точка лежит внутри треугольника

     :>>> point_triangle(3, -1, -1) -> 1
     Точка лежит вне треугольника и ближе всего к ней вершина A

     :>>> point_triangle(4, 4, 4) -> 2
     Точка лежит на равном расстоянии от вершин B и C,в этом случае нужно вывести
     ту вершину, у которой номер меньше, т.е. выведено должно быть число 2

     :>>> point_triangle(4, 2, 2) -> 0
     Точка лежит на стороне треугольника.

    :param d: длинна катета
    :param x1: координата точки
    :param x2: координата точки
    :return: номер ближайшей вершины 0 - внктри треугольника 1 – к вершине A, 2 – к B, 3 – к C
    """
    a_1 = 0
    b_2 = 0
    c_3 = 0
    if x2 > -x1 + d:
        a_1 = 2 if (abs((x1 - d) ** 2 + (x2 - 0) ** 2)) ** 0.5 <= (abs((x1 - 0) ** 2 + (x2 - d) ** 2)) ** 0.5 else 3
    if x1 < 0:
        b_2 = 1 if (abs((x1 - 0) ** 2 + (x2 - 0) ** 2)) ** 0.5 <= (abs((x1 - 0) ** 2 + (x2 - d) ** 2)) ** 0.5 else 3
    if x2 < 0:
        c_3 = 1 if (abs((x1 - 0) ** 2 + (x2 - 0) ** 2)) ** 0.5 <= (abs((x1 - d) ** 2 + (x2 - 0) ** 2)) ** 0.5 else 2
    if x1 >= 0 and x2 >= 0 and x2 + x1 <= d:
        return 0
    else:
        return min(filter(lambda s: s > 0, [a_1, b_2, c_3]))


d_input = int(input())
x1_input, x2_input = map(int, input().split())
print(point_triangle(d_input, x1_input, x2_input))
