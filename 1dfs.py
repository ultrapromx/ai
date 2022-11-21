# Implement depth First Search algorithm

# Using a Python dictionary to act as an adjacency list
graph = {"A":["B","F"],
       "B":["A","F","E","C"],
       "C":["B","E","D"],
       "D":["C","E"],
       "E":["F","B","C","D"],
       "F":["A","B","E"]
}

visited = set() # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
print("Depth-First Search is:")
dfs(visited, graph, 'A')