import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(T):
    day = input().zfill(8)
    year = day[:4]
    month = day[4:6]
    days = day[6:]
    if int(month) >= 1 and int(month) <= 12:
        if int(month) in [1, 3, 5, 7, 8, 10, 12]:
            if int(days) >= 1 and int(days) <= 31:
                print(f"#{t+1} {year}/{month}/{days}")
            else:
                print(f"#{t+1} -1")
        elif int(month) in [4, 6, 9, 11]:
            if int(days) >= 1 and int(days) <= 30:
                print(f"#{t+1} {year}/{month}/{days}")
            else:
                print(f"#{t+1} -1")
        else:
            if int(days) >= 1 and int(days) <= 28:
                print(f"#{t+1} {year}/{month}/{days}")
            else:
                print(f"#{t+1} -1")
    else:
        print(f"#{t+1} -1")