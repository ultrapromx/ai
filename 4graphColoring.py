# graph coloring problem.

def graphColouring(graph):
    colouring = {}
    for node in graph:
        neighbours = graph[node]
        colours = []
        for neighbour in neighbours:
            if neighbour in colouring:
                colours.append(colouring[neighbour])
        colour = 1
        while colour in colours:
            colour += 1
        colouring[node] = colour
    return colouring


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E', 'F'],
    'E': ['C', 'D', 'F'],
    'F': ['D', 'E']
}

colouring = graphColouring(graph)
print(colouring)