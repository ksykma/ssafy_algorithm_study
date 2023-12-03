def solution(numbers, hand):
    answer = ''
    l = [1, 4, 7]
    r = [3, 6, 9]
    d = [2, 5, 8, 0]
    last_l = -1
    last_r = -1
    idx_l = 3
    idx_r = 3
    for number in numbers:
        if number in l:
            answer += "L"
            last_l = number
        elif number in r:
            answer += "R"
            last_r = number
        else:
            if last_l != -1:
                if last_l in l:
                    idx_l = l.index(last_l)
                else:
                    idx_l = d.index(last_l)
            if last_r != -1:
                if last_r in r:
                    idx_r = r.index(last_r)
                else:
                    idx_r = d.index(last_r)
            if (last_l in d and last_r in d) or (last_l not in d and last_r not in d):
                if abs(idx_l - d.index(number)) < abs(idx_r - d.index(number)):
                    answer += "L"
                    last_l = number
                elif abs(idx_l - d.index(number)) > abs(idx_r - d.index(number)):
                    answer += "R"
                    last_r = number
                else:
                    if hand == "left":
                        answer += "L"
                        last_l = number
                    else:
                        answer += "R"
                        last_r = number
            elif last_l in d:
                if abs(idx_l - d.index(number))-1 < abs(idx_r - d.index(number)):
                    answer += "L"
                    last_l = number
                elif abs(idx_l - d.index(number))-1 > abs(idx_r - d.index(number)):
                    answer += "R"
                    last_r = number
                else:
                    if hand == "left":
                        answer += "L"
                        last_l = number
                    else:
                        answer += "R"
                        last_r = number
            elif last_r in d:
                if abs(idx_l - d.index(number)) < abs(idx_r - d.index(number))-1:
                    answer += "L"
                    last_l = number
                elif abs(idx_l - d.index(number)) > abs(idx_r - d.index(number))-1:
                    answer += "R"
                    last_r = number
                else:
                    if hand == "left":
                        answer += "L"
                        last_l = number
                    else:
                        answer += "R"
                        last_r = number
    return answer