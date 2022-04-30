# BOJ1620 나는야 포켓몬 마스터 이다솜
import sys
N, M = map(int, input().split())
pokemon = {}
pokemon2 = {}
for i in range(1, N+1):
    pokemonnumber = str(i)
    pokemonname = sys.stdin.readline().strip()
    pokemon[pokemonname] = pokemonnumber
    pokemon2[pokemonnumber] = pokemonname

for j in range(M):
    j = sys.stdin.readline().strip()
   
    if 49 <= ord(j[0]) <= 57: # 숫자일 때
        print(pokemon2[j])
    else:
        print(pokemon[j])