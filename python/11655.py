import sys

string = sys.stdin.readline().rstrip()
for ch in string:
    if ch.isalpha():
        new_ch = chr(ord(ch)+13)

        if ch.islower() and new_ch.islower() == False:
            new_ch = chr(ord(new_ch)-26)
        elif ch.isupper() and new_ch.isupper() == False:
            new_ch = chr(ord(new_ch)-26)

        print(new_ch, end='')
    else:
        print(ch, end='')
