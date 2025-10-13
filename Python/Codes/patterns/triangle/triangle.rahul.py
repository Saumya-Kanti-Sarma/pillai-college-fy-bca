#code to print the star pattern using 'for' loop(left side)
rows = int(input("Enter No of rows to print star triangle(Left): "))

for i in range(1, rows+1):
	for j in range(1, i+1):
		print("*", end=" ")
	print()

'''output: 
  *
  **
  ***
  ****
'''

#code to print the star pattern using 'for' loop(right side)
rows = int(input("Enter No of rows to print star triangle(Right): "))

for i in range(1, rows+1):
        for j in range(rows-i):
                print(" ", end="")
        for k in range(1, i+1):
                print("*", end="")
        print()

'''output:
    *
   **
  ***
 ****
'''

#code to print the star pyramid
rows = int(input("Enter No of rows to print star pyramid pattern: "))

for i in range(1, rows + 1):
        for j in range(rows - i):
                print(" ", end="")
        for k in range(1, i + 1):
                print("*", end="")
                if k < i:
                        print(" ", end="")
        print()

'''output:
    *
   * *
  * * *
 * * * *
* * * * *
'''
