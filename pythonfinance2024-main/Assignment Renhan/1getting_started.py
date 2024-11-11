#1getting_started.py

# 1. Syntax

# 1.1 Insert the missing indentation to make the code correct:
# HINT: https://www.w3schools.com/python/python_syntax.asp

# TODO: update the code below
if 4 ==2 :
  print("Four is equal to two!")


# 1.2 Variables
# HINT: https://www.w3schools.com/python/python_variables.asp

#1.2.1 Create a variable named fruit and assign the value Apple to it.
# TODO: Write your code below
fruit="Apple"


# 1.2.2 Create a variable called z, assign x + y to it, and display the result.

x = 10
y= 20

# TODO: Wrtie your code below
z=x+y


# 1.2.3 Remove the illegal characters in the variable name:

# TODO: Update the code below
city-name = "London"

# 1.2.4 Insert the correct keyword to make the variable x belong to the global scope.
# HINT: https://www.w3schools.com/python/python_variables_global.asp

# TODO: Update the code below
def myfunc():
  global x
  x = "fantastic"



# 1.2.5 write a program that switches the values stored in variables a and b.

a = 5
b = 4

# TODO: Write your code below
c=a
d=b
a=d
b=c


print('a : ',a)
print('b : ',b)


# 1.3. Data Types
# casting, numbers, booleans
# HINT: https://www.w3schools.com/python/python_datatypes.asp

# 1.3.1 Write a program that add the digits in a two digit number input.
# eg. if the input is 45. The the output should be 4+5=9

number = input("Enter a two-digit number: ")

# TODO: Wrtie your code below

# Check if the input is a valid two-digit number
if len(number) == 2 and number.isdigit():
    # Convert each character to an integer and add them
    digit_sum = int(number[0]) + int(number[1])
    print(f"{number[0]} + {number[1]} = {digit_sum}")
else:
    print("Please enter a valid two-digit number.")