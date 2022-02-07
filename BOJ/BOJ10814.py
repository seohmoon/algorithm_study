# BOJ 10814번 나이순 정렬

n = int(input())
members =[]
for i in range(n):
    mem_age, mem_name = map(str,input().split( ))
    members += [(int(mem_age), mem_name)]
members.sort(key=lambda x:x[0])
for member in members:
    print(member[0], member[1])

#tuple_list.sort(key=lambda x:-x[1]) #튜플리스트 평점 내림차순으로 정렬
 #   top5list = tuple_list[:5] #평점 5위까지 자름