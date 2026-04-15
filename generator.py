# create a generator that prints 0, 2, 4, 6, 8,...,10

def even():
    for i in range(1, 10, 2):
        yield i
        
for num in even():
    print(num)
