############################################################################################################
#
#   Program Name : Program1.py (Assignment_11)
#   Discription  : Write a program which accepts one number from user and prints count of digits in that number
#   Function     : Display()
#   Author       : Apurva Vilas Shinde
#   Date         : 22/01/2026
#
#############################################################################################################

#    Input  : 7521
#    Output : 4

def CountDigits(No):
    Count = 0
    i = 0

    while No > 0:
        Count = Count + 1
        No = No // 10

    return Count


def main():
    Value = 0
    Ret = 0

    print("Enter the number : ")

    Value = int(input())

    Ret = CountDigits(Value)

    print("Number of digits in",Value,"is",Ret)

if __name__ == "__main__":
    main()