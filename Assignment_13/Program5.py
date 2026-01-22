############################################################################################################
#
#   Program Name : Program5.py (Assignment_13)
#   Discription  : Write a program which accepts marks and displays grades
#   Function     : DisplayGrades()
#   Author       : Apurva Vilas Shinde
#   Date         : 22/01/2026
#
#############################################################################################################

#  Input  : 5
#  Output : Binary equivalent is : 101

def DisplayGrades(marks):
    if marks < 0 or marks > 100:
        print("Invalid marks")
        return
    
    if marks >= 0 and marks < 35:
        print("You are fail")
    elif marks >= 35 and marks < 50:
        print("Pass class")
    elif marks >= 50 and marks < 60:
        print("Second class")
    elif marks >= 60 and marks < 70:
        print("First class")
    elif marks >= 70 and marks <= 100:
        print("First class with distinction")

def main():
    Marks = 0

    print("Enter the marks : ")
    Marks = int(input())

    DisplayGrades(Marks)

if __name__  == "__main__":
    main()