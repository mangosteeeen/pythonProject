from collections import deque

# BFS 메서드 정의
def dfs(x, y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
# 각 노드가 연결된 정보를 표현(2차원 리스트)
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

n,m = map(int,input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1

print(result)