L = int(input())
if L <= 4:
    print(1)
else:
    a = L // 5
    if L % 5 == 0:
        print(a)
    else:
        print(a+1)