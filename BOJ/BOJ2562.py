# BOJ 2562번 최댓값
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
g = int(input())
h = int(input())
i = int(input())

all_list = [a,b,c,d,e,f,g,h,i]
tem = max(all_list)
print(tem)
print(all_list.index(tem)+1)

'''
input_list = []
num = 0
max_value = 0
for i in range(0, 9):
    i = input()
    input_list.append(i)
print(max(input_list))        
print(input_list.index(max(input_list))+1)
'''