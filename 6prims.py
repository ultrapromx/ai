# Prim's Algorithm in Python
# https://www.youtube.com/watch?v=Dtybc9IrKyY&t=750s


from heapq import *

def prims(graph, start, parent, distance, visited):
    distance[start]=0
    bag=[]  # for heap
    heappush(bag,[0,start])
    parent[start] = -1

    while bag:
        d,n = heappop(bag)
        if not visited[n]:
            visited[n] = 1
            for cd,cn in graph[n]:
                if distance[cn] > cd and not visited[cn]:
                    parent[cn] = n
                    distance[cn] = cd
                    heappush(bag, [cd,cn])

    print("Distance: ", distance)
    print("Parent", parent)


input = [[1,3,2],[1,2,1],
[2,3,1],[2,5,1],
[3,4,2],[5,4,5]]

n = 5
graph = {}
parent={}
distance = {}
visited = {}

for i in range(1, n+1):
    graph[i] = []
    distance[i] = 10**8+1 #infinity
    parent[i]=None
    visited[i] = 0

for u,v,d in input:
    graph[u].append([d,v])
    graph[v].append([d,u])

start=1

prims(graph, start, parent, distance, visited)


