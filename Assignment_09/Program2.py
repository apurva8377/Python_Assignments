####################################################################################################################################
#
#   Program Name : Program2.py
#   Discription  : Write a program which containes one function ChkGreater() that accepts two numbers and prints the greater number
#   Function     : ChkGreater()
#   Author       : Apurva Vilas Shinde
#   Date         : 18/01/2026
#
####################################################################################################################################

#   Input  : 10, 20
#   Output : 20 is greater


def ChkGreater(No1, No2):
    if(No1 > No2):
        return True
    else:
        return False


def main():
    Value1 = 0
    Value2 = 0
    Ret = 0

    print("Enter first number : ")
    Value1 = int(input())

    print("Enter second number : ")
    Value2 = int(input())

    Ret = ChkGreater(Value1, Value2)

    if(Ret == True):
        print(Value1," is greater")
    else:
        print(Value2," is greater")

if __name__ == "__main__":
    main()