def gen():
    for i in range(10, 101, 11):
        yield i
for nums in gen():
    print(nums)
