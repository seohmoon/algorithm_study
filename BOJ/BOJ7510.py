# BOJ7510 고급 수학
T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    lst.sort()
    print(f"Scenario #{tc}:")
    if lst[0]**2 + lst[1]**2 == lst[2]**2:
        print("yes")
    else:
        print("no")
    print()
