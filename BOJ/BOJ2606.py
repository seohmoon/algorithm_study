# BOJ2606 바이러스
def dfs(cur):
    global cnt
    visited[cur] = True # 방문처리 해주기
    cnt += 1
    
    for nxt in v[cur]:
        if visited[nxt]:
            continue

        dfs(nxt)

N = int(input())
M = int(input())
v = [[] for _ in range(N+1)] # 앞에 패딩

for i in range(M):
    a, b = map(int, input().split())

    v[a].append(b) # 리스트 안에 리스트 형식으로 연결요소 담아줌
    v[b].append(a)

visited = [False for _ in range(N+1)] # 방문표시 할 노드 만들기

cnt = 0
for i in range(2, N+1):
    if visited[i]:
        cnt += 1

print(cnt)

