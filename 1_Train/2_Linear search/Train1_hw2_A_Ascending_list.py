""" Описание задачи:
Дан список. Определите, является ли он монотонно возрастающим(то есть верно ли,
что каждый элемент этого списка больше предыдущего).
Выведите YES, если массив монотонно возрастает и NO в противном случае.
"""


def ascending_list(list_number: list) -> str:
    """
    Функция  ascending_list проверяет является ли список монотонно возрастающим

    Example :
     :>>> ascending_list(1,7,9) -> YES

     :>>> ascending_list(1,9,7) -> NO

     :>>> ascending_list(2,2,2) -> NO

    :param list_number: список чисел для анализа
    :return: {YES,NO}, результат проверки
    """
    if len(list_number) == 1:
        return 'YES'
    for i in range(len(list_number) - 1):
        if list_number[i] >= list_number[i + 1]:
            return 'NO'
    if i == len(list_number) - 2:
        return 'YES'


list_number_input = list(map(int, input().split()))
print(ascending_list(list_number_input))
