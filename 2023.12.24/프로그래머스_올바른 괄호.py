def solution(s):
    S = []
    result = True
    for i in s:
        if i == '(':
            S.append(i)
        elif S and i == ')' and S[-1] == '(':
            S.pop()
        elif i == ')':
            result = False
            break
             
    if S:
        result = False
        
    return result