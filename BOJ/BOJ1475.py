# BOJ 1475 방번호
N = input()
cnt = 1
plastic = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for i in N:
    i = int(i)
    if i != 6 and i != 9:
        if plastic[i] != 0:
            plastic[i] -= 1
        else:
            cnt += 1
            for j in range(10):
                plastic[j] += 1
            plastic[i] = 0
    else: # 6이나 9일때
        if plastic[6] != 0:
            plastic[6] -= 1
        elif plastic[9] != 0:
            plastic[9] -= 1
        elif plastic[6] == 0 and plastic[9] == 0:
            cnt += 1
            for k in range(10):
                plastic[k] += 1
            plastic[6] = 0
print(cnt)