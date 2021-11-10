""" Описание задачи:
Бригада скорой помощи выехала по вызову в один из отделенных районов.
К сожалению, когда диспетчер получил вызов, он успел записать только адрес дома и
номер квартиры K1, а затем связь прервалась.
1) Однако он вспомнил, что по этому же адресу дома некоторое время назад скорая помощь
выезжала в квартиру K2, которая расположена в подъезда P2 на этаже N2.
2) Известно, что в доме M этажей и количество квартир на каждой лестничной площадке одинаково.
Напишите программу, которая вычиляет номер подъезда P1 и номер этажа N1 квартиры K1.

Формат ввода: Во входном файле записаны пять положительных целых чисел K1, M, K2, P2, N2.
Все числа не превосходят 106.

Формат вывода: Выведите два числа P1 и N1. Если входные данные не позволяют
однозначно определить P1 или N1, вместо соответствующего числа напечатайте 0.
Если входные данные противоречивы, напечатайте два числа –1 (минус один).
"""


def ambulance(K1: int, M: int, K2: int, P2: int, N2: int) -> str:
    """
    Функция ambulance вычисляет номер подъезда P1 и номер этажа N1 квартиры K1.

    Example :
     :>>> ambulance(89, 20, 41, 1, 11) -> 2 3

     :>>> ambulance(11, 1, 1, 1, 1) -> 0 1

     :>>> ambulance(3, 2, 2, 2, 1) -> -1 -1

     :>>> 4) ambulance(5, 20, 2, 1, 1) -> 1 0

     :>>> 5) ambulance(11, 2, 4, 1, 2) -> 0 2

     :>>> 6) ambulance(1000, 1, 449, 449, 1) -> 1000 1

     :>>> 7) ambulance(40, 5, 60, 6, 5) -> 4 5

     :>>> 8) ambulance(130, 9, 175, 5, 8) -> 4 6

     :>>> 9) ambulance(753, 10, 1000, 1, 1) -> 1 1

     :>>> 10) ambulance(25, 3, 1, 1, 1) -> 0 0

     :>>> 13) ambulance(5, 1000, 5, 1, 2) -> 1 2

     :>>> 14) ambulance(41, 10, 41, 1, 10) -> -1 -1

     :>>> 23) ambulance(10, 3, 50, 1, 50) -> -1 -1

    :param K1: номер квартиры для вызова
    :param M: кол-во этажей в доме
    :param K2: номер квартиры известного адреса
    :param P2: номер подъезда известного адреса
    :param N2: номер этажа известного адреса
    :return: {P1 и N1}, номер подъезда и этажа квартиры для вызова
    """
    import math
    if N2 == 1 and P2 == 1:
        flat_on_floor = K2
    # elif K2%((N2-1)+(P2-1)*M) == 0:
    #    flat_on_floor = int(K2/(N2+(P2-1)*M))
    else:
        flat_on_floor = math.ceil(K2 / (N2 + (P2 - 1) * M))
    # print(flat_on_floor)
    if flat_on_floor * (N2 - 1) + flat_on_floor * M * (P2 - 1) >= K2 or N2 > M:
        return '-1 -1'
    else:
        P1_set = {0}
        N1_set = {0}
        P1 = 0
        N1 = 0
        # print(flat_on_floor*(N2-1)+flat_on_floor*M*(P2-1) < K2,flat_on_floor*N2+flat_on_floor*M*(P2-1) >= K2)
        while flat_on_floor * (N2 - 1) + flat_on_floor * M * (P2 - 1) < K2 \
                and flat_on_floor * N2 + flat_on_floor * M * (P2 - 1) >= K2 \
                and flat_on_floor <= max(K1, K2):
            if K1 % flat_on_floor > 0:
                floor = 1 + int(K1 / flat_on_floor)
            else:
                floor = int(K1 / flat_on_floor)
            if floor % M > 0:
                P1 = 1 + int(floor / M)
            else:
                P1 = int(floor / M)
            N1 = floor - (P1 - 1) * M
            N1_set = N1_set.union({N1})
            P1_set = P1_set.union({P1})
            # print(flat_on_floor,'---',P1,N1,'==',P1_set,N1_set )
            # print(flat_on_floor,'---',flat_on_floor*(N2-1)+flat_on_floor*M*(P2-1),
            # flat_on_floor*N2+flat_on_floor*M*(P2-1),
            # flat_on_floor*(N2-1)+flat_on_floor*M*(P2-1) <= K2,
            # flat_on_floor*N2+flat_on_floor*M*(P2-1) >= K2, flat_on_floor<=K1 )
            flat_on_floor += 1
        P1_set.discard(0)
        N1_set.discard(0)
        if len(P1_set) > 1:
            P1 = 0
        if len(N1_set) > 1:
            N1 = 0
        return str(P1)+' '+str(N1)


K1_input, M_input, K2_input, P2_input, N2_input = map(int, input().split())
print(ambulance(K1_input, M_input, K2_input, P2_input, N2_input))
