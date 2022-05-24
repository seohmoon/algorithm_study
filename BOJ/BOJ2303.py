# BOJ2303 숫자게임
N = int(input())
ans = 0 # 가장 큰 사람의 번호(i)
maxvalue = 0 # 최댓값
for i in range(1, N+1):
    lst = list(map(int, input().split()))
    tem = 0
    for a in range(5):
        for b in range(4):
            for c in range(3):
                temsum = str(lst[a]+lst[b]+lst[c])
                tem=max(tem, int(temsum[-1]))
    if maxvalue <= tem:
        maxvalue = tem
        ans = i
print(ans)
print("2022-05-24")