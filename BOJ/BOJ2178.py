# BOJ 2178 미로탐색
def bfs(i, j, N, M):
    visited = [[0]*M  for _ in range(N)] # 방문표시
    queue = [] # 큐
    queue.append((i, j)) # 시작점 enQueue
    visited[i][j] = 1  # 시작점 방문 표시

    while queue: # 큐가 비어있지 않으면 계속 반복
        i, j = queue.pop(0) # deQueue 첫번째꺼 제거
        if i == N-1 and j == M-1:
            return visited[i][j]
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj # 인접하고 이동할수 있는 칸
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 1 and visited[ni][nj] == 0:
                queue.append((ni, nj)) # enQueue
                visited[ni][nj] = visited[i][j] + 1
    return(0)
             

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
ans = bfs(0, 0, N, M)
print(ans)