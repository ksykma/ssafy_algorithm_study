boxes = [7, 4, 2, 0, 0, 6, 0, 7, 0]

result = []
for i in range(len(boxes)):
    cnt = 0
    for j in range(i + 1, len(boxes)):
        if boxes[i] > boxes[j]:
            cnt += 1
    result.append(cnt)        

print(result)