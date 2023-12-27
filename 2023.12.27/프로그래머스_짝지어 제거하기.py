def solution(s):
    answer = 1
    S = []
    for i in s:
        if len(S) == 0 or (S and i != S[-1]):
            S.append(i)
        elif S and i == S[-1]:
            S.pop()
    if S:
        answer = 0
    return answer