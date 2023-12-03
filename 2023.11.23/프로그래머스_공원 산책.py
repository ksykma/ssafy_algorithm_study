def solution(park, routes):
    r = 0
    c = 0
    change = 0
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == "S":
                r = i
                c = j
                change = 1
                break
        if change == 1:
            break
    for i in range(len(routes)):
        direct, cnt = routes[i].split()
        count = int(cnt)
        if direct == "N":
            while count != 0:
                if r - 1 < 0:
                    r += int(cnt) - count
                    break
                elif park[r - 1][c] == 'X':
                    r += int(cnt) - count
                    break
                else:
                    r -= 1
                    count -= 1  
        elif direct == "S":
            while count != 0:
                if r + 1 > len(park) - 1:
                    r -= int(cnt) - count
                    break
                elif park[r + 1][c] == 'X':
                    r -= int(cnt) - count
                    break
                else:
                    r += 1
                    count -= 1  
        elif direct == "W":
            while count != 0:
                if c - 1 < 0:
                    c += int(cnt) - count
                    break
                elif park[r][c - 1] == 'X':
                    c += int(cnt) - count
                    break
                else:
                    c -= 1
                    count -= 1  
        elif direct == "E":
            while count != 0:
                if c + 1 > len(park[0]) - 1:
                    c -= int(cnt) - count
                    break
                elif park[r][c + 1] == 'X':
                    c -= int(cnt) - count
                    break
                else:
                    c += 1
                    count -= 1 
    answer = [r, c]
    return answer

print(solution(["OOO", "OSO", "OOO", "OOO"], ["N 2", "S 2"]))