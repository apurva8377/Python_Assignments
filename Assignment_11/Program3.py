#################################################################################################
#
#   Program Name : Program3.py (Assignment_11)
#   Discription  : Write a program which accepts one number from user and prints sum of digits
#   Function     : Display()
#   Author       : Apurva Vilas Shinde
#   Date         : 22/01/2026
#
##################################################################################################

#    Input  : 7+5+2+1
#    Output : 15

def (No):
    Sum = 0
    Digit = 0
    i = 0

    while No > 0:
        Digit = No % 10
        Sum = Sum + Digit
        No = No // 10

    return Sum


def main():
    Value = 0
    Ret = 0

    print("Enter the number : ")

    Value = int(input())

    Ret = SumDigits(Value)

    print("Sum of digits in",Value,"is",Ret)

if __name__ == "__main__":
    main()



