#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
import re
def match(pattern, string):
    strings = re.findall(pattern, string)
    if strings:
        print(f"String matches: ")
        for string in strings:
            print(string)
        else:
            print(f"String does not match")
pattern = r'a.*b$'
string = str(input("String = "))
match(pattern, string)
