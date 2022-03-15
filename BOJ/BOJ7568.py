# BOJ7568 덩치

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
print(cntsort)




print (ranking)
            