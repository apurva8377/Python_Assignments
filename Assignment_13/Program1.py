############################################################################################################
#
#   Program Name : Program1.py (Assignment_13)
#   Discription  : Write a program which accepts length and width of rectangle and prrints area
#   Function     : AreaOfrectangle()
#   Author       : Apurva Vilas Shinde
#   Date         : 22/01/2026
#
#############################################################################################################

#  Input  : 4   5
#  Output : 20.0

def AreaOfRectangle(length, width):
    Area = length * width
    return Area

def main():
    Length = 0
    Width = 0
    Ret = 0

    print("Enter length of rectangle : ")
    Length = float(input())

    print("Enter width of rectangle : ")
    Width = float(input())

    Ret = AreaOfRectangle(Length, Width)

    print("Area of rectangle is : ",Ret)

if __name__  == "__main__":
    main()