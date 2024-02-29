#Write a Python program to split a string at uppercase letters.
import re
def conv(text):
    text1 = re.findall(r'[A-Z][^A-Z]', text)

    return text1
text = str(input("Input = "))
text1 = conv(text)
print(text1)