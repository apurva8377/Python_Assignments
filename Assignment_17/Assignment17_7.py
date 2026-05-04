########################################################################
#
#   Program Name : Assignment17_6.py
#   Author       : Apurva Vilas Shinde
#   Description  : Write a program which accept one number and display below pattern.
#   Input        : 4
#   Output       : 1    2   3   4
#                  1    2   3   
#                  1    2   
#                  1  
#   Date         : 04/05/2026
#
#######################################################################

def DisplyPattern(No):
    for i in range(No):
        for j in range(1,No+1):
            print(j,end=" ")
        print()

def main():
    Value = int(input("Enter number : "))
    
    DisplyPattern(Value)

if __name__ == "__main__":
    main()