import sys
input = sys.stdin.readline

def isVowel(ch):
    if ch in ['a', 'e', 'i', 'o', 'u']:
        return True
    else:
        return False

while True:
    password = input().rstrip()

    if password == 'end':
        break

    acceptable = isVowel(password[0])
    cnt = 1
    for i in range(1, len(password)):
        ch = password[i]

        # 모음 포함 확인
        if not acceptable:
            acceptable = isVowel(ch)

        # 모음 혹은 자음 3개 연속 확인
        if isVowel(ch) != isVowel(password[i-1]):
            cnt = 1
        else:
            cnt += 1
        
        if cnt == 3:
            acceptable = False
            break

        # 같은 문자 2개 연속 확인
        if ch not in ['e', 'o'] and password[i-1] == ch:
            acceptable = False
            break

    if acceptable:
        print(f"<{password}> is acceptable.")
    else:
        print(f"<{password}> is not acceptable.")
