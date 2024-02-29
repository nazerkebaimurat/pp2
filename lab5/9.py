#Write a Python program to insert spaces between words starting with capital letters.
import re
def insrt(text):
    text1 = re.sub(r'([A-Z][a-z]+)', r' \1', text)
    return text1
text = input("Input = ")
text1 = insrt(text)
print(text1)