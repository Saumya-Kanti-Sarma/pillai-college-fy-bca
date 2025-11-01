"""
Set Operations 
Perform operations on two sets of student names. 
●  Create sets for two classes. 
●  Find the union of both sets (students in either class). 
●  Find the intersection (students common to both classes). 
●  Find the difference (students unique to one class). 
●  Check if a student is part of a set using membership operators
"""

set1 = {'Saumya','Roshan','Abi','Akash','Joydrina'}
set2 = {'Abi','Akash','Susanti','Bhumika','Tvisha'}

# union
u = set1.union(set2)
print("Union of classes:",u)

#intersection
i = set1.intersection(set2)
print("Intersection of classes:",i)

#difference
d = set1.difference(set2)
print("Difference of classes:",d)

#checking membership
if 'Saumya' in set1:
  print("Saumya is available in class")


