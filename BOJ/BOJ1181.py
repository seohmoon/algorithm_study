#BOJ 1181 단어정렬
n = int(input())
word_list = []
for i in range(n):
    i = input()
    if (i, len(i)) not in word_list:
        word_list += [(i, len(i))]
word_list.sort(key = lambda x:x[0])
word_list.sort(key = lambda x:x[1])
for word in word_list:
    if word[0] == word_list[-1][0]:
        print(word[0], end="")
    else :
        print(word[0])