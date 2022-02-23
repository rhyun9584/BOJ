import sys

strings = sys.stdin.readlines()
for s in strings:
    little = big = num = space = 0
    for ch in s:
        if 'a' <= ch <= 'z':
            little += 1
        elif 'A' <= ch <= 'Z':
            big += 1
        elif '0' <= ch <= '9':
            num += 1
        elif ch == ' ':
            space += 1
    
    print(little, big, num, space)