# SW Expert Academy 0303_문제풀이 - 1220

import sys
sys.stdin = open('input.txt', 'r')

for t in range(1, 11):
    N = int(input())
    arr = [input().split() for _ in range(N)]
    
    # 1은 N극, 2는 S극, 위에 N극, 아래에 S극
    result = 0
    for i in range(N):
        word = ''
        for j in range(N):
            if arr[j][i] != '0':
                word += arr[j][i]
        result += word.count('12')
    print(f'#{t}', result)