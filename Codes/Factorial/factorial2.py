"""
More advance approach
Q) Find the factorial of a given number  using a python code 
    INPUT: 3
    OUTPUT: The factorial of 3 is: 6

    INPUT: 5
    OUTPUT: The factorial of 5 is: 120

= APPROACH:
  1. declear a variable (let input_num) to store the input as int
  2. save the initial value inside another variable (let inital_value)
  3. make a while loop that runs till input variable becomes 0
  4. inside the while loop declear a variable (let factorial) with value 1
  5. multiply the value of the variable with input variable and save it init
  6. reduce the value of input variable by 1
  7. print the result
"""


input_value = int(input("Enter your number: "))
initial_value = input_value
factorial = 1

# with the use if while loop
while input_value >0:
  factorial *= input_value
  input_value -= 1

# with the use of for loop
for i in range(0, input_value):
  factorial *=input_value
  input_value -= 1


# making a function
def factorial_function(input_num):
  initial_value = input_num
  factorial  = 1
  for i in range(0,input_num):
    factorial *= input_num
    input_num -= 1
  print(f"The factorial of {initial_value} is {factorial}")

factorial_function(5)


