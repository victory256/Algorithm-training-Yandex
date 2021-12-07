""" Описание задачи:
Фермер Иван с юности следит за своим газоном. Газон можно считать плоскостью, на которой
в каждой точке с целыми координатами растет один пучок травы.

В одно из воскресений Иван воспользовался газонокосилкой и постриг некоторый прямоугольный
участок газона. Стороны этого участка параллельны осям координат, а две противоположные
вершины расположены в точках (x1, y1) и (x2, y2). Следует отметить, что пучки травы,
находящиеся на границе этого прямоугольника, также были пострижены.

Довольный результатом Иван купил и установил на газоне дождевальную установку.
Она была размещена в точке с координатами (x3, y3) и имела радиус действия струи r.
Таким образом, установка начала поливать все пучки, расстояние от которых до точки (x3, y3)
не превышало r.

Все было хорошо, но Ивана заинтересовал следующий вопрос: сколько пучков травы оказалось и
пострижено, и полито в это воскресенье?

Требуется написать программу, которая позволит дать ответ на вопрос Ивана.

Формат ввода:
В первой строке входного файла содержатся четыре целых числа x1, y1, x2, y2
(−100 000 ≤ x1 < x2 ≤ 100 000; −100 000 ≤ y1 < y2 ≤ 100 000).

Во второй строке входного файла содержатся три целых числа x3, y3, r
(−100 000 ≤ x3, y3 ≤ 100 000; 1 ≤ r ≤ 100 000)

Формат вывода:
В выходной файл необходимо вывести одно целое число — число пучков травы,
которые были и пострижены, и политы.
"""


def lawn(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int, r: int) -> int:
    """
    Функция lawn выводит число пучков травы, которые были и пострижены, и политы

    Example :
     :>>> lawn(0, 0, 5, 4, 4, 0, 3) -> 14

     - - - - - -    - пострижены
     - - - - 0 -
     - - 0 0 0 0 *
     - - 0 0 0 0 *
     - 0 0 0 0 0 * *
         @ @ @ @ @
         @ @ @ @ @
             @    -  политы

    :param x1: −100 000 ≤ x1 < x2 ≤ 100 000, координата газона
    :param y1: −100 000 ≤ y1 < y2 ≤ 100 000, координата газона
    :param x2: −100 000 ≤ x1 < x2 ≤ 100 000, координата газона
    :param y2: −100 000 ≤ y1 < y2 ≤ 100 000, координата газона
    :param x3: −100 000 ≤ x3 ≤ 100 000, координата дождевальной установки
    :param y3: −100 000 ≤ y3 ≤ 100 000, координата дождевальной установки
    :param r: 1 ≤ r ≤ 100 000, координата дождевальной установки
    :return: число пучков травы, которые были и пострижены, и политы
    """
    from math import ceil, floor
    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)
    s = 0
    for y in range(max(y1, y3 - r), min(y2, y3 + r) + 1):
        delta_x = (r ** 2 - (y3 - y) ** 2) ** 0.5
        delta_x_left = ceil(x3 - delta_x)
        delta_x_right = floor(x3 + delta_x)
        segment_1 = max(delta_x_left, x1)
        segment_2 = min(delta_x_right, x2)
        if segment_2 - segment_1 >= 0:
            s += segment_2 - segment_1 + 1
    return s


x1_input, y1_input, x2_input, y2_input = map(int, input().split())
x3_input, y3_input, r_input = map(int, input().split())
print(lawn(x1_input, y1_input, x2_input, y2_input, x3_input, y3_input, r_input))
