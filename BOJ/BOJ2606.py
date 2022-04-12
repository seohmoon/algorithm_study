# BOJ2606 바이러스
# 연결 요소의 크기
def dfs(cur):
    cnt = 1 # 자기 자신
    visited[cur] = True # 방문처리 해주기
    
    for nxt in v[cur]:
        if visited[nxt]:
            continue 

        cnt += dfs(nxt)
    
    return(cnt)

N = int(input())
M = int(input())
v = [[] for _ in range(N+1)] 

for i in range(M):
    a, b = map(int, input().split())

    v[a].append(b) # 리스트 안에 리스트 형식으로 연결요소 담아줌
    v[b].append(a)

visited = [False for _ in range(N+1)] # 방문표시 할 노드 만들기

print(dfs(1) - 1)

