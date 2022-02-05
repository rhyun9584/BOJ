N = int(input())
A_list = [int(x) for x in list(input().split())]
op = [int(x) for x in list(input().split())]

result = []
def operation(ex_val, idx, sum, sub, mul, div):
    # 계산이 끝났다면, max와 min 값과 비교
    if idx == N:
        result.append(ex_val)
        return

    if sum > 0:
        val = ex_val + A_list[idx]
        operation(val, idx+1, sum-1, sub, mul, div)
    if sub > 0:
        val = ex_val - A_list[idx]
        operation(val, idx+1, sum, sub-1, mul, div)
    if mul > 0:
        val = ex_val * A_list[idx]
        operation(val, idx+1, sum, sub, mul-1, div)
    if div > 0:
        val = int(ex_val/A_list[idx])
        operation(val, idx+1, sum, sub, mul, div-1)

operation(A_list[0], 1, op[0], op[1], op[2], op[3])

print(max(result))
print(min(result))