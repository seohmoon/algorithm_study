# BOJ 1157번 단어공부

#words = 'SwsoefF'
# 가장 많이 사용 된 알파펫을 대문자로 출력, 가장많이 사용된 알파벳이 여러개면 ?
# 일단 전부 대문자로 바꾸고 하나씩 비교하며 카운트해서 비교

words = input()
words = words.upper()
word2 = set(words)
words2 = list(word2)
tem = 0
result = ''

for word in words2:
    a = words.count(word)
    if a > tem:
        tem = a
        result = word
    elif a == tem:
        result = '?'
print(result)

''' 이건 시간 초과 나온 코드
count_check = []
count_num_list = []
tem = 0

for i in word:
    a = word.count(i)
    count_check.append((i,a))
    count_num_list.append(a)
    if a > tem:
        tem = a

if count_num_list.count(tem) == tem:
    for j in count_check:
        if j[1] == tem:
            print(j[0])
            break
else :
    print('?')
    '''