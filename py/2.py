import re
def fin(pattern, seq):
    sequence = re.findall(pattern, seq)
    if sequence:
        print(f"found: ")
        for string in sequence:
            print(seq)
    else:
        print(f"does not found: ")
pattern = r'[a-z].'
seq = str(input())
