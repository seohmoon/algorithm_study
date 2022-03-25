# BOJ1436 영화감독 숌
N = int(input())

a = N // 16
b = N % 16

if a == 0:
    if b == 1:
        print(666)
    elif 1 < b < 6:
        print(f"{b-1}666")
else:
    if b < 7:
        