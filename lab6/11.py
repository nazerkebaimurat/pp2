#Write a Python program to write a list to a file.
def write_list_to_file(filename, input_list):
    try:
        with open(filename, 'w') as file:
            for item in input_list:
                file.write(str(item) + '\n')
        print(f"The list has been successfully written to '{filename}'.")
    except IOError:
        print(f"Error: Unable to write to file '{filename}'.")
my_list = [1, 2, 3, 4, 5]
filename = input("Enter the filename to write the list to: ")
write_list_to_file(filename, my_list)
