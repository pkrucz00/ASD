class Node:
    def __init__(self):
        self.level = None
        self.low = None
        self.children = []


def __get_cuts(x, nodes, articulation_points, bridges):
    is_articulation_point = False

    for y in nodes[x].children:
        if nodes[y].level is None:
            nodes[y].low = nodes[y].level = nodes[x].level + 1
            __get_cuts(y, nodes, articulation_points, bridges)

            if not is_articulation_point and nodes[y].low >= nodes[x].level:
                is_articulation_point = True

            if nodes[y].low == nodes[y].level:
                bridges.append((x, y))

            nodes[x].low = min(nodes[x].low, nodes[y].low)

        elif nodes[x].level != nodes[y].level + 1:
            # istnieje krawędź powrotna (nie do rodzica)
            nodes[x].low = min(nodes[x].low, nodes[y].level)

    if is_articulation_point:
        articulation_points.append(x)


def get_cuts(nodes):
    articulation_points, bridges = [], []

    nodes[0].low = nodes[0].level = 0
    call_count = 0

    for y in nodes[0].children:
        if nodes[y].level is None:
            nodes[y].low = nodes[y].level = 1
            __get_cuts(y, nodes, articulation_points, bridges)

            if nodes[y].low == nodes[y].level:
                bridges.append((0, y))

            call_count += 1

    # korzeń jest punktem artykulacji wtedy i tylko wtedy, gdy ma więcej niż jedno dziecko w drzewie dfs
    if call_count > 1:
        articulation_points.append(0)

    return articulation_points, bridges


# zakładam, że graf jest spójny
n = 6
edges = [(1, 2), (0, 2), (0, 1), (2, 4), (3, 4), (0, 5)]

nodes = [Node() for _ in range(n)]
for x, y in edges:
    nodes[x].children.append(y)
    nodes[y].children.append(x)

articulation_points, bridges = get_cuts(nodes)

print(sorted(articulation_points))
for i in range(len(bridges)):
    bridges[i] = tuple(sorted(bridges[i]))
print(sorted(bridges))
