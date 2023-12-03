def solution(coin, cards):
    answer = 0
    mycard = cards[0:len(cards)//3]
    cnt = coin
    check = 0
    go = 0
    for i in range(len(cards)//3, len(cards)//2):
        for j in range(len(mycard)):
            if cnt > 0:
                if mycard[j] + cards[i] == len(cards) + 1:
                    mycard.append(cards[i])
                    cnt -= 1
                if mycard[j] + cards[i+1] == len(cards) + 1:
                    mycard.append(cards[i+1])
                    cnt -= 1
        for j in range(len(mycard)):
            for k in range(j+1, len(mycard)):
                if mycard[j] + mycard[k] == len(cards) + 1:
                    answer += 1
                    go = 1
                    mycard = [q for q in mycard if q not in {mycard[j], mycard[k]}]
                    break
            if go == 1:
                go = 0
                break
            else:
                check = 1
        if check == 1:
            answer += 1
            break
    return answer

print(solution(4, [3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4]))
print(solution(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]))