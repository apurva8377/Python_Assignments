########################################################################
#
#   Program Name : Assignment17_10.py
#   Author       : Apurva Vilas Shinde
#   Description  : Write a program which accept number from user and return addition of digits in that number.
#   Input        : 5187934
#   Output       : 37
#   Date         : 04/05/2026
#
#######################################################################

def AddDigits(No):
    if(No < 0):
        No = -No

    if No == 0:
        return 1
    
    Sum = 0
    
    while(No != 0):
        Digit = No % 10
        Sum = Sum + Digit
        No = No // 10

    return Sum

def main():
    try:
        Value = int(input("Enter number : "))
        Ret = AddDigits(Value)
        print("The Summation of digits in",Value,"is : ",Ret)
    except ValueError:
        print("invalid input. Please enter valid input")

if __name__ == "__main__":
    main()