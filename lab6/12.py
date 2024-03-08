#import string
import string
def generate_files():
    uppercase_letters = string.ascii_uppercase
    for letter in uppercase_letters:
        filename = f"{letter}.txt"
        with open(filename, 'w'):
            pass  
generate_files()
