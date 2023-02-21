words = input()
icp = {'+' : 1, '-' : 1, '*' : 2, '/' : 2, '(' : 3, ')' : 0}
isp = {'+' : 1, '-' : 1, '*' : 2, '/' : 2, '(' : 0, ')' : 0}
S = []
char = ''
for i in words:
    if i in icp:
        if i == ')':
            while S[-1] != '(':
                char += S.pop()
            S.pop()
        else:
            while S and isp[S[-1]] >= icp[i]:
                char += S.pop()
            S.append(i)
    else:
        char += i
while S:
    char += S.pop()
print(char)