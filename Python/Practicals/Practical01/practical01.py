#C:\Users\serea\Downloads\FY_BCA\Python\Codes\Practical01
"""
Control Flow with if, else, and Loops:
Write a program to calculate the grade of a student based on marks entered. 
● Use if-elif-else conditions to assign grades (e.g., A, B, C, D). 
● Use a for loop to input marks for 5 subjects and calculate the average. 
● Use a while loop to ask the user if they want to calculate another student’s grade
"""

counter = 0
score = 0
while True:
    for counter in range(5):
        if counter == 0:
            marks = int(input("Enter your marks in Physics: "))
        elif counter == 1:
            marks = int(input("Enter your marks in Chemistry: "))
        elif counter == 2:
            marks = int(input("Enter your marks in Mathematics: "))
        elif counter == 3:
            marks = int(input("Enter your marks in Biology: "))
        elif counter == 4:
            marks = int(input("Enter your marks in Computer: "))
        counter =+1
        score += marks
    grades = (score/500)*100
    if grades >=80:
        print("You got A grade")
    elif grades >=60:
        print("You got B grade")
    elif grades >=40:
        print("You got C grade")
    else:
        print("You got D grade")
    
    print(f"The average marks is {score/5}")
    another = input("Press 1 to calcualte average of another student: ")
    if another == "1":
        score =0
    else: 
        break
