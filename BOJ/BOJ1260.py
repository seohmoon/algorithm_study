# BOJ1260 DFS와 BFS 
def DFS(x):
    pass

def BFS(x):
    pass

N, M, V = map(int, input().split())
arr = [[] for _ in range(N+1)]

for i in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

visited = [False for _ in range(N+1)]