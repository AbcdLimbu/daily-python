import time

def timer(func):
    def wrapper():
        start = time.time()
        print("Before Time")
        func()
        print("After time")
        end = time.time()
        print("Time: ", end - start)
    return wrapper

@timer
def test():
    for i in range(1, 1000):
        pass

test()
