#################################################################################################
#
#   Program Name : Program4.py (Assignment_11)
#   Discription  : Write a program which accepts one number from user and prints reverse of that number
#   Function     : Display()
#   Author       : Apurva Vilas Shinde
#   Date         : 22/01/2026
#
##################################################################################################

#    Input  : 123
#    Output : 321

def ReverseNumber(No):
    Rev = 0
    Digit = 0

    while No > 0:
        Digit = No % 10
        Rev = (Rev*10) + Digit
        No = No // 10

    return Rev


def main():
    Value = 0
    Ret = 0

    print("Enter the number : ")

    Value = int(input())

    Ret = ReverseNumber(Value)

    print("Reverse of",Value,"is",Ret)

if __name__ == "__main__":
    main()