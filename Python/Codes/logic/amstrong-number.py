"""
Amstrong number
INPUT: 153
	step1: 1x1x1 + 5x5x5 + 3x3x3
	step2: check if the square sum of all this numbers are equal to input then this is an amstrong number
"""

x = input("Enter your number: ")
result = 0
for num in x:
	y = int(num)
	z = y*y*y
	result = result +z

print(result)
if int(x) == result:
	print("the number is an amstrong number")
else:
	print("the number is not an amstrong number")

	
