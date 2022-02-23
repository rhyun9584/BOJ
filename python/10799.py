import sys

string = sys.stdin.readline()
string = string.replace("()", ".")

count = 0
pipe = 0
for ch in string:
    if ch == '(':
        pipe += 1
    elif ch == ')':
        count += 1
        pipe -= 1
    elif ch == '.':
        count += pipe

print(count)