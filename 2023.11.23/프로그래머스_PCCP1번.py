def solution(bandage, health, attacks):
    hp = health
    t, r, p = bandage
    cnt = 0 # 연속성공
    start = attacks[0][0]

    for i in range(len(attacks)):
        while start != attacks[i][0] + 1:
            if start != attacks[i][0]:
                if hp < health:
                    hp += r
                    cnt += 1
                    if cnt == t:
                        hp += p
                        cnt = 0
                if hp > health:
                    health = hp
            else:
                hp -= attacks[i][1]
                cnt = 0
                if hp <= 0:
                    hp = -1
                    break
            start += 1

    return hp






# def solution(bandage, health, attacks):
#     start = attacks[0][0] # 시작 체력
#     hp = health # 체력
#     cnt = 0
#     time = bandage[0] # 시전 시간
#     recovery = bandage[1] # 초당 회복량
#     recovery_plus = bandage[2] # 추가 회복량
#     for i in range(len(attacks)): # 공격 시간 길이만큼 for문
#         while start != attacks[i][0] + 1: # start의 값이 공격하는 시간과 같을 때까지
#             if attacks[i][0] == start: # 현재 초가 공격이 존재하는 초라면
#                 if hp - attacks[i][1] <= 0:
#                     hp = -1
#                     break
#                 else:
#                     hp -= attacks[i][1] # hp 깎기
#                     cnt = 0
#             else: # 회복하는 초라면
#                 cnt += 1 # 연속 횟수 추가
#                 if hp < health: # 풀피가 아닐때만
#                     hp += recovery # 회복시켜주기
#             if cnt == time and hp > 0:
#                 cnt = 0
#                 if hp + recovery_plus >= health:
#                     hp = health
#                 else:
#                     hp += recovery_plus
#             start += 1
#         if hp <= 0:
#             hp = -1
#             break
                
#     return hp