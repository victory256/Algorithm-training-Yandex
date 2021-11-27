""" Описание задачи:
Дан неориентированный невзвешенный граф. В графе возможны петли и кратные рёбра.
Постройте такой новый граф без петель и кратных рёбер, что для любых двух вершин
в нём расстояние равно расстоянию в исходном графе. Если вершины не связны,
расстояние между ними бесконечность.

Формат ввода:
На первой строке число вершин 1<=n и число рёбер m<=100 000.
Следующие m строк содержат пары чисел от 1 до n – рёбра графа.

Формат вывода
Новый граф в таком же формате. Рёбра можно выводить в произвольном формате.
"""


def multigraph(mass_edge: list) -> list:
    """
    Функция multigraph проверяет удаляет петли или кратные ребра

    Example :
     :>>> multygraph([(1, 1) , (1, 2), (3, 4)]) -> [(1, 2), (3, 4)]

     :>>> multygraph([(2, 1) , (1, 2), (3, 4)]) -> [(1, 2), (3, 4)]

    :param mass_edge: граф до анализа ребра
    :return: граф после добавления ребра
    """
    less_edge = []
    for i in range(len(mass_edge)):
        if mass_edge[i][0] != mass_edge[i][1]:
            less_edge.append((min(mass_edge[i][0], mass_edge[i][1]), max(mass_edge[i][0], mass_edge[i][1])))
    return list(set(less_edge))


n_input, m_input = map(int, input().split())
edge = []
# считываем весь граф
for _ in range(m_input):
    vertex_1_inp, vertex_2_inp = map(int, input().split())
    edge.append((vertex_1_inp, vertex_2_inp))
# удаляем петли или кратные ребра
edge = multigraph(edge)
# выводим получившийся граф
print(n_input, len(edge))
for i in range(len(edge)):
    print(edge[i][0], edge[i][1])
