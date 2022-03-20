# BOJ2164 카드2

def mix(x):
    newarr = []
    for i in range(len(x)):
        if i % 2 == 0:
            newarr.append(i)
    return(newarr)


N = int(input())
arr = []
for i in range(N+1):
    arr.append(i)

while True:
    if len(arr) == 2:
        print(arr[1])
        break
    else:
        mix(arr)
