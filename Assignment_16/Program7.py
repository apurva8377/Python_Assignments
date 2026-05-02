####################################################################################################
#
#   Program Name : Assignment16_7.py
#   Author       : Apurva Vials Shinde
#   Description  : Write a program which contains one function that accept one number from user and returns true if number is divisible by 5 otherwise return false.
#   Function     : CheckDivisible(No)       
#   Input        : 8 / 25       
#   Output       : False / True
#   Date         : 01/05/2026
#
####################################################################################################

def CheckDivisible(No):
    if(No % 5 == 0 and No != 0):
        return True
    else:
        return False

def main():
    Value = int(input("Enter the number : "))

    Ret = CheckDivisible(Value)

    if(Ret == True):
        print(Value,"is divisible by 5.")
    else:
        print(Value,"is not divisible by 5.")

if __name__ == "__main__":
    main()
