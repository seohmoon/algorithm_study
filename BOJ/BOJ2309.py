#BOJ2309 일곱난쟁이 - 투포인터
def low_high(x): # 오름차순으로 정렬
    for i in range(len(x)-1):
        for j in range(len(x)-1):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]
    return (x)

heights = []
for i in range(9):
    i = int(input())
    heights.append(i)

heights = low_high(heights) # 오름차순으로 정렬
total = 0
while True:
    a = 0
    for i in range(7):
        total += heights[i + a]
    if total == 100:
        for j in range(7):
            print(heights[j])
            break
    if total < 100:
        a + 1
        

