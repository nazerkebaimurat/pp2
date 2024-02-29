#Write a python program to convert snake case string to camel case string.
import re
def conv(text):
    words = text.split('_')
    text1 = words[0] + ''.join(word.capitalize()for word in words[1:])
    return text1
text = str(input("Input = "))
text1 = conv(text)
print(text1)
