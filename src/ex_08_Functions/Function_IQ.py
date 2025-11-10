# Create a program to sum of three number from the user input,
# if user doesn't enter any number', use default as 100, 200, 300

# Logic Building

# Step 1 - I/O and O/P
# I/O -  int
# O/P - int

# Step 2 - Rough Logic
# return n1+n2+n3


# Step 3 - Write Logic


number1=float(input("Enter a num1:"))
number2=float(input("Enter a num2:"))
number3=float(input("Enter a num3:"))

def sum_of_three_num(num1=10, num2=20, num3=30):
    return num1+num2+num3

result=sum_of_three_num()
print(result)

result1=sum_of_three_num(number1,number2,number3)
print(result1)

result3=sum_of_three_num(10,5,10)
print(result3)

result4=sum_of_three_num(5)
print(result4)