############################################################################################################
#
#   Program Name : Program3.py (Assignment_13)
#   Discription  : Write a program which accepts number and prints binary equivalant
#   Function     : BinaryEquivalent()
#   Author       : Apurva Vilas Shinde
#   Date         : 22/01/2026
#
#############################################################################################################

#  Input  : 5
#  Output : Binary equivalent is : 101

def BinaryEquivalent(No):
    Binary = ""
    Digit = 0

    while No > 0:
        Digit = No % 2
        Binary = str(Digit) + Binary
        No = No // 2

    print("Binary equivalent is :",Binary)

def main():
    Value = 0

    print("Enter the number : ")
    Value = int(input())

    BinaryEquivalent(Value)

if __name__  == "__main__":
    main()