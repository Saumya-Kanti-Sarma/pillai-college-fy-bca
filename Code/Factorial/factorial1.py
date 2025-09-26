"""
Q) Find the factorial of a given number (let 3) using a python code and not using  for loop
    INPUT: 3
    OUTPUT: The factorial of 3 is: 6

= APPROACH:
  1. declear a variable (let input_num) to store the input as int
  2. save the initial value inside another variable (let inital_value)
  3. declear a varaible (let factorial) with initial value as 1
  4. multiply the variable (factorial) with the input value (input_num) to increment it 
  5. subtract 1 from the input variable (input_num)
  6. repeat the 4ht and 5th step for 2 more times
  7. print the statement
"""
input_num = int(input("Enter your number: ")) #takes the input from user and saves it as in integer value
initial_value = input_num #storing the initial value in saperate variable

factorial = 1

factorial = factorial * input_num # factorial = 1x3 =3
input_num = input_num - 1 #input_num = 3-1 = 2

factorial = factorial * input_num # factorial = 3x2 = 6
input_num = input_num - 1 #input_num = 2-1 =1

factorial = factorial * input_num # factorial = 6x1 = 6
input_num = input_num - 1 #input_num = 1-1 = 0

print(f"The factorial of {initial_value} is: {factorial}")



