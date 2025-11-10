def decorator1(func):
    def wrapper():
        print("before hello world")
        func()
        print("after hello world")
    return wrapper()
def decorator2(func):
    def wrapper():
        print("before hello world2")
        func()
        print("after hello world2")
    return wrapper()

@decorator2
#@decorator2
def say_hello():
    print("Hello World")

