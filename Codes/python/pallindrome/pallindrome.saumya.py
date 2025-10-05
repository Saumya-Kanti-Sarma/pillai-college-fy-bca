"""
Q. You are given a string or a number. Write a python code to check if it is pallindrom or not WITHOUT using string slicing method.
    Example 01.
      INPUT = 123
      OUTPUT = 321
      RESULT = the word is not pallindromic
    Example 01.
      INPUT = "madam"
      OUTPUT = "madam"
      RESULT = the world is pallindromic
"""

x = input("enter a word or an number: ")
len_x = len(x) - 1
rev = ""

for i in range( len_x +1):
  y = len_x -i
  # print(y)
  rev = rev + x[y]

if( rev == x):
  print("the word is pallindromic")
else:
  print("the word is not pallendromic")

