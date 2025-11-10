def before_after_test_ui(func):

    def wrapper():
        print("Before test ui")
        func()
        print("After test ui")
    return wrapper()







@before_after_test_ui
def test_ui():
    print("test_ui")