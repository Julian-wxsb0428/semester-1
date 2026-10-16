# Worksheet 1.2: Task 1 Solution
grade=input("Please enter your grade(between 0 and 100): ")
import sys
def check_grade(grade):
    valid= grade.isdecimal() and 0<=int(grade)<=100
    if not valid:
        sys.exit("Error!")
check_grade(grade)
grade=int(grade)
if grade>=0 and grade<=39:
    print(f"{grade}is a Fail")
elif grade>=40 and grade<=69:
    print(f"{grade}is a Pass")
else:
    print(f"{grade}is a Distinction")
    