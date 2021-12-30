""" Описание задачи:
По последовательности чисел во входных данных определите ее вид:

CONSTANT – последовательность состоит из одинаковых значений
ASCENDING – последовательность является строго возрастающей
WEAKLY ASCENDING – последовательность является нестрого возрастающей
DESCENDING – последовательность является строго убывающей
WEAKLY DESCENDING – последовательность является нестрого убывающей
RANDOM – последовательность не принадлежит ни к одному из вышеупомянутых типов

Формат ввода:
По одному на строке поступают числа последовательности ai, |ai| ≤ 109.
Признаком окончания последовательности является число -2× 109. Оно в последовательность не входит.

Формат вывода:
В единственной строке выведите тип последовательности.
"""


def type_sequenсe(a_seq: int, b_seq: int):
    """
    Процедура type_sequenсe изменяет массив type_mass в зависимости от элементов a_seq, b_seq

    Example :
     :>>> type_sequenсe(-530,-530) -> [['CONSTANT',1],['ASCENDING',0],['DESCENDING',0]]

     :>>> type_sequenсe(-530,-560) -> [['CONSTANT',0],['ASCENDING',0],['DESCENDING',1]]

    :param a_seq: число для сравнения
    :param b_seq: число для сравнения
    :return: изменный масив type_sequenсe
    """
    if b_seq != -2000000000 and a_seq == b_seq:
        type_mass[0][1] += 1
    if b_seq != -2000000000 and a_seq < b_seq:
        type_mass[1][1] += 1
    if b_seq != -2000000000 and a_seq > b_seq:
        type_mass[2][1] += 1


type_mass = [['CONSTANT', 0], ['ASCENDING', 0], ['DESCENDING', 0]]
a_seq_input = int(input())
kol = 0
while a_seq_input != -2000000000:
    b_seq_input = int(input())
    kol += 1
    type_sequenсe(a_seq_input, b_seq_input)
    # print(kol, type_mass)
    a_seq_input = b_seq_input
if type_mass[0][1] == kol - 1:
    print('CONSTANT')
elif type_mass[1][1] == kol - 1:
    print('ASCENDING')
elif type_mass[0][1] + type_mass[1][1] == kol - 1:
    print('WEAKLY ASCENDING')
elif type_mass[2][1] == kol - 1:
    print('DESCENDING')
elif type_mass[0][1] + type_mass[2][1] == kol - 1:
    print('WEAKLY DESCENDING')
else:
    print('RANDOM')
