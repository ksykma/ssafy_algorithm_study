# SW Expert Academy 0220_Queue - 11650    

import sys
sys.stdin = open('input.txt', 'r')

def enqueue(item):
    global rear
    rear += 1
    Q[rear] = item
    
def dequeue():
    global front
    if isEmpty():
        return 0
    front += 1
    return Q[front]

def isEmpty():
    return rear == front

def isFull():
    return rear == len(Q) - 1
T = int(input())
for t in range(1, T + 1):
    N, M = list(map(int, input().split()))
    lst = list(map(int, input().split()))
    Q = [0] * (N + M)
    rear = -1
    front = 0
    for i in range(N):
        enqueue(lst[i])
    for i in range(M):
        if i >= N:
            i = i % N
            enqueue(lst[i])
            dequeue()
        else:
            enqueue(lst[i])
            dequeue()
    print(f'#{t}', Q[front])