# SW Expert Academy 0220_Queue - 11649 

import sys
sys.stdin = open('input.txt', 'r')
# def enQueue(item):
#     global rear
#     if isFull():
#         print('꽉참')
#     else:
#         rear += 1
#         Q[rear] = item

# def deQueue():
#     global front
#     if isEmpty():
#         return
#     else:
#         front += 1
#         return Q[front]
    
# def isEmpty():
#     return front == rear

# def isFull():
#     return rear == len(Q) -1

# def Qpeek():
#     if isEmpty():
#         return
#     else:
#         return Q[front + 1]

# T = int(input())
# for t in range(1, T + 1):
#     N, M = list(map(int, input().split()))
#     Q = list(map(int, input().split())) + [0] * M
#     front = -1
#     rear = N-1

#     for i in range(M):
#         a = deQueue()
#         enQueue(a)
#     print(f'#{t}', Q[front+1])

def enQueue(item):
    global rear
    if front == (rear + 1) % (N + M):
        return
    rear = (rear + 1) % (M + N)
    Q[rear] = item

def deQueue():
    global front
    front = (front + 1) % (N + M)
    return Q[front]


T = int(input())
for t in range(1, T + 1):
    N, M = list(map(int, input().split()))
    Q = list(map(int, input().split())) + [0] * M
    front = 0
    rear = N-1

    for i in range(M):
        a = deQueue()
        enQueue(a)
    print(f'#{t}', Q[front+1])