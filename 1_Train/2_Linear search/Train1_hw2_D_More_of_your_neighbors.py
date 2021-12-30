""" Описание задачи:
Дан список чисел. Определите, сколько в этом списке элементов, которые больше
двух своих соседей и выведите количество таких элементов.

Формат ввода:
Вводится список чисел. Все числа списка находятся на одной строке.

Формат вывода:
Выведите ответ на задачу.
"""


def more_neighbors(list_number: list) -> int:
    """
    Функция more_neighbors выводит кол-во элементов, которые больше двух своих соседей.

    Example :
     :>>> more_neighbors([1,2,3,4,5]) -> 0

     :>>> more_neighbors([5,4,3,2,1]) -> 0

     :>>> more_neighbors([1,5,1,5,1]) -> 2

    :param list_number: массив для анализа
    :return: кол-во элементов
    """
    rho = [True if list_number[i] > list_number[i - 1] and list_number[i] > list_number[i + 1] else False
           for i in range(1, len(list_number) - 1)]
    return sum(rho)

list_number_input = list(map(int, input().split()))
print(more_neighbors(list_number_input))
