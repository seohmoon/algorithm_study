# BOJ10250 ACM호텔
T = int(input())

for tc in range(1, T+1):
    H, W, N = map(int, input().split())
    if H >= N:
        print(f"{N}01")
    else:
        a = N // H + 1
        b = N % H
        if b == 0:
            if a < 11:
                print(f"{H}0{a-1}")
            else:
                print(f"{H}{a-1}")
        else:
            if a < 10:
                print(f"{b}0{a}")
            else:
                print(f"{b}{a}")

