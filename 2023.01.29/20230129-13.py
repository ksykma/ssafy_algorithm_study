import sys
sys.stdin = open('input.txt', 'r')

num = int(input())

result = 1
for i in range(num + 1):
    print(result, end = ' ')
    result *= 2
    