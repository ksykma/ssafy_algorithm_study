import sys
sys.stdin = open('input.txt', 'r')

N = int(input())

numbers = list(map(int, input().split()))
numbers.sort()
result = numbers[N // 2]

print(result)