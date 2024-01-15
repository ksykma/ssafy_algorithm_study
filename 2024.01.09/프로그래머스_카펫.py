def solution(brown, yellow):
    answer = []
    sol = brown - 4 # 테두리 빼주고
    n1 = 1 # 세로길이 - 2를 1부터 시작
    while True:
        n2 = (sol - 2*n1) // 2 # 가로길이 - 2의 길이
        if n1*n2 != yellow: # (가로 - 2) * (세로 - 2)값이 yellow와 같아야 함
            n1 += 1
        else:
            answer = [max(n1, n2)+2, min(n1, n2)+2]
            break
    return answer

print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))