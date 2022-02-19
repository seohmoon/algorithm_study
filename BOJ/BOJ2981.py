# BOJ2981 검문
N = int(input())
nums = []
for i in range(N):
    i = int(input())
    nums.append(i)

nums.sort()
M = []
for i in range(2,nums[0]):
    tem = nums[0] % i
    tem2 = 1
    for j in nums:
        if j % i != tem:
            tem2 = -1
            break
    if tem2 > 0:
        M.append(i)

for j in M:
    print(j, end=" ")