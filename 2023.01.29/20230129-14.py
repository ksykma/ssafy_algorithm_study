import sys
sys.stdin = open('input.txt', 'r')

N = int(input())

for i in range(N + 1):
    print(N - i, end = ' ')