# BOJ 2577번 숫자의 개수
a = int(input())
b = int(input())
c = int(input())
abc = a * b * c
abc_list = []
tem = 0
for i in str(abc):
    abc_list.append(i)
for j in range(0,10):
    print(abc_list.count(str(tem)))
    tem += 1