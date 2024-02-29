#Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
import re
def match(pattern, string):
    match = re.match(pattern, string)
    if match:
        print(f"String matches")
    else:
        print(f"String does not match")
pattern = r'ab{2, 3}'

string = str(input("String = "))
strings = string.split()
for string in strings:
    match(pattern, string)