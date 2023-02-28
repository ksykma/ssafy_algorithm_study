import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    num = list(input())
    start = ['0'] * len(num)
    result = 0
    while start != num:
        for i in range(len(num)):
            if start[i] != num[i]:
                for j in range(i, len(num)):
                    start[j] = num[i]
                result += 1
    print(f'#{t}', result)