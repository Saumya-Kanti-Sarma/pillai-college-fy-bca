str = input("Enter a message: ")

a = str.count("a")
e =str.count("e")
i = str.count("i")
o = str.count("o")
u = str.count("u")
print(f"the line has {a} a, {e} e, {i} i and {u} u")


"""
#Building my own logic with loops
a,e,i,o,u =0,0,0,0,0
for char in str:
	char.lower()
	if "a" == char:
		a+=1
	if "e" == char:
		e+=1
	if "i" == char:
		i+=1
	if "o" == char:
		o+=1
	if "u" == char:
		u+=1
"""
