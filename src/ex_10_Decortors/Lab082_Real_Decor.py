import time


def print_logs(func):
    def wrapper():
        print("Start of Logs")
        func()
        print("End of Logs")
    return wrapper()

def time_decorator(func):
    def wrapper():
        start_time= time.time()
        print(start_time)
        func()
        ent_time=time.time()
        print(ent_time)
    return wrapper()


#@print_logs
@time_decorator
def test_ui_1():
    print("Add a function, time taken by this function 1")


#@print_logs
@time_decorator
def test_ui_2():
    print("Add a function, time taken by this function 2")