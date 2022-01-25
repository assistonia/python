from collections import deque
import queue

def dfs(graph,N,visited):
    #방문 처리
    visited[N]=True
    print(N, end=' ')
    for i in range(len(graph[N])):
        k=graph[N][i]
        if visited[k] == False :
            dfs(graph,k,visited)

def bfs(graph,N,visited):
    #visited 초기화
    visited=[False] * 9
    
    queue=deque([N])
    visited[N] = True
    print(N,end=" ")
    while queue:
        l = queue.popleft()
        for i in range(len(graph[l])):
             k=graph[l][i]
             if visited[k] == False:
                 queue.append(k)
                 visited[k] = True
                 print(k,end=" ")
               
graph=[
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
#각 노드가 방문된 정보를 리스트로 표현 [1차원 리스트]
visited=[False] * 9

print("dfs:",end=" ")
dfs(graph, 1, visited)
print()
print("bfs:",end=" ")
bfs(graph, 1, visited)
