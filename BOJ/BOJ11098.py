# BOJ11098 첼시를 도와줘!
T = int(input())
for tc in range(1, T+1):
    p = int(input())
    money = 0
    ans = [""]
    for i in range(p):
        a, b = map(str, input().split())
        a = int(a)
        if a > money:
            money = a
            ans[0] = b
    print(*ans)
