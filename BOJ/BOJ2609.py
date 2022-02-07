# BOJ 2609번 최대공약수와 최소공배수

# 약수찾기
def soo(x):
    tem = 1
    tem_list = []
    while tem <= x:
        if x % tem == 0:
            tem_list.append(tem)
        tem += 1
    return(tem_list)

a, b = map(int, input().split())

a_list = soo(a)
b_list = soo(b)
# 최대공약수
max_num = 0
for i in a_list:
    for j in b_list:
        if i == j:
            max_num = i
print(max_num)
print(max_num*(a//max_num)*(b//max_num)) # 최소공배수