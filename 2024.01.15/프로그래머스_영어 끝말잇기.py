def solution(n, words):
    answer = 1
    end = 0
    check = { i : 0 for i in set(words)}
    check[words[0]] = 1
    if len(words[0]) == 1:
        return [1, 1]
    for i in range(1, len(words)):
        answer += 1
        if words[i-1][-1] != words[i][0]:
            end = 1
            break
        elif len(words[i]) == 1:
            end = 1
            break
        elif check[words[i]] == 1:
            end = 1
            break
        else:
            check[words[i]] = 1
    if answer == len(words) and end == 0:
        return [0, 0]
    return [answer % n if answer % n != 0 else n, answer // n if answer % n == 0 else answer // n + 1]

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))