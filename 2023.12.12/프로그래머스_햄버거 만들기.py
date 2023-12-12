def solution(ingredient):
    lst = []
    answer = 0
    for i in ingredient:
        lst.append(i)
        if lst[-4:] == [1, 2, 3, 1]:
            answer += 1
            for _ in range(4):
                lst.pop()
    return answer

print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))
print(solution([1, 3, 2, 1, 2, 1, 3, 1, 2]))