# SWEA스도쿠 검증
import sys
sys.stdin = open("input (4).txt")

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    check = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = 1

    for i in range(9): #행 기준, 열 기준
        if result == 0:
            break
        tem1 = []
        tem2 = []
        for j in range(9):
            tem1 += [arr[i][j]]
            tem2 += [arr[j][i]]
        tem1 = sorted(tem1)
        tem2 = sorted(tem2)
        if tem1 != check or tem2 != check:
            result = 0
            print(f"#{tc} 0")
            break

    if result != 0:
        for a in range(1, 8, 3):
            for b in range(1, 8, 3):
                tem3 = []
                if result == 0:
                    break
                for c in range(3):
                    for d in range(3):
                        tem3 += [arr[a - 1 + c][b - 1 + d]]
                tem3 = sorted(tem3)
                if tem3 != check:
                    result = 0
                    print(f"#{tc} 0")
                    break

    if result == 1:
        print(f"#{tc} 1")