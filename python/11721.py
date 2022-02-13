list = list(input())
for i in range(len(list)//10+1):
    start = i*10
    if start+9 < len(list):
        print(''.join(list[start:start+10]))
    else:
        print(''.join(list[start:]))