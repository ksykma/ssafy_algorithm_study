def solution(s):
    answer = ''
    check = 0
    for i in s:
        if i != ' ':
            if check == 0:
                answer += i.upper()
                check = 1
            else:
                answer += i.lower()
        else:
            check = 0
            answer += ' '
    return answer

print(solution("a  b  c"))
print("3people UnFollowed Me" == "3people Unfollowed Me")