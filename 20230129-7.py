import sys
sys.stdin = open('input.txt', 'r')

P, K = map(int,input().split())

print(P - K + 1)
