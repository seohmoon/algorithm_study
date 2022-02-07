# BOJ 11720번 숫자의 합
n = int(input())
numbers = input()
sum_number = 0
for number in numbers:
    sum_number += int(number)
print(sum_number)