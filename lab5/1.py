#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
import re
def string(pattern, str):
    match = re.match(pattern, str)
    if match:
        print(f"String '{str}' matches the pattern '{pattern}'")
    else:
        print(f"Does not match")

pattern = r'ab*'

str = str(input("String = "))

for str in string:
    string(pattern, str)
