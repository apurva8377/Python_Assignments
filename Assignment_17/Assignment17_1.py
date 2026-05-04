########################################################################
#
#   Program Name : Assignment17_1.py
#   Author       : Apurva Vials Shinde
#   Description  : Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub( for subtraction, Mult() for multiplication and Div() for division. All functions accepts two parameters as number and perform the operation. Write on python program which call all the functions from Arithmetic module by accepting the parameters from user.
#   Function     : import from Module Arithmatic      
#   Input        : 10,5        
#   Output       : Addition is : 10
#                  Substaction is : 5
#                  Multiplication is : 50
#                  Division is : 2.0
#   Date         : 01/05/2026
#
#######################################################################

import Arithmetic

def main():
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))

    print("Addition is : ",Arithmetic.Add(Value1,Value2))
    print("Substaction is : ",Arithmetic.Sub(Value1,Value2)) 
    print("Multiplication is : ",Arithmetic.Mult(Value1,Value2))
    print("Division is : ",Arithmetic.Div(Value1,Value2))

if __name__ == "__main__":
    main()