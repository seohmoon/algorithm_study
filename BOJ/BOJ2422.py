# BOJ2422 한윤정이 이탈리아에 가서 아이스크림을 사먹는데
N, M = map(int, input().split())
total = (N*(N-1)*(N-2)) // (3*2*1)
lst = []
for i in range(M):
    a, b = map(int, input().split())
    for j in range(1, N+1):
        if j != a and j != b:
            tem = [a, b, j]
            tem.sort()
            if tem not in lst:
                lst.append(tem)
print(total - len(lst))
    
