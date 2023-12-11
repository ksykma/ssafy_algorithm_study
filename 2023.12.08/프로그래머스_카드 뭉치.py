def solution(cards1, cards2, goal):
    check = 0
    for i in range(len(goal)):
        if len(cards1) > 0 and goal[i] == cards1[0]:
            cards1.pop(0)
        else:
            check += 1
        if len(cards2) > 0 and goal[i] == cards2[0]:
            cards2.pop(0)
        else:
            check += 1
        if check == 2:
            check = 0
            return 'No'
        else:
            check = 0
    return 'Yes'
    
print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]))
print(solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"]))
