# BOJ11931 수 정렬하기 4
N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))
lst.sort(reverse=True)
print(*lst, sep="\n")