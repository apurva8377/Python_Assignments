########################################################################
#
#   Program Name : Assignment17_9.py
#   Author       : Apurva Vilas Shinde
#   Description  : Write a program which accept number from user and return number of digits in that number.
#   Input        : 5187934
#   Output       : 7
#   Date         : 04/05/2026
#
#######################################################################

def CountDigits(No):
    if(No < 0):
        No = -No

    if No == 0:
        return 1
    
    Count = 0
    
    while(No != 0):
        Count = Count + 1
        No = No // 10

    return Count

def main():
    try:
        Value = int(input("Enter number : "))
        Ret = CountDigits(Value)
        print("The number of digits in",Value,"is : ",Ret)
    except ValueError:
        print("invalid input. Please enter valid input")

if __name__ == "__main__":
    main()