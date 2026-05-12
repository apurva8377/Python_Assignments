########################################################################
#
#   Program Name   : Assignment19_2.py
#   Author         : Apurva Vials Shinde
#   Description    : Write a program which contains one lambda function which accepts two parameters and return its multiplication.
#   Input          : 4  3 / 6   3
#   Output         : 12 / 18         
#   Date           : 11/05/2026
#
#######################################################################

Multiplication = lambda No1,No2 : No1 * No2

def main():
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))

    Ret = Multiplication(Value1, Value2)

    print("The multiplication of",Value1,"&",Value2,"is : ",Ret)

if __name__ == "__main__":
    main()