#BOJ1152 단어의 개수
problem = input()
problem = problem.strip()
if len(problem) == 0:
    print(0)
else:    
    print(problem.count(' ') + 1)