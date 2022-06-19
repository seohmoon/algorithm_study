# BOJ25024 시간과 날짜
def check_time(x, y):
    if x > 23:
        return("No")
    else:
        if y > 59:
            return("No")
        else:
            return("Yes")

def check_date(x, y):
    case1 = [1, 3, 5, 7, 8, 10, 12]
    if x > 12 or x == 0:
        return("No")
    else:
        if x in case1:
            if y > 31 or y == 0:
                return("No")
        elif x == 2:
            if y > 29 or y == 0:
                return("No")
        else:
            if y > 30 or y == 0:
                return("No")
        return("Yes") 

T = int(input())
for i in range(T):
    x, y = map(int, input().split())
    print(check_time(x, y), end=" ")
    print(check_date(x, y))
