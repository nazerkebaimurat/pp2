#Write a Python program with builtin function to multiply all the numbers in a list
from functools import reduce
def mult(nums):
    result = reduce(lambda a, b: a*b, nums)
    return result
n_str = input("List: ")
nums = [int(x) for x in n_str.split()]
result = mult(nums)
print(result)