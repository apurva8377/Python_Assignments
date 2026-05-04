########################################################################
#
#   Program Name : Assignment17_5.py
#   Author       : Apurva Vilas Shinde
#   Description  : Write a program which accept one number for user and check whether number is prime or not.
#   Input        : 5          
#   Output       : It is prime/Not prime number.
#   Date         : 04/05/2026
#
#######################################################################

def CheckPrime(No):
    for i in range(2,No+1):
        if(No % i != 0):
            return True
        else:
            return False

def main():
    Ret = 0

    Value = int(input("Enter number : "))
    
    Ret = CheckPrime(Value)
    if(Ret == True):
        print(Value,"is prime number")
    else:
        print(Value,"is not prime number")

if __name__ == "__main__":
    main()