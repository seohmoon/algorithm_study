# BOJ 11866 요세푸스 문제 0
N, K = int(input())
queue = []
for i in range(1, N+1):
    queue.append(i)

while True:
    newqueue = []
    for j in range(1, len(queue)):
        if j > K:
            newqueue.append(j)
            


