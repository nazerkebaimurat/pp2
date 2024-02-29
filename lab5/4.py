#Write a Python program to find the sequences of one upper case letter followed by lower case letters
import re
def finded(pattern, seq):
    sequence = re.findall(pattern, seq)
    if sequence:
        print(f"String matches: ")
        for seq in sequence:
            print(seq)
        else:
            print(f"String does not match")
pattern = r'\b[A-B]+[a-b\b]'
seq = str(input("String = "))
finded(pattern, seq)