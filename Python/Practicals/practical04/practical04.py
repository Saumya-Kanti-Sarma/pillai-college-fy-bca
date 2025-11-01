"""
Tuples and Their Applications 
Create a program to handle student records. 
● Store student details (roll number, name, marks) in a tuple. 
● Use tuple unpacking to retrieve the details. 
● Create a function that accepts variable-length argument tuples and calculates the 
average marks of the students.
"""
roll_no, name, marks = (2570,"Saumya Kanti Sarma",280)
print("Roll No: ",roll_no)
print("Name: ",name)
print("Marks: ",marks)

def average_marks(*args):
    marks = tuple(args)
    total_marks = 0
    for mark in marks:
        total_marks += mark
    ave = total_marks/len(marks)
    return ave
    

average_score = average_marks(50,45,81,88,90)
print("The average score is: ",average_score)
