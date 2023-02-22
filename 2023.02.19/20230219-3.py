import sys
sys.stdin = open('input.txt', 'r')

icp = {'+' : 1, '*' : 2}
for t in range(1, 11):
    N = int(input())
    words = input()
    S = []
    cal = ''
    for i in words:
        if i in icp:
            if len(S) == 0:
                S.append(i)
            else:
                while S and  icp[S[-1]] >= icp[i]:
                    cal += S.pop()
                S.append(i)
        else:
            cal += i
    while S:
        cal += S.pop()
    stack = []
    for i in cal:
        if i == '+':
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b)
        elif i == '*':
            b = stack.pop()
            a = stack.pop()
            stack.append(a * b)
        else:
            stack.append(int(i))
    print(f'#{t}', stack[0])
    