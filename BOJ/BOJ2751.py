# BOJ 백준 2751번 수 정렬하기2
# n개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램
'''시간초과
n = int(input())
list_input = []
for i in range(n):
    list_input.append(int(input()))
for k in sorted(list_input):
    print(k)
'''

'''시간초과
n = int(input())
list_input = []
for i in range(n):
    i = int(input())
    list_input += [i]
index_num = 0
for j in range(n-1):
    if list_input[index_num] > list_input[index_num+1]:
        tem = list_input[index_num+1]
        list_input[index_num+1] = list_input[index_num]
        list_input[index_num] = tem
        index_num += 1
for k in list_input:
    print(k)
    '''