""" Описание задачи:
На уроке геометрии семиклассники Вася и Петя узнали, что такое параллелограмм.
На перемене после урока они стали играть в игру: Петя называл координаты четырех точек
в произвольном порядке, а Вася должен был ответить, являются ли эти точки вершинами
параллелограмма.
Вася, если честно, не очень понял тему про параллелограммы, и ему требуется
программа, умеющая правильно отвечать на Петины вопросы.
Напомним, что параллелограммом называется четырехугольник,
противоположные стороны которого равны и параллельны.

Формат ввода:
В первой строке входного файла записано целое число
N (1 ≤ N ≤ 10) - количество заданных Петей вопросов.
Каждая из N последующих строк содержит описание четырех точек - четыре пары
целых чисел X и Y (−100 ≤ X ≤ 100, −100 ≤ Y ≤ 100), обозначающих координаты точки.
Гарантируется, что четыре точки, о которых идет речь в одном вопросе, не лежат
на одной прямой.

Формат вывода:
Для каждого из вопросов выведите "YES", если четыре заданные точки
могут образовать параллелограмм, и "NO" в противном случае.
Ответ на каждый из запросов должен быть в отдельной строке без кавычек.
"""


def rho(t1_x: int, t1_y: int, t2_x: int, t2_y: int) -> float:
    """
    вспомогательная функция rho находит расстояние между двумя точками на плоскости
    :param t1_x: координата точки
    :param t1_y: координата точки
    :param t2_x: координата точки
    :param t2_y: координата точки
    :return: значение расстояния
    """
    return (abs((t1_x - t2_x) ** 2 + (t1_y - t2_y) ** 2)) ** 0.5


def parallelogram(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int, x4: int, y4: int) -> str:
    """
    Функция parallelogram определяет являются ли четыре точки вершинами параллелограмма.

    Example :
     :>>> parallelogram(1, 1, 4, 2, 3, 0, 2, 3) -> YES

     :>>> parallelogram(1, 1, 5, 2, 2, 3, 3, 0) -> NO

     :>>> parallelogram(0, 0, 5, 1, 6, 3, 1, 2) -> YES

    :param x1: координата вершины
    :param y1: координата вершины
    :param x2: координата вершины
    :param y2: координата вершины
    :param x3: координата вершины
    :param y3: координата вершины
    :param x4: координата вершины
    :param y4: координата вершины
    :return: {YES, NO} являются ли вершинами параллелограмма
    """
    if (abs(rho(x1, y1, x2, y2) - rho(x3, y3, x4, y4)) < 0.001 and abs(
            (x1 - x2) * (y3 - y4) - (x3 - x4) * (y1 - y2)) < 0.001) or (
            abs(rho(x1, y1, x3, y3) - rho(x2, y2, x4, y4)) < 0.001 and abs(
            (x1 - x3) * (y2 - y4) - (x2 - x4) * (y1 - y3)) < 0.001):
        return 'YES'
    else:
        return 'NO'


n_input = int(input())
for _ in range(n_input):
    x1_input, y1_input, x2_input, y2_input, x3_input, y3_input, x4_input, y4_input = map(int, input().split())
    print(parallelogram(x1_input, y1_input, x2_input, y2_input, x3_input, y3_input, x4_input, y4_input))
