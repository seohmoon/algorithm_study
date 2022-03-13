# BOJ1920 수찾기   
# 시간초과    
N = int(input())
nrr = list(map(int, input().split()))
M = int(input())
mrr = list(map(int, input().split()))
nrr.sort()
a = 0
for i in range(M):
    check = 0
    if i == 0:
        for j in range(N):
            if mrr[i] == nrr[j]:
                a = j
                check = 1
                print(1)
                break
            #elif mrr[i] > nrr[j]:
             #       a = j-1
              #      print(0)
               #     break
    else:
        if mrr[i] == mrr[i-1]:
            check = 1
            print(1)
            break
        elif mrr[i] > mrr[i-1]:
            for j in range(a,N):
                if mrr[i] == nrr[j]:
                    a = j
                    check = 1
                    print(1)
                    break
                #elif mrr[i] > nrr[j]:
                 #   a = j-1
                  #  print(0)
                   # break
        elif mrr[i] < mrr[i-1]:
            for j in range(0,N):
                if mrr[i] == nrr[j]:
                    a = j
                    check = 1
                    print(1)
                    break
                #elif mrr[i] > nrr[j]:
                 #   a = j-1
                  #  print(0)
                   # break
        if check == 0:
            print(0)