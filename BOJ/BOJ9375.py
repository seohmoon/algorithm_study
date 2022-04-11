# BOJ9375 패션왕 신해빈
from ast import Not


def cnt(x):
    
    pass


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    clothes = []
    for i in range(N):
        clothes.append(list(map(str, input().split())))
    clothes.sort(key=lambda x:x[-1]) # 종류를 기준으로 정렬
    kind = [] # 종류가 몇갠지 찾기
    for j in clothes:
        if kind == [] or j[-1] not in kind:
            kind.append(j[-1])

