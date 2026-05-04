########################################################################
#
#   Program Name : Assignment17_4.py
#   Author       : Apurva Vilas Shinde
#   Description  : Write a program which accept one number form user and return addition of its factors.
#   Input        : 12          
#   Output       : 16  (1+2+3+4+6)
#   Date         : 04/05/2026
#
#######################################################################

def SumFactors(No):
    Sum = 0

    for i in range(1, int(No/2)+1):
        if No % i == 0:
            Sum = Sum + i

    return Sum

def main():
    Ret = 0

    Value = int(input("Enter number : "))
    
    Ret = SumFactors(Value)
    print("The summation of factors of",Value,"is :",Ret)

if __name__ == "__main__":
    main()