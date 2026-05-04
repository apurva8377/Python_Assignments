########################################################################
#
#   Program Name : Assignment17_6.py
#   Author       : Apurva Vilas Shinde
#   Description  : Write a program which accept one number and display below pattern.
#   Input        : 4         
#   Output       : *    *   *   *
#                  *    *   *   
#                  *    *   
#                  *   
#   Date         : 04/05/2026
#
#######################################################################

def DisplyPattern(No):
    for i in range(No,0,-1):
        for j in range(i):
            print("*",end=" ")
        print()

def main():
    Value = int(input("Enter number : "))
    
    DisplyPattern(Value)

if __name__ == "__main__":
    main()