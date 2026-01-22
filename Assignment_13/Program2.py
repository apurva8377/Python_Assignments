############################################################################################################
#
#   Program Name : Program2.py (Assignment_13)
#   Discription  : Write a program which accepts radius of circle and prints area of circle
#   Function     : AreaOfCircle()
#   Author       : Apurva Vilas Shinde
#   Date         : 22/01/2026
#
#############################################################################################################

#  Input  :
#  Output :

def AreaOfCircle(radius):
    PI = 3.14
    Area = PI * (radius**2)
    return Area

def main():
    Radius = 0

    print("Enter radius of circle : ")
    Radius = float(input())

    Ret = AreaOfCircle(Radius)

    print("Area of circle is : ",Ret)

if __name__  == "__main__":
    main()