def solution(keymap, targets):
    answer = []
    for i in range(len(targets)):
        cnt = 0
        for j in range(len(targets[i])):
            min_val = 100
            for k in range(len(keymap)):
                if targets[i][j] in keymap[k]:
                    for q in range(len(keymap[k])):
                        if targets[i][j] == keymap[k][q]:
                            if min_val > q+1:
                                min_val = q+1
                                break
            if min_val == 100:
                answer.append(-1)
                cnt = 0
                break
            else:
                cnt += min_val
        if cnt != 0:
            answer.append(cnt)
    return answer

print(solution(["AGB", "BSSS"], ["AGZ", "BSSS"]))