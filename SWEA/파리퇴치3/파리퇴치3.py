# SWEA12712 파리 퇴치3
import sys
sys.stdin = open("in1.txt")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_value = 0

    for i in range(N):
        for j in range(N):
            tem1 = 0
            tem2 = 0
            for x in range(1, M): # 대각선
                di_x = [-x, -x, x, x]
                dj_x = [-x, x, -x, x]
                for a in range(4):
                    ni = i + di_x[a]
                    nj = j + dj_x[a]
                    if 0 <= ni < N and 0 <= nj < N:
                        tem1 += arr[ni][nj]
            tem1 += arr[i][j] # 기준점 값 더하기
            for y in range(1, M): # 상하좌우
                di_y = [0, y, 0, -y]
                dj_y = [y, 0, -y, 0]
                for b in range(4):
                    ni = i + di_y[b]
                    nj = j + dj_y[b]
                    if 0 <= ni < N and 0 <= nj < N:
                        tem2 += arr[ni][nj]
            tem2 += arr[i][j]
            if tem1 > max_value:
                max_value = tem1
            if tem2 > max_value:
                max_value = tem2

    print(f"#{tc} {max_value}")