participants =  [3, 7, 100, 21, 13, 6, 5, 7, 5, 6, 3, 13, 21]

lst = []
for i in participants:
    cnt = 0
    for j in participants:
        if i == j:
            cnt += 1
    if cnt == 2:
        lst.append(i)

participants = [k for k in participants if k not in lst]
print(participants[0])