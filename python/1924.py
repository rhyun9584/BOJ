x, y = [int(x) for x in input().split()]
days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

after = 0
for i in range(1, x):
    after += month[i-1]

print(days[(after+y-1)%7])