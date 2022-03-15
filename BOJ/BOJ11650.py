# BOJ11650
N = int(input())
tem = []
for i in range(N):
    i = tuple(map(int, input().split()))
    tem.append(i)

ans = sorted(tem, key=lambda x: (x[0],x[1]))

for x, y in ans:
    print(x,y)



