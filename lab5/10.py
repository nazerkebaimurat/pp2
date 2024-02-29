#Write a Python program to convert a given camel case string to snake case.
import re
def conv(text):
    text1 = ' '
    for i, char in enumerate(text):
        if char.isupper() and i != 0:
            text1 += '_'
        text1 += char.lower()
    return text1
text = input("Input = ")
text1 = conv(text)
print(text1)
