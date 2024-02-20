#Create a generator that generates the squares of numbers up to some number N
#1
def squares(n):
    for i in range(1, n+1):
        yield i ** 2

n = int(input("n = "))
for square in squares(n):
    print(square)

#Write a program using generator to print the even numbers
#between 0 and n in comma separated form where n is input from console.
#2
def evennum(n):
    for i in range(0, n+1, 2):
        yield i

n = int(input("n = "))
even = evennum(n)

print(*even, sep=",")

#Define a function with a generator which can iterate the numbers, 
#which are divisible by 3 and 4, between a given range 0 and n.
#3
def gen(n):
    for i in range(0, n+1):
        yield i

n = int(input("n = "))
for i in gen(n):
    if i % 3 == 0 and i % 4 == 0:
        print(i, sep=" ")

#Implement a generator called squares to yield the square of all numbers from (a) to (b). 
#Test it with a "for" loop and print each of the yielded values.
#4
def squares(a, b):
    for i in range(a, b+1):
        yield i ** 2

a = int(input("a = "))
b = int(input("b = "))

for square in squares(a, b):
    print(square)

#Implement a generator that returns all numbers from (n) down to 0.
#5
def gen(n):
    while n >= 0:
        yield n
        n -= 1
    
n = int(input("n = "))
for num in gen(n):
    print(num)

