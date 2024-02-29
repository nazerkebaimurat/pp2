#Write a Python program to replace all occurrences of space, comma, or dot with a colon.
import re
def repl(pattern, text):
    pattern = r'[ ,.]'
    text1 = re.sub(pattern, ':', text)
    return text1
text = str(input("Input = "))
text1 = repl(text)
print(text1)