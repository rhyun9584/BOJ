N = int(input())
table = [[int(x) for x in input().split()] for _ in range(N)]

max_profit = 0
def get_work(start, now_profit):
    global max_profit

    is_end = True
    for day in range(start, N+1):
        next_date = day + table[day-1][0]
        if next_date <= N+1:
            is_end = False
            now_profit += table[day-1][1]
            get_work(next_date, now_profit)
            now_profit -= table[day-1][1]
        
    if is_end:
        max_profit = max(max_profit, now_profit)
        return

get_work(1, 0)
print(max_profit)