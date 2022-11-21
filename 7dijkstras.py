# https://www.youtube.com/watch?v=oRwrtfSl81c


from heapq import *

def dijkstra(graph, start, visited, distance):
    distance[start]=0
    bag=[]  # for heap
    heappush(bag,[0,start])

    while bag:
        d,n = heappop(bag)
        visited[n]=1
        for cd,cn in graph[n]:
            if not visited[cn] and distance[n]+cd<distance[cn]:
                distance[cn] = distance[n] + cd
                heappush(bag, [distance[n]+cd,cn])

    print(distance)


input = [[1,3,2],[1,2,1],
[2,3,1],[2,5,1],
[3,4,2],[5,4,5]]

n = 5
graph = {}
distance = {}
visited = {}

for i in range(1, n+1):
    graph[i] = []
    distance[i] = 10**8+1 #infinity
    visited[i] = 0

for u,v,d in input:
    graph[u].append([d,v])
    graph[v].append([d,u])

start=1

dijkstra(graph,start,visited,distance)