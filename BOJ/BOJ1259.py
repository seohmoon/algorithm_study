# BOJ2164 카드2

def mix(x):
    global arr
    newarr = [0]
    if len(x) % 2 == 0:
        newarr.append(arr[-1])
    for i in range(1, len(x)):
        if i % 2 == 0:
            newarr.append(arr[i])
    return(newarr)

N = int(input())
arr = []
for i in range(N+1):
    arr.append(i)

while len(arr) > 2:
    arr = mix(arr)

if len(arr) == 2:
        print(arr[1]) 