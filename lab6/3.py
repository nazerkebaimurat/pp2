#Write a Python program with builtin function that checks whether a passed string is palindrome or not.
def palindrome(string):
    string1 = string
    string1.reverse()
    if string1 == string:
        return 'yes'
    else:
        return 'no'
string = input("String: ")
result = palindrome(string)
print(result)