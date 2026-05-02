####################################################################################################
#
#   Program Name : Assignment16_2.py
#   Author       : Apurva Vials Shinde
#   Description  : Write a program which contains one function named as ChkNum() which accept one parameter as number. If number is even then it should display “Even number” otherwise display “Odd number” on console.
#   Function     : ChkNum()        
#   Input        : 11 / 8            
#   Output       : Odd Number / Even Number
#   Date         : 01/05/2026
#
##############################################3#####################################################

def ChkNum(No):
    if((No % 2) == 0):
        return True
    else:
        return False

def main():
    Value = int(input("Enter the number : "))

    Ret = ChkNum(Value)

    if(Ret == True):
        print(Value,"is Even number.")
    else:
        print(Value,"is Odd number.")

if __name__ == "__main__":
    main()
