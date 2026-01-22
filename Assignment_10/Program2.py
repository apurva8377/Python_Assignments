######################################################################################################################
#
#   Program Name : Program2.py (Assignment_02)
#   Discription  : Write a program which accepts one number and prints sum of first natural numbers
#   Function     : SumNatural()
#   Author       : Apurva Vilas Shinde
#   Date         : 22/01/2026
#
######################################################################################################################

# Input :  5 
# Output : 15

def SumNatural(No):
    Sum = 0
    i = 1

    while i <= No:
        Sum = Sum + i
        i = i + 1
    return Sum


def main():
    Value = 0
    Ret = 0

    print("Enter the number : ")
    Value = int(input())

    Ret = SumNatural(Value)

    print("Sum of natural number is : ",Ret)

if __name__ == "__main__":
    main()