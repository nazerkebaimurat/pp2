#Write a Python program to count the number of lines in a text file.
def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            line_count = 0
            for line in file:
                line_count += 1
        return line_count
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return -1
filename = input("Enter the filename: ")
num_lines = count_lines(filename)
if num_lines >= 0:
    print(f"The number of lines in '{filename}' is: {num_lines}")
