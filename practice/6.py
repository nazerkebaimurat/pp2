def gen(n):
    while n <= 0:
        yield n
        n -= 1
    
n = int(input("n = "))
for num in gen(n):
    print(num, sep=" ")
