# BOJ2576 홀수
ans_sum = 0
ans_min = 100
for i in range(7):
    i = int(input())
    if i % 2 != 0:
        ans_sum += i
        ans_min = min(ans_min, i)
if ans_sum == 0:
    print(-1)
else:
    print(ans_sum)
    print(ans_min)