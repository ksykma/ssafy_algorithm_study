import sys
sys.stdin = open('input.txt', 'r')

N = int(input())

result = 0
for i in str(N):
    result += int(i)

print(result)