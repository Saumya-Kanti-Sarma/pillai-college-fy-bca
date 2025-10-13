"""
Q. Write a python code to reverse a number and check if it's pallindrome or not? NOTE: you cannot convert the number into string 
    INPUT: 123
    OUTPUT: 321
"""
x = 123
rev = 0
counter = 0
while counter <3:
  y = x%10          # y => 123 % 10 = 3
  rev = rev *10 + y # rev => 0 *10 + 3 = 3
  # print(rev)      # 3
  x = int(x/10)     # x => 123/10 => 12.3 = int(12.3) => 12
  counter +=1       # counter = 0 + 1


