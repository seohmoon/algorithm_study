# BOJ1260 DFS와 BFS 
def dfs(x):
    cnt = 1
    visited[x] = True

    for nxt in arr[x]:
        if visited[nxt]:
            continue
        cnt += dfs(nxt)
    return(cnt)

def BFS(x):
    pass

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]

for i in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

visited = [False for _ in range(N+1)]

print(dfs(1))
