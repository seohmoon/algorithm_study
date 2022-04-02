# BOJ4673 셀프 넘버
n = [1, 3, 5, 7, 9, 20, 31, 42, 53, 64, 75, 86]
#while n <= 10000:
#    print(*n)
print(*n, sep='\n')
m = 97
while m <= 10000:
    print(m)
    mstr = str(m)
    for i in mstr:
        m += int(i)