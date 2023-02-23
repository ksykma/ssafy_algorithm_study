# SW Expert Academy 0222_Tree - 1231  

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    lst = [i for i in range(0, N+1)]
    result = [0] * (N+1)
    last = 1
    def inorder(v):
        global last
        if v > N:
            return
        inorder(v*2)
        result[v] = last
        last += 1
        inorder(v*2+1)
    inorder(1)
    print(f'#{t}', result[1], result[N//2])