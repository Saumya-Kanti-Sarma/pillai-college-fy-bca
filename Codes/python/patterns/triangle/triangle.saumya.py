"""
1. White a python code using for loop that print this triangle
    *
    **
    ***
    ****
"""
for i in range(5):
  print("*"*i)

"""
2. White a python code using for loop that print this triangle
       *
      **
     ***
    ****
"""
for i in range(5):
  s = 4 - 1
  print(f"{" "*s}{"*"*i}")

"""
3. White a python code using for loop that print this triangle
       *
      * *
     * * *
    * * * *
"""
for i in range(5):
  s = 4 - 1
  print(f"{" "*s}{" *"*i}")