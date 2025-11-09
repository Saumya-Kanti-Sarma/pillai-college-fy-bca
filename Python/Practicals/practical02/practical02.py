str = (input("Enter a Word: ")).lower()
a = str.count("a")
e =str.count("e")
i = str.count("i")
o = str.count("o")
u = str.count("u")
print(f"the line has {a} a, {e} e, {i} i and {u} u")

word = input("Enter a word:")
rev = word[::-1]
if word == rev:
    print("the word is pallendromic")
else:
    print("the word is not pallendromic")

string = input("Enter a String: ")
print(string.upper())
print(string.lower())
print(string.title())
print(string.capitalize())

