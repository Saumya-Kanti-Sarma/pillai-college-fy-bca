"""
Q. You are given two number ( let 1,2) using this two number make a fibonacci series till the 10th index
    INPUT = 1,2
    OUTPUT = 1,2,3,5,8,12....

  ANSWER:
  let us assume x and y are the two variables and z is the output i.e sum of x and y. If we make a table then it looks something like this: 
    ____________________________
    x | 1 | 2 | 3 | 5  | 8  |...
    y | 2 | 3 | 5 | 8  | 12 |...
    z | 3 | 5 | 8 | 12 | 19 |...
    ____________________________

"""

x = 1
y = 2
print(f"{x}, {y}", end="")
for i in range(10):
  z = x+y
  x = y 
  y= z
  print(f", {z}", end="")
print("...")