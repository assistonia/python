from collections import deque  #collections 모듈 사용

graphlist=[[],   #그래프 처리 
[2,3,8],
[1,7],
[1,4,5],
[3,5],
[3,4],
[7],
[2,6,8],
[1,7]
]

visiter=[False] * 9 #방문하지 않은 정보를 저장

def BFS(graph,visit):
    startnode=1    #시작번호는 1번
    queue = deque([startnode])  #deque 생성
    visit[startnode] =True #시작노드는 방문한것으로 

    while queue:
        a=queue.popleft()  
        print(a, end = ' ') #처음 노드를 출력
        for i in graph[a]:
            if not visit[i]: #방문하면 queue에 넣어지고 방문이된다
                queue.append(i)
                visit[i]=True #방문후 방문한 자리에 방문처리를 해준다

def DFS(graph,v,visited):
    visited[v]=True #시작지점을 방문처리
    print(v, end=' ')  #방문한 곳을 출력
    for b in graph[v]:
        if not visited[b]:
            DFS(graph, b,visited)  #재귀함수로 방문하지 않은곳이 없어질때까지 방문


BFS(graphlist,visiter) 
print()

visiter=[False] * 9 #visiter 다시 초기화 

DFS(graphlist,1,visiter)