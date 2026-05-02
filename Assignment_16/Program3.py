####################################################################################################
#
#   Program Name : Assignment16_3.py
#   Author       : Apurva Vials Shinde
#   Description  : Write a program which contains one function named as Add() which accepts two numbers from user and return addition of that two numbers.
#   Function     : Add(No1, No2)        
#   Input        : 11 , 5           
#   Output       : 16
#   Date         : 01/05/2026
#
####################################################################################################

def Add(No1, No2):
    Ans = 0
    Ans = No1 + No2
    return Ans

def main():
    Value1 = int(input("Enter the first number : "))

    Value2 = int(input("Enter the second number : "))

    Ret = Add(Value1,Value2)

    print("Addition is : ",Ret)

if __name__ == "__main__":
    main()
