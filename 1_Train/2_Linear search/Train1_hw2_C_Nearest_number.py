""" Описание задачи:
Напишите программу, которая находит в массиве элемент, самый близкий по величине
к  данному числу.

Формат ввода:
В первой строке задается одно натуральное число N, не превосходящее 1000 – размер массива.
Во второй строке содержатся N чисел – элементы массива (целые числа, не превосходящие
по модулю 1000). В третьей строке вводится одно целое число x, не превосходящее по модулю 1000.

Формат вывода:
Вывести значение элемента массива, ближайшее к x. Если таких чисел несколько,
выведите любое из них.
"""


def nearest_number(find_number: int, list_number: list) -> int:
    """
    Функция nearest_number находит в массиве list_number элемент, самый близкий
    по величине к  данному числу find_number.

    Example :
     :>>> nearest_number(6, [1,2,3,4,5]) -> 5

     :>>> nearest_number(3, [5,4,3,2,1]) -> 3

    :param find_number: число для поиска в массиве
    :param list_number: массив для анализа
    :return: ближайший элемент
    """
    rho = [abs(i - find_number) for i in list_number]
    return list_number[rho.index(min(rho))]


n_input = int(input())
list_number_input = list(map(int, input().split()))
find_number_input = int(input())
print(nearest_number(find_number_input, list_number_input))
