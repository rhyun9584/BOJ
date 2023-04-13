word = input()

count = [0] * (ord('Z') - ord('A') + 1)
for w in word:
    w = w.upper()

    idx = ord(w) - ord('A')
    count[idx] += 1

max_count = max(count)
result = []
for i in range(0, len(count)):
    if count[i] == max_count:
        result.append(chr(ord('A')+i))

if len(result) > 1:
    print("?")
else:
    print(result[0])