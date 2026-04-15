def count():
    for i in range(1, 10):
        return i

def numbers():
    for i in range(1, 10):
        yield i

num = numbers()
print(next(num))
