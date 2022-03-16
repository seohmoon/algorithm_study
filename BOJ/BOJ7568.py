# BOJ7568 덩치

from tabnanny import check


N = int(input())
peoples = []
for people in range(N):
    peoples.append(tuple(map(int, input().split())))
cnt = [0]*N 
for i in range(N):
    tem = 0
    for j in range(N):
        if i != j:
            if peoples[i][0] > peoples[j][0] and peoples[i][1] > peoples[j][1]:
                tem += 1
    cnt[i] = tem
ranking = [0]*N
cntsort = sorted(cnt, reverse=True)
#print(cntsort)
check = 1
for a in range(N):
    
    if a == 0:
        ranking[a] = 1
    else:
        if cntsort[a-1] == cntsort[a]:
            ranking[a] = ranking[a-1]
            check += 1
        else:
            ranking[a] = ranking[a-1] + check
            check = 1
#print(ranking)
for b in cnt:
    for c in range(N):
        if b == cntsort[c]:
            print(ranking[c], end=" ")
            break            