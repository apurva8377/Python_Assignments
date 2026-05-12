########################################################################
#
#   Program Name   : Assignment19_1.py
#   Author         : Apurva Vials Shinde
#   Description    : Write a program which contains one lambda function which accepts one parameter and return
# power of two.    
#   Input          : 4/6 
#   Output         : 16/64          
#   Date           : 11/05/2026
#
#######################################################################

PowerOfTwo = lambda No : 2 ** No

def main():
    Value = int(input("Enter the number : "))

    Ret = PowerOfTwo(Value)

    print("The",Value,"th power of 2 is : ",Ret)

if __name__ == "__main__":
    main()