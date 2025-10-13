
#checking pallendromic words with using forloop
word = "saumya"
"""
rev = ""
index = len(word) - 1
for i in range(0,index +1):
    #print(i)
    rev += word[index - i]
    #print(word[index - i],end="")

print(rev)
if word == rev:
    print("the word is pallendromic")
else:
    print("the word is not pallendromic")
"""

#checking pallendromic word using buildin method
rev = word[::-1]
if word == rev:
    print("the word is pallendromic")
else:
    print("the word is not pallendromic")
