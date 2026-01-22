##########################################################################################################
#
#   Program Name : Program5.py
#   Discription  : Write a program which accepts one number and checks whether it is divisible by 3 and 5
#   Function     : CheckDivisible()
#   Author       : Apurva Vilas Shinde
#   Date         : 18/01/2026
#
##########################################################################################################

#   Input  :  12
#   Output :  Divisible by 3 and 5

def CheckDivisible(No):
    if (No % 3 == 0) and (No % 5 == 0):
        return True
    else:
        return False

def main():
    Value = 0
    Ret = False

    print("Enter the number : ")
    Value = int(input())

    Ret = CheckDivisible(Value)

    if Ret == True:
        print(Value," is divisible by 3 and 5")
    else:
        print(Value," is not divisible by 3 and 5")

if __name__ == "__main__":
    main()