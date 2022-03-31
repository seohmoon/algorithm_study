# BOJ2693 N번째 큰 수
T = int(input())
for tc in range(T):
    arr = list(map(int, input().split()))
    arr.sort()
    print(arr[-3])