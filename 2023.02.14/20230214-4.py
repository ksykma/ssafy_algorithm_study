# SW Expert Academy 0214_Stack1 - 12397 

S = []
import sys
sys.stdin = open('input.txt', 'r')
                
# T = int(input())
# for t in range(1, T + 1):
#     N = int(input())
#     def paper(n):
#         if n == 10: return 1
#         if n == 20: return 3

#         return paper(n-10) + paper(n-20) * 2
#     print(paper(N))

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    memo = [0] * 501
    def paper(n):
        if n == 10: return 1
        if n == 20: return 3
        if memo[n] != 0: return memo[n]

        memo[n] = paper(n-10) + paper(n-20)*2
        return memo[n]
    print(paper(N))