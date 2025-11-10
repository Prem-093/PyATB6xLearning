# User Defined
# 1. They can't return -> non return
# 2.They can return something
# 3.They have parameters
# 4. They don't parameters / arguments


def user_name():
    print("Hello!")

user_name()



def multipy_Addition_subs_divide(num1, num2):
    return num1+num2,num1*num2,num1+num2,

mathOpertion=multipy_Addition_subs_divide(30,20)
print(mathOpertion)


def Argument(name="Pramod"):
    print("Hello",name.upper())

Argument("Prem")
Argument()

def multiplr_args(name1="A", name2="B"):
    print("mul:",name1,name2)

multiplr_args()
multiplr_args("Prem","Tripathi")
multiplr_args(name1="Kartik")
multiplr_args(name2="Tripathi")


def sum_of_two_numbers(num1=10,num2=20):
    return num1+num2

result=sum_of_two_numbers(30,40)
print(result)


result=sum_of_two_numbers()
print(result)
