def collatz(num):
    cnt = 0
    while True:
        if num != 1:
            if num % 2 == 0:
                num = num / 2
                cnt += 1
            else:
                num = num * 3 + 1
                cnt += 1
        else:
            break
    if cnt > 500:
        return -1
    else:
        return cnt
print(collatz(6))  # => 8
print(collatz(16))  # => 4
print(collatz(27))  # => 111
print(collatz(626331))  # => -1