# 2. Implement A star (A*) Algorithm for any game search problem.

AdjacencyList = {
    'S': [('B', 4), ('C', 3)],
    'B': [('F', 5), ('E', 12)],
    'C': [('E', 10), ('D', 7)],
    'D': [('E', 2)],
    'E': [('G', 5)],
    'F': [('G', 16)],
    'G': []

}

def get_neighbors(v):
    return AdjacencyList[v]

def h(n):
    H = {
        'S': 0,
        'B': 12,
        'C': 11,
        'D': 6,
        'E': 4,
        'F': 11,
        'G': 0
    }
    return H[n]

def a_star_algorithm(start, stop):
    open_list = {start}
    closed_list = set([])

    g = {}
    g[start] = 0

    parents = {}
    parents[start] = start

    while len(open_list) > 0:
        n = None
        for v in open_list:
            if n is None or g[v] + h(v) < g[n] + h(n):
                n = v
        if n is None:
            print('Path does not exist!')
            return None
        if n == stop:
            reconst_path = []

            while parents[n] != n:
                reconst_path.append(n)
                n = parents[n]

            reconst_path.append(start)
            reconst_path.reverse()

            return reconst_path

        for (m, weight) in get_neighbors(n):
            if m not in open_list and m not in closed_list:
                open_list.add(m)
                parents[m] = n
                g[m] = g[n] + weight
            else:
                if g[m] > g[n] + weight:
                    g[m] = g[n] + weight
                    parents[m] = n

                    if m in closed_list:
                        closed_list.remove(m)
                        open_list.add(m)

        open_list.remove(n)
        closed_list.add(n)


    print("Path Does not Exit")
    return None



a = a_star_algorithm('S', 'G')
print("Shortest Path: ", a)

sum = 0
for i in range(len(a) - 1):
    list = AdjacencyList[a[i]]
    for j in range(len(list)):
        if list[j][0] == a[i + 1]:
            sum += list[j][1]
print("Total Distance: ", sum)
