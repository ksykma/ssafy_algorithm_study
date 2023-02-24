# SW Expert Academy 0208_String - 1961 숫자 배열 회전 

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    word = input()
    N = len(word)
    result = 1
    for i in range(N//2):
        if word[i] != word[N-1-i]:   # 양 끝 숫자가 다르면
            result = 0
            break
    print(f'#{t}', result)
