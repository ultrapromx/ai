# Implement Breadth First Search algorithm

graph = {
    "A":["B", "D"],
    "B":["A", "C"],
    "C":["B"],
    "D":["A", "E", "F"],
    "E":["D", "F", "G"],
    "F":["D", "E", "H"],
    "G":["E", "H"],
    "H":["G", "F"]
}

visited = [] # List for visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node): #function for BFS
  visited.append(node)
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
print("BFS Traversal")
bfs(visited, graph, 'A')    # function calling