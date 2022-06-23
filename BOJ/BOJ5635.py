# BOJ5635 생일

N = int(input())

young_year = 1989 # 문제에서 주어진 범위가 1990까지
young_month = 0
young_date = 0

old_year = 2011 # 문제에서 주어진 범위가 2010까지
old_month = 13
old_date = 32

young = [""]
old = [""]

for i in range(N):
    a, b, c, d = map(str, input().split())
    b = int(b)
    c = int(c)
    d = int(d)

    if d > young_year:
        young_year = d
        young_month = c
        young_date = b
        young[0] = a
    elif d == young_year:
        if c > young_month:
            young_year = d
            young_month = c
            young_date = b
            young[0] = a
        elif c ==young_month:
            if b > young_date:
                young_year = d
                young_month = c
                young_date = b
                young[0] = a

    if d < old_year:
        old_year = d
        old_month = c
        old_date = b
        old[0] = a
    elif d == old_year:
        if c < old_month:
            old_year = d
            old_month = c
            old_date = b
            old[0] = a
        elif c == old_month:
            if d < old_date:
                old_year = d
                old_month = c
                old_date = b
                old[0] = a

print(*young)
print(*old)

