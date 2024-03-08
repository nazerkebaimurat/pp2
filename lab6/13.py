#Write a Python program to copy the contents of a file to another file
def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as src_file:
            contents = src_file.read()
        with open(destination_file, 'w') as dest_file:
            dest_file.write(contents)
        print(f"Contents of '{source_file}' copied to '{destination_file}' successfully.")
    except FileNotFoundError:
        print("Error: One or both files not found.")
source_file = input("Enter the source filename: ")
destination_file = input("Enter the destination filename: ")
copy_file(source_file, destination_file)
