def solution(priorities, location):
    answer = 0
    max_location = priorities.index(max(priorities)) # 맨 처음 중요도가 가장 높은 값의 위치
    while True:
        max_val = max(priorities) # 현재 가장 큰 값(제일 중요한 프로세스)
        if (priorities[max_location] == max_val):
            priorities[max_location] = 0 # 가장 중요도가 높은 값을 0으로 리셋
            answer += 1
            if (max_location == location):
                break
        max_location += 1 # 위치를 뒤로 한칸 씩 옮겨주기
        if (max_location >= len(priorities)): # max_location값이 길이를 넘어서면
            max_location = 0 # 0으로 리셋
    return answer
