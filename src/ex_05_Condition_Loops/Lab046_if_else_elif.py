# Problem  Find the Max between 3 numbers

# Logic Building

# User inputs - num1, num2, num3 -> int
# O/p -> int or String with max number .

num1=float(input("Enter the first  num :"))
num2=float(input("Enter the second num :"))
num3=float(input("Enter the third  num :"))

if(num1<=0 or num2<=0 or num3<=0):
   print("Enter a valid num")
else:
    if num1>num2>num3:
        print("num1 is max")
    elif num2>num3:
        print("num2 is max")
    else:
        print("num3 is max")
