#Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.
import os
def delete_file(path):
    try:
        if not os.path.exists(path):
            print(f"Error: File '{path}' does not exist.")
            return
        if not os.access(path, os.R_OK | os.W_OK):
            print(f"Error: No read/write access to file '{path}'.")
            return
        os.remove(path)
        print(f"File '{path}' has been deleted successfully.")
    except Exception as e:
        print(f"An error occurred while deleting the file: {e}")
file_path = input("Enter the path of the file to delete: ")
delete_file(file_path)
