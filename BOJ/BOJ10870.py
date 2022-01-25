#BOJ 백준 10870번 피보나치 수 5

def my_fibonacci(n):
    if n < 2: #피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다
        return n
    else :
        return my_fibonacci(n - 2) + my_fibonacci(n - 1)


n = int(input())
print(my_fibonacci(n))
