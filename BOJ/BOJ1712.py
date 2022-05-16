# BOJ1712 손익분기점
A, B, C = map(int, input().split())
if B >= C:
    print(-1)
else:
    ans = A // (C-B) + 1
    print(ans)
    

''' 시간초과
n = 1
while True:
    if B >= C:
        print(-1)
        break
    if A + n*B < n*C:
        print(n)
        break
    else:
        n += 1
        '''