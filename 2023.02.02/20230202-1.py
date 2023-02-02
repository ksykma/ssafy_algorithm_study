# 카운팅 정렬

A = [0, 4, 1, 3, 1, 2, 4, 1]
C = [0, 0, 0, 0, 0]
B = [0, 0, 0, 0, 0, 0, 0, 0]

for i in range(0, len(A)):
    C[A[i]] += 1

print(C)

for i in range(1, len(C)):
    C[i] += C[i-1]

print(C)

for i in range(7, -1, -1):
    C[A[i]] -= 1
    B[C[A[i]]] = A[i]

print(B)


# 자료의 빈도수 계산
K = 4
D = [0] * (K + 1)
E = [0] * len(A)
for val in A:
    D[val] += 1
print(D)

# 누적 빈도수 계산
for j in range(1, K + 1):
    D[j] += D[j - 1]
print(D)

# 원자료들을 하나씩 정렬 될 위치로 복사
for val in A:
    # A -> E로
    D[val] -= 1
    E[D[val]] = val

print(E)