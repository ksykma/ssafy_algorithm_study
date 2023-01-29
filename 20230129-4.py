import sys
sys.stdin = open('input.txt', 'r')

alphabets = input()

for alphabet in alphabets:
    print(ord(alphabet)-64, end = ' ')