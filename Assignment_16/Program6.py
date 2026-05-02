####################################################################################################
#
#   Program Name : Assignment16_6.py
#   Author       : Apurva Vials Shinde
#   Description  : Write a program which accept number from user and check whether that number is positive or negative or zero.
#   Function     : CheckNumber(No)       
#   Input        : 11 / -8 / 0       
#   Output       : Positive Number / Negative Number / Zero
#   Date         : 01/05/2026
#
####################################################################################################

def CheckNumber(No):
    if(No > 0):
        print(No,"is Positive number.")
    elif(No < 0):
        print(No,"is Negative number.")
    else:
        print(No,"is Zero.")

def main():
    Value = int(input("Enter the number : "))
    CheckNumber(Value)

if __name__ == "__main__":
    main()
