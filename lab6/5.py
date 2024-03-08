#Write a Python program with builtin function that returns True if all elements of the tuple are true.
tuple_str = input("Tuple: ")
my_tuple = eval(tuple_str)
if isinstance(my_tuple):
    print("True")
else:
    print("False")