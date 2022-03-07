# SWEA12733 기지국
import sys
sys.stdin = open("in1.txt")

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(str, input())) for _ in range(n)]
    # 델타 탐색은 범위 주의
    di = [0, 1, 0, -1, 0, 2, 0, -2, 0, 3, 0, -3]
    dj = [1, 0, -1, 0, 2, 0, -2, 0, 3, 0, -3, 0]

    for i in range(n):
        for j in range(n):
            if arr[i][j] == "A":
                for a in range(4): # 상하좌우 1개씩
                    ni = i + di[a]
                    nj = j + dj[a]
                    if 0 <= ni < n and 0 <= nj < n:
                        arr[ni][nj] = "X"
            elif arr[i][j] == "B":
                for b in range(8): # 상하좌우 2개씩
                    ni = i + di[b]
                    nj = j + dj[b]
                    if 0 <= ni < n and 0 <= nj < n:
                        arr[ni][nj] = "X"
            elif arr[i][j] == "C": # 상하좌우 3개씩
                for c in range(12):
                    ni = i + di[c]
                    nj = j + dj[c]
                    if 0 <= ni < n and 0 <= nj < n:
                        arr[ni][nj] = "X"
    cnt = 0
    for x in range(n):
        for y in range(n):
            if arr[x][y] == "H":
                cnt += 1

    print(f"#{tc} {cnt}")