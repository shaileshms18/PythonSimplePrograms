import re

for t in range(int(input())):
    S=raw_input()
    try:
        re.compile(S)
        print True
    except:
        print False