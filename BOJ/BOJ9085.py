#BOJ9085 더하기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    ans = 0
    for i in lst:
        ans += i
    print(ans)
