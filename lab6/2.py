#Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
def calc(string):
    upper_cnt = 0 
    lower_cnt = 0
    for char in string:
        if char.isupper():
            upper_cnt += 1
        if char.islower():
            lower_cnt += 1
    return upper_cnt, lower_cnt

string = input("String: ")
upper_cnt, lower_cnt  = calc(string)
print("Number of upper case letters: ", upper_cnt)
print("NUmber of lower case letters: ", lower_cnt)
