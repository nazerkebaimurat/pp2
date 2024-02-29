#Write a Python program to find sequences of lowercase letters joined with a underscore.
import re
def lowerstr(pattern, seq):
    sequence = re.findall(pattern, seq)
    if sequence:
        print(f"Secuence found: ")
        for string in sequence:
            print(seq)
    else:
        print(f"Sequence does not found")
pattern = r'\b[a-z]+_[a-z]+\b'

seq = str(input())