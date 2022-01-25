#BOJ 백준 10872번 팩토리얼_재귀

def my_factorial(n):
    if n <= 1: # 0! = 1, 1! = 1 이니까 따로 빼줌
        return 1
    else :
        return n * my_factorial(n - 1)

n= int(input())
print(my_factorial(n))