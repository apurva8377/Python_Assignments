##################################################################################################
#
#   Program Name : Program3.py
#   Discription  : Write a program which accepts one number and prints square of that number
#   Function     : Square()
#   Author       : Apurva Vilas Shinde
#   Date         : 18/01/2026
#
###################################################################################################

#   Input  :  5
#   Output :  25

def Square(No):
    Ans = No ** 2
    # Ans = No * No

    return Ans

def main():
    Value = 0
    Ret = 0

    print("Enter the number : ")
    Value = int(input())

    Ret = Square(Value)

    print("Square of ",Value," is : ",Ret)

if __name__ == "__main__":
    main()